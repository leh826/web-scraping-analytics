from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import pandas as pd


load_dotenv()

app = FastAPI(title="API de Busca de Operadoras")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

df_operadoras = pd.read_csv("../data/csv/transformed_data.csv")

@app.get("/operadoras")
def listar_operadoras(
    nome_fantasia: str = Query(
        None,
        min_length=2,
        description="Nome parcial ou completo da operadora"
    )
):
    if nome_fantasia:
        mask = df_operadoras["Nome_Fantasia"].str.contains(nome_fantasia, case=False, na=False)
        df_filtrado = df_operadoras[mask]
    else:
        df_filtrado = df_operadoras

    df_filtrado = df_filtrado.sort_values("Nome_Fantasia").head(10)


    colunas = ["Registro_ANS", "CNPJ", "Razao_Social", "Nome_Fantasia", "Modalidade", "Representante"]
    resultado = df_filtrado[colunas].to_dict(orient="records")
    return resultado