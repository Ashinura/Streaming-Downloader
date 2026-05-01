import os
import json
import threading
from copy import deepcopy
from types import MappingProxyType

class ConfigurationError(Exception):
    pass


# =========================
# Properties
# =========================

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) 

VERSION = "v3.0.0"
CONFIG_FILE = os.path.join(ROOT_DIR, "config.json")

DEFAULT_CONFIG = {
    "user": {
        "autoupdate": True,
        "language": "fr"
    },
    "flask": {
        "debug": False,
        "ip": "127.0.0.1",
        "port": 5000
    },
    "path": {
        "default": "./downloads",
        "music": "./downloads",
        "social": "./downloads",
        "video": "./downloads"
    }
}

REGISTRED_SITES = (
    "youtube",
    "dailymotion",
    "soundcloud",
    "facebook",
    "tiktok",
    "twitter",
)

SITES_DATA = MappingProxyType({
    "default": {"category": "default", "color": "white", "lib": "ytdlp"},
    "youtube": {"category": "video", "color": "red", "lib": "ytdlp"},
    "dailymotion": {"category": "video", "color": "black", "lib": "ytdlp"},
    "soundcloud": {"category": "music", "color": "yellow", "lib": "ytdlp-sc"},
    "spotify": {"category": "music", "color": "green", "lib": "spotdl"},
    "facebook": {"category": "social", "color": "blue", "lib": "ytdlp"},
    "tiktok": {"category": "social", "color": "black", "lib": "ytdlp"},
    "twitter": {"category": "social", "color": "blue", "lib": "ytdlp"},
})

TRANSLATION = MappingProxyType({
    "fr": {
        "settings": "Paramètres",
        "destination_path": "Chemin de destination",
        "dev_page": "Page Développeur",
        "config_title": "Configuration",
        "chkbox_on": "OUI",
        "chkbox_off": "NON",
        "user_params": "Paramètres Utilisateur",
        "language": "Langue",
        "auto_update": "Mise à jour automatique",
        "flask_server": "Serveur Flask",
        "access_type": "Type d'accès",
        "access_local": "Accès Local",
        "access_network": "Accès Réseau",
        "port": "Port",
        "debug_mode": "Mode Debug",
        "default_folder": "Dossier par défaut",
        "video_folder": "Dossier vidéos",
        "music_folder": "Dossier musique",
        "social_folder": "Dossier réseaux sociaux",
        "browse": "Parcourir",
        "reset": "Réinitialiser",
        "auto_save_info": "Sauvegarde automatique", 
        "go_back": "Retour",
        "actual_version": "Version Actuelle",
        "update_available": "MaJ disponible"
    },
    "en": {
        "settings": "Settings",
        "destination_path": "Destination Path",
        "dev_page": "Developer Page",
        "config_title": "Configuration",
        "chkbox_on": "ON",
        "chkbox_off": "OFF",
        "user_params": "User Settings",
        "language": "Language",
        "auto_update": "Automatic Update",
        "flask_server": "Flask Server",
        "access_type": "Access Type",
        "access_local": "Local Access (12)",
        "access_network": "Network Access",
        "port": "Port",
        "debug_mode": "Debug Mode",
        "default_folder": "Default Folder",
        "video_folder": "Video Folder",
        "music_folder": "Music Folder",
        "social_folder": "Social Media Folder",
        "browse": "Browse",
        "reset": "Reset",
        "auto_save_info": "Auto-save enabled",
        "go_back": "Back",
        "actual_version": "Actual Version",
        "update_available": "Update available"
    }
})


# =========================
# Runtime
# =========================

def loadConfig():
    """Charge la config du fichier JSON ou crée une config par défaut"""
    if not os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "w", encoding="utf-8") as f:
                json.dump(DEFAULT_CONFIG, f, indent=4, ensure_ascii=False)
            print(f"[INFO] - Fichier {CONFIG_FILE} créé avec les paramètres par défaut")
        except Exception as e:
            print(f"[ERROR] - Erreur lors de la création du fichier config: {e}")
        return deepcopy(DEFAULT_CONFIG)
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            loaded = json.load(f)
            base = deepcopy(DEFAULT_CONFIG)
            for section, values in loaded.items():
                if section in base:
                    base[section].update(values)
            return base
    except Exception as e:
        print(f"[ERROR] - Erreur lecture config.json: {e}")
    return deepcopy(DEFAULT_CONFIG)

def saveConfig(config_to_save):
    """Enregistre la config sur le disque"""
    try:
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(config_to_save, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"[ERROR] - Erreur écriture config.json: {e}")

_lock = threading.RLock()
_config = loadConfig()


# =========================
# API Utils
# =========================

def getConfig():
    with _lock:
        return deepcopy(_config)


def updateConfig(new_data: dict):
    if not isinstance(new_data, dict):
        raise ConfigurationError("[ERROR] - updateConfig attend un dictionnaire")

    with _lock:
        for section, values in new_data.items():
            if section not in _config:
                raise ConfigurationError(f"[ERROR] - Section inconnue: {section}")
            if not isinstance(values, dict):
                raise ConfigurationError(f"[ERROR] - La section '{section}' doit être un dictionnaire")
            
            _config[section].update(values)
        
        saveConfig(_config)


def resetConfig():
    with _lock:
        _config = deepcopy(DEFAULT_CONFIG)
        saveConfig(_config)