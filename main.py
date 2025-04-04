import os
from data_transformation.transform_data_register import transform_data
from database.connection import execute_query
from database.insert import insert_data

print("Criando tabelas...")
with open("database/Queries/schema.sql", "r") as file:
    execute_query(file.read())

print("Processando CSV...")
transform_data("data/csv/Relatorio_cadop.csv", "data/csv/transformed_data.csv")

print("Inserindo dados...")
insert_data("data/csv/transformed_data.csv")

print("Processo concluído!")
