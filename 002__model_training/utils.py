from pathlib import Path
import requests
import os
import zipfile


download_folder = Path(".") / "dataset"

if not os.path.exists(download_folder):
    os.mkdir(download_folder)

def download_dataset():
    url = "https://www.kaggle.com/api/v1/datasets/download/ldausl/regression-with-an-insurance"
    file_path = download_folder / "fichier.zip"

    response = requests.get(url, allow_redirects=True)
    if response.status_code == 200:
        with open(file_path, "wb") as file:
            file.write(response.content)
        print("Fichier correctement téléchargé")
    else:
        print("Erreur au téléchargement")

    with zipfile.ZipFile(file_path, "r") as zip_ref:
        zip_ref.extractall(download_folder)
