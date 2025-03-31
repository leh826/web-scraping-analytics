import requests
from bs4 import BeautifulSoup
import os

url = "https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/"

folder_csv = "csv"
os.makedirs(folder_csv, exist_ok=True)

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

#encontra o primeiro link que termina em .csv
csv_link = None
for a_tag in soup.find_all("a"):
    href = a_tag.get("href")
    if href and href.endswith(".csv"):
        csv_link = url + href 
        break 
    
if csv_link:
    file_name = os.path.join(folder_csv, os.path.basename(csv_link))
    
    #download do CSV
    csv_response = requests.get(csv_link)
    if csv_response.status_code == 200:
        with open(file_name, "wb") as file:
            file.write(csv_response.content)
        print(f"Download concluído: {file_name}")
    else:
        print("Erro ao baixar o arquivo.")
else:
    print("Nenhum arquivo CSV encontrado.")
