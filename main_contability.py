from data_transformation.extract_csv_zip import extract_csv_from_zip
from data_transformation.transform_finances import process_csv_for_postgres
from database.connection import execute_query


print("Extraindo dados dos zips..")
extract_csv_from_zip()

print("Criando tabelas...")
with open("database/Queries/finance.sql", "r") as file:
    execute_query(file.read())

print("Processando arquivos financeiros...")
process_csv_for_postgres()

print("Arquivo gerado e tabelas criadas com sucesso!")
