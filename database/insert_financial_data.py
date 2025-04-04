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
    
    # Inserir dados
    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO dados_financeiros (data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            row["DATA"], 
            row["REG_ANS"], 
            row["CD_CONTA_CONTABIL"], 
            row["DESCRICAO"], 
            row["VL_SALDO_INICIAL"] if not pd.isna(row["VL_SALDO_INICIAL"]) else 0.0,  # Substituir NULL por 0.0
            row["VL_SALDO_FINAL"] if not pd.isna(row["VL_SALDO_FINAL"]) else 0.0   # Substituir NULL por 0.0
        ))
    
    conn.commit()
    cur.close()
    conn.close()
    print("Dados financeiros inseridos com sucesso!")