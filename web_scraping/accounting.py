import requests
from bs4 import BeautifulSoup
import os
from zipfile import ZipFile

url_base = "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/"

page = requests.get(url_base)
soup = BeautifulSoup(page.content, 'html.parser')

folder_zips = "zips"
os.makedirs(folder_zips, exist_ok=True)

years = []
for a_tag in soup.find_all('a', href=True):
    href = a_tag['href']
    if href[:-1].isdigit(): 
        years.append(int(href[:-1]))

# Baixa os 2 ultimos anos
years.sort(reverse=True)
anos_para_baixar = years[:2]

#baixa os arquivos
for ano in anos_para_baixar:
    url_ano = f"{url_base}{ano}/"
    page_ano = requests.get(url_ano)
    soup_ano = BeautifulSoup(page_ano.content, 'html.parser')
    
    #verificado que os arquivos são 
    for a_tag in soup_ano.find_all('a', href=True):
        href = a_tag['href']
        if href.endswith(".zip"):
            url_zip = f"{url_ano}{href}"
            nome_arquivo = os.path.join(folder_zips, os.path.basename(href))
            
            response = requests.get(url_zip)
            if response.status_code == 200:
                with open(nome_arquivo, "wb") as file:
                    file.write(response.content)
                print(f"Download completed: {nome_arquivo}")
            else:
                print(f"Download Error: {url_zip}")

print("Download done!")