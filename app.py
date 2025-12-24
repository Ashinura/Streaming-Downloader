import flask
from routes.menu import menu_bp
from routes.api import api_bp
from properties import getConfig

app = flask.Flask(__name__)
app.register_blueprint(menu_bp)
app.register_blueprint(api_bp)

if __name__ == "__main__":
    try:
        flaskConfig = getConfig()["flask"]

        app.run(
            host=flaskConfig.get("ip", "127.0.0.1"),
            port=flaskConfig.get("port", 5000),
            debug=flaskConfig.get("debug", False)
        )
    except Exception as e:
        print(f"Erreur au démarrage : {e}")
