from flask import Blueprint, render_template

config_bp = Blueprint("config", __name__)

@config_bp.route("/config")
def renderConfig():
    return render_template("config.html")