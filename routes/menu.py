import flask 

menu_bp = flask.Blueprint("menu", __name__)

@menu_bp.route("/")
def renderMenu():
    return flask.render_template("menu.html")

