# routes/api.py
from os import path, _exit
from threading import Thread
from subprocess import Popen, CREATE_NEW_PROCESS_GROUP, DETACHED_PROCESS
from time import sleep
from flask import Blueprint, jsonify, request
from core.properties import ROOT_DIR, VERSION, DEFAULT_CONFIG, getConfig, updateConfig, ConfigurationError

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
        print(f"[ERROR] - Erreur interne API: {e}")
        return jsonify({"status": "error", "message": "Erreur interne du serveur"}), 500

@api_bp.route("/config/default", methods=["GET"])
def defaultConfig_route():
    return jsonify(DEFAULT_CONFIG)

@api_bp.route("/properties/version", methods=["GET"])
def getVersion_route():
    return jsonify(VERSION)

@api_bp.route("/update-project", methods=["POST"])
def trigger_update():
    from utils.update.updater import updateProject
    try:
        if not updateProject():
            return jsonify({"status": "failed", "message": "Échec de l'installation"}), 500

        def restart():
            sleep(2)
            restart_script = path.join(ROOT_DIR, "utils", "update", "restart.vbs")
            Popen(
                ["wscript", restart_script],
                creationflags=CREATE_NEW_PROCESS_GROUP | DETACHED_PROCESS
            )
            _exit(0) # Tuer le processus actuel

        Thread(target=restart, daemon=True).start()
        return jsonify({"status": "success"}), 200

    except Exception as e:
        print(f"[ERROR] - Erreur API Update : {e}")
        return jsonify({"status": "error", "message": str(e)}), 500