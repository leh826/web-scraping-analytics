import psycopg2
import csv
import os
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST", "localhost"),
    port=os.getenv("POSTGRES_PORT", "5432"),
)
cur = conn.cursor()

folder_csv = "csv"
file_name = "Relatorio_cadop.csv"
file_csv = os.path.join(folder_csv, file_name)

# Verifica se o arquivo existe antes de tentar abrir
if not os.path.exists(file_csv):
    print(f"Erro: Arquivo {file_csv} não encontrado!")
    exit(1)

# Ler e inseri dados no PostgreSQL
with open(file_csv, "r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=";")
    next(reader)  # Pula cabeçalho
    
    for row in reader:
        # Converter valores vazios para NULL no PostgreSQL
        row = [None if val == "" else val for val in row]

        try:
            cur.execute(
                """
                INSERT INTO operadoras (
                    registro_ans, cnpj, razao_social, nome_fantasia, modalidade, logradouro, 
                    numero, complemento, bairro, cidade, uf, cep, ddd, telefone, fax, 
                    endereco_eletronico, representante, cargo_representante, regiao_comercializacao, data_registro_ans
                ) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
                row
            )
        except psycopg2.Error as e:
            print(f"\nErro ao inserir linha: {row}")
            print(f"Erro do PostgreSQL: {e}\n")

conn.commit()
cur.close()
conn.close()

print("Importação concluída!")
