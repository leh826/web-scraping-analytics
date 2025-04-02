import pandas as pd

# Carregar o arquivo CSV
arquivo_csv = 'data/csv/1T2024.csv'
dados = pd.read_csv(arquivo_csv, delimiter=";", encoding="utf-8")

# Exibir as primeiras linhas do CSV
print(dados.head())

# Obter informações gerais sobre os dados
print(dados.info())