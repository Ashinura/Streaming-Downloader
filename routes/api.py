# routes/api.py

from flask import Blueprint, jsonify, request
from properties import VERSION, DEFAULT_CONFIG, getConfig, updateConfig, ConfigurationError

api_bp = Blueprint("api", __name__)

@api_bp.route("/config", methods=["GET"])
def getConfig_route():
    return jsonify(getConfig())

@api_bp.route("/config", methods=["POST"])
def updateConfig_route():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"status": "error", "message": "Aucune donnée reçue"}), 400
            
        updateConfig(data)
        
        return jsonify({
            "status": "success",
            "config": getConfig()
        })
    except ConfigurationError as e:
        return jsonify({"status": "error", "message": str(e)}), 400
    except Exception as e:
        print(f"Erreur interne API: {e}")
        return jsonify({"status": "error", "message": "Erreur interne du serveur"}), 500

@api_bp.route("/config/default", methods=["GET"])
def defaultConfig_route():
    return jsonify(DEFAULT_CONFIG)

@api_bp.route("/properties/version", methods=["GET"])
def getVersion_route():
    # On renvoie directement la string ou un petit objet
    return jsonify(VERSION)