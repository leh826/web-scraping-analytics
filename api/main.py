from fastapi import FastAPI
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

conn = psycopg2.connect(
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST", "localhost"),
    port=os.getenv("POSTGRES_PORT", "5432"),
)

def get_db_connection():
    return conn

@app.get("/operadoras")
def listar_operadoras():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM ans_operadoras")
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data
