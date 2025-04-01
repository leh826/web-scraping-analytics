from fastapi import FastAPI
import psycopg2

app = FastAPI()

def get_db_connection():
    return psycopg2.connect("dbname=meubanco user=postgres password=senha host=localhost")

@app.get("/operadoras")
def listar_operadoras():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM operadoras")
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data
