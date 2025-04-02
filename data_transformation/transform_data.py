import pandas as pd
import numpy as np
import zipfile
import os
import shutil

def extract_csv_from_zip(source_folder, destination_folder):
    os.makedirs(destination_folder, exist_ok=True)
    
    # Percorre todos os arquivos na pasta de origem
    for file in os.listdir(source_folder):
        if file.endswith(".zip"): 
            zip_path = os.path.join(source_folder, file)
            
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                for zip_file in zip_ref.namelist():
                    if zip_file.endswith(".csv"): 
                        extracted_path = zip_ref.extract(zip_file, destination_folder)
                        print(f"Extraído: {extracted_path}")

source_folder = "data/zips"
destination_folder = "data/csv"

extract_csv_from_zip(source_folder, destination_folder)