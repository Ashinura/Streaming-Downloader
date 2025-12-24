from flask import Blueprint, jsonify, request, render_template
from properties import (
    VERSION,
    getConfig,
    updateConfig,
    resetConfig,
    ConfigurationError,
)

api_bp = Blueprint("config", __name__)


# =========================
# Views
# =========================

@api_bp.route("/config")
def renderConfig():
    return render_template("config.html")


# =========================
# API
# =========================

@api_bp.route("/api/config", methods=["GET"])
def getConfig_route():
    return jsonify(getConfig())


@api_bp.route("/api/config", methods=["POST"])
def updateConfig_route():
    try:
        data = request.get_json()
        updateConfig(data)
        return jsonify({
            "status": "success",
            "config": getConfig()
        })
    except ConfigurationError as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": "Erreur interne"
        }), 500


@api_bp.route("/api/config/reset", methods=["POST"])
def resetConfig_route():
    resetConfig()
    return jsonify({
        "status": "success",
        "config": getConfig()
    })

@api_bp.route("/api/properties/version", methods=["GET"])
def getVersion_route():
    return VERSION