import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def insert_data(csv_file):
    df = pd.read_csv(csv_file, delimiter=",", encoding="utf-8", dtype=str)

    conn = psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("POSTGRES_HOST", "localhost"),
        port=os.getenv("POSTGRES_PORT", "5432"),
    )
    cur = conn.cursor()

    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO ans_operadoras (registro_ans, cnpj, razao_social, nome_fantasia, modalidade, logradouro, numero, complemento, bairro, cidade, uf, cep, ddd, telefone, fax, endereco_eletronico, representante, cargo_representante, regiao_comercializacao, data_registro_ans)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """, tuple(row))

    conn.commit()
    cur.close()
    conn.close()
    print("Dados inseridos com sucesso!")

if __name__ == "__main__":
    insert_data("csv/transformed_data.csv")
