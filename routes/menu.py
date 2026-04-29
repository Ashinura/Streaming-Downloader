import flask
from properties import VERSION
from StrDL import remote_version

menu_bp = flask.Blueprint("menu", __name__)

@menu_bp.route("/")
def renderMenu():
    return flask.render_template("menu.html", version=VERSION, update_available=remote_version)