import flask

config_bp = flask.Blueprint("config", __name__)

@config_bp.route("/config")
def renderConfig():
    return flask.render_template("config.html")