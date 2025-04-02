import requests
from bs4 import BeautifulSoup
import os
from zipfile import ZipFile

url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
page = requests.get(url)
data_page = BeautifulSoup(page.content, 'html.parser')

# uids dos links desejados
uids = ["f710899c6c7a485ea62a1acc75d86c8c", "85adaa3de5464d8aadea11456bfb4f94"]

folder_pdfs = "data\pdfs"
os.makedirs(folder_pdfs, exist_ok=True)

#armazenando os caminhos dos PDFs baixados
files_pdfs = []

for a_tag in data_page.find_all('a', attrs={"data-mce-href": True, "href": True}):
    if any(uid in a_tag["data-mce-href"] for uid in uids):
        url_pdf = a_tag["href"]
        
        # Obtém o nome do arquivo
        name_file = os.path.join(folder_pdfs, os.path.basename(url_pdf))     
        # Faz o download do PDF
        response = requests.get(url_pdf)

        if response.status_code == 200:
            with open(name_file, "wb") as file:
                file.write(response.content)
            files_pdfs.append(name_file)
            print(f"Download completo: {name_file}")
        else:
            print(f"Erro no download: {url_pdf}")

# Compactando todos os PDFs
if files_pdfs:

    name_zip = os.path.join(folder_pdfs,"files_pdfs.zip")
    with ZipFile(name_zip, 'w') as zipf:
        for file in files_pdfs:
            zipf.write(file, os.path.basename(file))
    print(f"File zip em: {name_zip}")
else:
    print("Nenhum Pdf baixado.")

# Salvando uma lista com os PDFs 
with open(os.path.join( "pdf_list.txt"), "w") as f:
    for pdf_path in files_pdfs:
        f.write(pdf_path + "\n")