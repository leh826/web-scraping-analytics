import os
import pandas as pd
import re

def process_csv_for_postgres():
    caminho_pasta = "data/csv"

    arquivos_csv = [arquivo for arquivo in os.listdir(caminho_pasta) if arquivo.endswith(".csv")]

    arquivos_filtrados = [arquivo for arquivo in arquivos_csv if re.match(r"^\d", arquivo)]

    df_lista = []

    # Ler e transformar os arquivos filtrados
    for arquivo in arquivos_filtrados:
        caminho_arquivo = os.path.join(caminho_pasta, arquivo)
        
        dtype_spec = {
            "REG_ANS": str,
            "CD_CONTA_CONTABIL": str,
            "DESCRICAO": str,
        }

        df = pd.read_csv(caminho_arquivo, delimiter=";", encoding="utf-8", dtype=dtype_spec)

        # Converter a coluna "DATA" para o tipo Date
        df["DATA"] = pd.to_datetime(df["DATA"], errors="coerce")

        # Converter colunas numéricas (garantindo que valores inválidos sejam convertidos para 0.0)
        df["VL_SALDO_INICIAL"] = (
            df["VL_SALDO_INICIAL"]
            .astype(str)
            .str.replace(",", ".", regex=True)
            .replace("", "0") 
            .astype(float)
        )
        
        df["VL_SALDO_FINAL"] = (
            df["VL_SALDO_FINAL"]
            .astype(str)
            .str.replace(",", ".", regex=True)
            .replace("", "0")  
            .astype(float)
        )

        # Converter colunas para string (VARCHAR no banco)
        df["REG_ANS"] = df["REG_ANS"].astype(str)
        df["CD_CONTA_CONTABIL"] = df["CD_CONTA_CONTABIL"].astype(str)
        
        df_lista.append(df)

    # Concatenar todos os DataFrames em um único DataFrame consolidado
    df_final = pd.concat(df_lista, ignore_index=True)

    # Exibir as primeiras linhas do DataFrame consolidado
    print(df_final.head())

    df_final.to_csv("data/csv/adjusted_data.csv", index=False, encoding="utf-8", sep=",", quotechar='"')

    print("Arquivo processado e salvo com sucesso!")
