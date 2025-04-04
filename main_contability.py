
#from data_transformation.extract_csv_zip import extract_csv_from_zip
import os
from data_transformation.transform_finances import process_csv_for_postgres
from database.connection import execute_query
from database.insert_financial_data import insert_financial_data

# 1. Criar as tabelas no banco
print("Criando tabelas...")
with open("database/Queries/finance.sql", "r") as file:
    execute_query(file.read())

# 2. Processar os arquivos CSV
print("Processando arquivos financeiros...")
process_csv_for_postgres()

# 3. Inserir os dados transformados no banco de dados
print("Inserindo dados financeiros...")
insert_financial_data("data/csv/adjusted_data.csv")

print("Processo concluído!")
