import requests
from bs4 import BeautifulSoup
import os
from zipfile import ZipFile

url_base = "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/"

page = requests.get(url_base)
soup = BeautifulSoup(page.content, 'html.parser')

folder_zips = "data\zips"
os.makedirs(folder_zips, exist_ok=True)

years = []
for a_tag in soup.find_all('a', href=True):
    href = a_tag['href']
    if href[:-1].isdigit(): 
        years.append(int(href[:-1]))

# Baixa os 2 ultimos anos
years.sort(reverse=True)
years_to_download = years[:2]

#baixa os arquivos
for year in years_to_download:
    url_year = f"{url_base}{year}/"
    page_year = requests.get(url_year)
    soup_year = BeautifulSoup(page_year.content, 'html.parser')
    
    #verificado tipo zip 
    for a_tag in soup_year.find_all('a', href=True):
        href = a_tag['href']
        if href.endswith(".zip"):
            url_zip = f"{url_year}{href}"
            name_file = os.path.join(folder_zips, os.path.basename(href))
            
            response = requests.get(url_zip)
            if response.status_code == 200:
                with open(name_file, "wb") as file:
                    file.write(response.content)
                print(f"Download completed: {name_file}")
            else:
                print(f"Download Error: {url_zip}")

print("Download done!")