import os
import threading
from copy import deepcopy
from types import MappingProxyType


# =========================
# Config
# =========================

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) 

VERSION = "v3.0.0"

DEFAULT_CONFIG = {
    "user": {
        "autoupdate": False,
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

CURRENT_CONFIG = {
    "user": {
        "autoupdate": True,
        "language": "fr"
    },
    "flask": {
        "debug": True,
        "ip": "0.0.0.0",
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
    # TODO
})


# =========================
# Runtime
# =========================

class ConfigurationError(Exception):
    pass

_lock = threading.RLock()
_config = deepcopy(CURRENT_CONFIG)


# =========================
# API
# =========================

def getConfig():
    with _lock:
        return deepcopy(_config)

def updateConfig(new_data: dict):
    if not isinstance(new_data, dict):
        raise ConfigurationError("updateConfig attend un dictionnaire")

    with _lock:
        for key, value in new_data.items():
            if key not in _config:
                raise ConfigurationError(f"Section inconnue: {key}")
            if not isinstance(value, dict):
                raise ConfigurationError(f"La section '{key}' doit être un dictionnaire")
            print(_config[key])
            print(value)
            _config[key].update(value)


def setValue(path: str, value):
    keys = path.split(".")
    with _lock:
        current = _config
        for k in keys[:-1]:
            if k not in current:
                raise ConfigurationError(f"Clé inconnue: {k}")
            current = current[k]
        current[keys[-1]] = value


def resetConfig():
    global _config
    with _lock:
        _config = deepcopy(DEFAULT_CONFIG)
