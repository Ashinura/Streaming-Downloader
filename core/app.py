from os import path 
from flask import Flask 
from routes.menu import menu_bp
from routes.config import config_bp
from routes.api import api_bp
from core.properties import getConfig, TRANSLATION, ROOT_DIR

TEMPLATES_DIR = path.join(ROOT_DIR, 'templates')
STATIC_DIR = path.join(ROOT_DIR, 'static')

app = Flask(__name__, template_folder=TEMPLATES_DIR, static_folder=STATIC_DIR)
app.register_blueprint(menu_bp)
app.register_blueprint(config_bp)
app.register_blueprint(api_bp, url_prefix='/api')

@app.context_processor
def utility_processor():
    def get_text(key):
        userConfig = getConfig().get("user", {})
        lang = userConfig.get("language", "fr")

        texts = TRANSLATION.get(lang, TRANSLATION["fr"])

        return texts.get(key, key)
    
    return dict(
        trad=get_text,
        update_available=app.config.get('REMOTE_VERSION')
    )