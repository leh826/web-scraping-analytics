# import os
# import csv
# from datetime import datetime
# def format_value(value, is_numeric=False):
#     """ Formata valores removendo espaços e convertendo para o formato correto. """
#     value = value.strip().replace('"', '')  # Remove espaços extras e aspas
#     if is_numeric:
#         return value.replace(',', '.') if value else '0.00'  # Converte para formato decimal
#     return value

# def process_csv_for_postgres(csv_folder, output_file):
#     with open(output_file, 'w', encoding='utf-8') as sql_file:
#         sql_file.write("CREATE TABLE IF NOT EXISTS contabilidade (\n")
#         sql_file.write("    data DATE,\n")
#         sql_file.write("    reg_ans VARCHAR(10),\n")
#         sql_file.write("    cd_conta_contabil VARCHAR(20),\n")
#         sql_file.write("    descricao TEXT,\n")
#         sql_file.write("    vl_saldo_inicial NUMERIC(15,2),\n")
#         sql_file.write("    vl_saldo_final NUMERIC(15,2)\n");
#         sql_file.write(");\n\n")
        
#         for file in os.listdir(csv_folder):
#             if file.endswith(".csv"):
#                 csv_path = os.path.join(csv_folder, file)
#                 with open(csv_path, newline='', encoding='utf-8') as csv_file:
#                     reader = csv.reader(csv_file, delimiter=';')
#                     next(reader) 
#                     for row in reader:
#                         data = datetime.strptime(format_value(row[0]), "%Y-%m-%d").date()
#                         reg_ans = format_value(row[1])
#                         cd_conta_contabil = format_value(row[2])
#                         descricao = format_value(row[3])
#                         vl_saldo_inicial = format_value(row[4], is_numeric=True)
#                         vl_saldo_final = format_value(row[5], is_numeric=True)
#                         sql_file.write(
#                             f"INSERT INTO contabilidade VALUES ('{data}', '{reg_ans}', '{cd_conta_contabil}', "
#                             f"'{descricao}', {vl_saldo_inicial}, {vl_saldo_final});\n"
#                         )

# destination_folder = "database"
# output_sql = "finance.sql"

# process_csv_for_postgres(destination_folder, output_sql)

import pandas as pd

# Carregar o arquivo CSV
dados = pd.read_csv('seuarquivo.csv', delimiter=";", encoding="utf-8") #ajustar para ler a pasta
# Converter a coluna "DATA" para o tipo Date
dados['DATA'] = pd.to_datetime(dados['DATA'], errors='coerce')

# Converter colunas numéricas para o formato correto (NUMERIC(15,2))
dados['VL_SALDO_INICIAL'] = pd.to_numeric(dados['VL_SALDO_INICIAL'], errors='coerce')
dados['VL_SALDO_FINAL'] = pd.to_numeric(dados['VL_SALDO_FINAL'], errors='coerce')

# Converter colunas para VARCHAR
dados['REG_ANS'] = dados['REG_ANS'].astype(str)
dados['CD_CONTA_CONTABIL'] = dados['CD_CONTA_CONTABIL'].astype(str)

# Salvar em um novo arquivo CSV
dados.to_csv('dados_ajustados.csv', index=False, sep=",", encoding="utf-8", quotechar='"')