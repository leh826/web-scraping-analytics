import pandas as pd

def transform_data(input_file, output_file):
    # Especifica todas as colunas a serem lidas como string
    dtype_spec = {
        "Registro_ANS": str,
        "CNPJ": str,
        "CEP": str,
        "DDD": str,
        "Telefone": str,
        "Fax": str,
        "UF": str
    }
    df = pd.read_csv(input_file, delimiter=";", encoding="utf-8", dtype=dtype_spec)

    # Remover espaços extras nas colunas de texto
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # Preencher valores NaN e strings vazias com "null"
    df = df.replace({"": "null", None: "null"}).fillna("null")

    # Corrigir DDD, Telefone e Fax (removendo .0 no final)
    df["DDD"] = df["DDD"].astype(str).str.replace(r"\.0$", "", regex=True)
    df["Telefone"] = df["Telefone"].astype(str).str.replace(r"\.0$", "", regex=True)
    df["Fax"] = df["Fax"].astype(str).str.replace(r"\.0$", "", regex=True)

    # Converter Regiao_de_Comercializacao para inteiro (preenchendo vazios com 0)
    df["Regiao_de_Comercializacao"] = df["Regiao_de_Comercializacao"].replace("null", "0").astype(int)

    # Converter Data_Registro_ANS para formato de data (deixando "null" onde for inválido)
    df["Data_Registro_ANS"] = pd.to_datetime(df["Data_Registro_ANS"], errors="coerce").dt.date
    df["Data_Registro_ANS"] = df["Data_Registro_ANS"].astype(str).replace("NaT", "null")

    # Salvar o dataframe transformado em um novo arquivo CSV
    df.to_csv(output_file, index=False, sep=",", encoding="utf-8", quotechar='"')
    print("Transformação concluída. Dados salvos em:", output_file)

if __name__ == "__main__":
    transform_data("data/csv/Relatorio_cadop.csv", "data/csv/transformed_data.csv")


    
