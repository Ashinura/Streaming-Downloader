from os import path, listdir, walk, remove
from requests import get
from zipfile import ZipFile
from io import BytesIO
from shutil import rmtree, copytree, copy2
from filecmp import cmp
from subprocess import run
from sys import executable
from core.properties import VERSION, ROOT_DIR


GITHUB_REPO = "Ashinura/Streaming-Downloader"
API_URL = f"https://api.github.com/repos/{GITHUB_REPO}/releases/latest"

# Test Dev
BRANCH_NAME = "release/3.0.0"
TEST_URL = f"https://github.com/{GITHUB_REPO}/archive/refs/heads/{BRANCH_NAME}.zip"

# Liste des fichiers/dossiers locaux qui ne doivent pas être touchés par l'updater
PROTECTED_ITEMS = {
    "temp_update",                  # Dossier créé pendant l'update
    "core/config.json",             # Config utilisateur 
    ".venv",                        # Env
    ".git",                         # Dossier git local
    ".gitattributes",               # LF Lines Ending 
    "static/img/str_dl-logo.ico",   # Logo 
    "StrDL.py",                     # Évite de se remplacer soi-même pendant le run
}

def getLatestRelease():
    if "test" in VERSION:
        return None

    if TEST_URL and VERSION != "v3.0.0-test":
        return {
            "tag_name": "v3.0.0-test",
            "zipball_url": TEST_URL
        }
    try:
        response = get(TEST_URL, timeout=10)  # Changer par API_URL en prod
        if response.status_code == 200:
            return response.json()
    except Exception as error:
        print(f"[ERROR] - Erreur check MAJ : {error}")
    return None

def checkRemoteVersion():
    """
    Compare la version locale avec la version distante sans lancer d'update.
    Retourne le tag_name s'il est différent de la version actuelle.
    """
    data = getLatestRelease()
    if data:
        new_version = data.get('tag_name')
        if new_version != VERSION:
            return new_version
    return None

def updateProject():
    release_data = getLatestRelease()
    if not release_data or release_data.get('tag_name') == VERSION:
        return False

    print(f"[UPDATE] - Installation de la version {release_data['tag_name']}...")

    try:
        response_archive = get(release_data['zipball_url'])

        with ZipFile(BytesIO(response_archive.content)) as zip_file:
            extract_path = path.join(ROOT_DIR, "temp_update")
            if path.exists(extract_path):
                rmtree(extract_path)
            zip_file.extractall(extract_path)

        items = listdir(extract_path)
        subfolder_path = next(
            path.join(extract_path, i)
            for i in items
            if path.isdir(path.join(extract_path, i))
        )

        for item_name in listdir(subfolder_path):
            source_item = path.join(subfolder_path, item_name)
            destination_item = path.join(ROOT_DIR, item_name)

            relative_path = path.relpath(destination_item, ROOT_DIR).replace("\\", "/")
            if relative_path in PROTECTED_ITEMS or item_name in PROTECTED_ITEMS:
                print(f"[UPDATE] - Protégé : {relative_path}")
                continue

            if path.isdir(source_item):
                if path.exists(destination_item):
                    rmtree(destination_item)
                copytree(source_item, destination_item)
                print(f"[UPDATE] - Dossier copié : {item_name}")

            else:
                # Ne copie que si le fichier est différent ou inexistant
                if path.exists(destination_item) and cmp(source_item, destination_item, shallow=False):
                    print(f"[UPDATE] - Identique : {item_name}")
                else:
                    copy2(source_item, destination_item)
                    print(f"[UPDATE] - Fichier copié : {item_name}")

        rmtree(extract_path)
        installRequirements()
        cleanPycache(ROOT_DIR)
        print(f"[UPDATE] - Mise à jour terminée")
        return True

    except Exception as error:
        print(f"[ERROR] - Erreur pendant l'update : {error}")
        return False
    

def installRequirements():
    """Mets à jour les dépendances depuis utils/requirements.txt"""
    requirements_path = path.join(ROOT_DIR, "utils", "requirements.txt")
    if path.exists(requirements_path):
        print("[UPDATE] - Mise à jour des dépendances...")
        try:
            result = run(
                [executable, "-m", "pip", "install", "-r", requirements_path],
                capture_output=True,
                text=True,
                check=False
            )
            if result.stdout:
                print(result.stdout.strip())
            if result.returncode == 0:
                print("[INFO] - Dépendances à jour")
            else:
                print(f"[WARN] - pip install a retourné : {result.returncode}")
                if result.stderr:
                    print(result.stderr)
        except Exception as e:
            print(f"[ERROR] - Erreur pip install : {e}")

def cleanPycache(root_dir):
    """Supprime tous les __pycache__ et fichiers .pyc"""
    for dirpath, dirnames, filenames in walk(root_dir):
        if ".venv" in dirnames:
            dirnames.remove(".venv")
        if "__pycache__" in dirnames:
            cache_path = path.join(dirpath, "__pycache__")
            try:
                rmtree(cache_path)
                print(f"[UPDATE] - Cache supprimé : {path.relpath(cache_path, root_dir)}")
            except Exception as e:
                print(f"[WARN] - {e}")
    # Supprime les .pyc orphelins
    for dirpath, dirnames, filenames in walk(root_dir):
        if ".venv" in dirpath:
            continue
        for f in filenames:
            if f.endswith(".pyc"):
                pyc_path = path.join(dirpath, f)
                py_path = pyc_path[:-1]
                if not path.exists(py_path):
                    try:
                        remove(pyc_path)
                        print(f"[UPDATE] - .pyc orphelin supprimé : {path.relpath(pyc_path, root_dir)}")
                    except Exception as e:
                        print(f"[WARN] - {e}")