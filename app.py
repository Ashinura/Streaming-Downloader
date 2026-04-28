import flask
from flask import config
from routes.menu import menu_bp
from routes.config import config_bp
from routes.api import api_bp
from properties import getConfig, TRANSLATION

app = flask.Flask(__name__)
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
    
    return dict(trad=get_text)