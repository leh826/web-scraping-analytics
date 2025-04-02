import os
from data_transformation.transform_data_register import transform_data
from database.connection import execute_query
from database.insert import insert_data

# 1. Criar as tabelas no banco
print("Criando tabelas...")
with open("database/schema.sql", "r") as file:
    execute_query(file.read())

# 2. Transformar o CSV
print("Processando CSV...")
transform_data("data/csv/Relatorio_cadop.csv", "data/csv/transformed_data.csv")

# 3. Inserir os dados no banco
print("Inserindo dados...")
insert_data("data/csv/transformed_data.csv")

print("Processo concluído!")
