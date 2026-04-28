import os
import requests
import zipfile
import io
import shutil
from properties import VERSION, ROOT_DIR


GITHUB_REPO = "Ashinura/Streaming-Downloader" 
API_URL = f"https://api.github.com/repos/{GITHUB_REPO}/releases/latest"

# Liste des fichiers/dossiers locaux qui ne doivent pas être touchés par l'updater
PROTECTED_ITEMS = {
    "temp_update", # Dossier créer pendant l'update 
    "config.json", 
    ".venv", # Default Env
    ".strdl", # Env
    ".git", 
    "StrDL.py" # Evite de se remplacer soi-même pendant le run
}

def getLatestRelease():
    try:
        response = requests.get(API_URL, timeout=10)
        if response.status_code == 200:
            return response.json()
    except Exception as error:
        print(f"Erreur check MAJ : {error}")
    return None

def updateProject():
    release_data = getLatestRelease()
    if not release_data or release_data.get('tag_name') == VERSION:
        return False

    print(f"Installation de la version {release_data['tag_name']}...")
    
    try:
        response_archive = requests.get(release_data['zipball_url'])
        zip_file = zipfile.ZipFile(io.BytesIO(response_archive.content))
        
        extract_path = os.path.join(ROOT_DIR, "temp_update")
        if os.path.exists(extract_path):
            shutil.rmtree(extract_path)
        zip_file.extractall(extract_path)
        
        subfolder_name = os.listdir(extract_path)[0]
        subfolder_path = os.path.join(extract_path, subfolder_name)

        for item_name in os.listdir(subfolder_path):
            if item_name in PROTECTED_ITEMS:
                continue
            
            source_item = os.path.join(subfolder_path, item_name)
            destination_item = os.path.join(ROOT_DIR, item_name)
            
            if os.path.isdir(source_item):
                if os.path.exists(destination_item): 
                    shutil.rmtree(destination_item)
                shutil.copytree(source_item, destination_item)

            else:
                shutil.copy2(source_item, destination_item)
        
        shutil.rmtree(extract_path)
        return True

    except Exception as error:
        print(f"Erreur pendant l'update : {error}")
        return False