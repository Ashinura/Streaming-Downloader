import flask
from core.properties import VERSION

menu_bp = flask.Blueprint("menu", __name__)

@menu_bp.route("/")
def renderMenu():
    return flask.render_template("menu.html", version=VERSION)