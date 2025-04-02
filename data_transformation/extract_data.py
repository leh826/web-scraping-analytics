import pdfplumber
import pandas as pd
import os
from zipfile import ZipFile

csv_filename = "Dados_rol.csv"
zip_filename = "Teste_Leticia.zip"

folder_pdfs = "pdfs"
pdf_list_path = os.path.join(folder_pdfs, "pdf_list.txt")

#verificações de possiveis erros
if not os.path.exists(pdf_list_path):
    raise FileNotFoundError("Arquivo pdf_list.txt não encontrado.")

#procura nome 1 em pdf_list.txt
with open(pdf_list_path, "r", encoding="utf-8") as file:
    first_pdf_name = file.readline().strip()

#determina o caminho
pdf_path = os.path.join(first_pdf_name)

# verificação de possivel erro
if not os.path.exists(pdf_path):
    raise FileNotFoundError(f"O arquivo PDF {first_pdf_name} não foi encontrado no diretório {folder_pdfs}.")

#definição das colunas do pdf
colunas = [
    "PROCEDIMENTO", "RN (alteração)", "VIGÊNCIA", "OD", "AMB", "HCO", "HSO", 
    "REF", "PAC", "DUT", "SUBGRUPO", "GRUPO", "CAPÍTULO"
]

def extract_table_from_pdf(pdf_path):
    data = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()
            if tables:
                for table in tables:
                    for row in table:
                        if row:
                            data.append(row)
    return data

#extração dos dados
data = extract_table_from_pdf(pdf_path)

df = pd.DataFrame(data)

#substituindo abreviações
df.replace({
    "OD": "Seg. Odontológica",
    "AMB": "Seg. Ambulatorial"}
    , inplace=True)

df.to_csv(csv_filename, index=False, encoding='utf-8')

with ZipFile(zip_filename, 'w') as zipf:
    zipf.write(csv_filename)

print(f"Arquivo CSV salvo e compactado como {zip_filename}")
