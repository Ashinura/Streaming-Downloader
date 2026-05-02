from flask import Blueprint, render_template
from core.properties import VERSION

menu_bp = Blueprint("menu", __name__)

@menu_bp.route("/")
def renderMenu():
    return render_template("menu.html", version=VERSION)