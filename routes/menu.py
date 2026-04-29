import flask
from properties import VERSION
import StrDL

menu_bp = flask.Blueprint("menu", __name__)

@menu_bp.route("/")
def renderMenu():
    print(StrDL.remote_version)
    return flask.render_template("menu.html", version=VERSION, update_available=StrDL.remote_version)