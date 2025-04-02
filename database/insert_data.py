import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def insert_financial_data(csv_file):
    # Ler o arquivo transformado
    df = pd.read_csv(csv_file, delimiter=",", encoding="utf-8", dtype=str)
    
    # Conectar ao banco PostgreSQL
    conn = psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("POSTGRES_HOST", "localhost"),
        port=os.getenv("POSTGRES_PORT", "5432"),
    )
    cur = conn.cursor()
    
    # Criar tabela se não existir (ajuste conforme seu schema)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS dados_financeiros (
            id SERIAL PRIMARY KEY,
            data DATE,
            reg_ans VARCHAR(20),
            cd_conta_contabil VARCHAR(50),
            descricao TEXT,
            vl_saldo_inicial NUMERIC(15,2),
            vl_saldo_final NUMERIC(15,2),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    
    # Inserir dados
    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO dados_financeiros (data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
            VALUES (%s, %s, %s, %s, %s, %s);
        """, (
            row['data'],
            row['reg_ans'],
            row['cd_conta_contabil'],
            row['descricao'],
            float(row['vl_saldo_inicial']) if row['vl_saldo_inicial'] else None,
            float(row['vl_saldo_final']) if row['vl_saldo_final'] else None
        ))
    
    conn.commit()
    cur.close()
    conn.close()
    print("Dados financeiros inseridos com sucesso!")

if __name__ == "__main__":
    insert_financial_data("csv/transformed_financial_data.csv")