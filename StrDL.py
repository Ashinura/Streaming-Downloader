import os
import sys
from core.properties import getConfig

remote_version = None

def main():
    global remote_version
    config = getConfig()
    flaskSettings = config.get("flask", {})
    userSettings = config.get("user", {})
    
    is_debug = flaskSettings.get("debug", False)

    if is_debug:
        if os.environ.get('WERKZEUG_RUN_MAIN') != 'true':
                print("[DEBUG] - Mise à jour automatique désactivée")
    else:
        print("[DEBUG] - OFF")
        print("[INFO] - Vérification des mises à jour")
    
    if userSettings.get("autoupdate", False) and not is_debug:
        try:
            from utils.update.updater import updateProject
            if updateProject():
                print("[INFO] - Mise à jour installée. Redémarrage...")
                os.execv(sys.executable, [sys.executable] + sys.argv)
        except Exception as error:
            print(f"[ERROR] - Erreur MAJ : {error}")
    else: 
        from utils.update.updater import checkRemoteVersion
        remote_version = checkRemoteVersion()
        if remote_version:
            print(f"[UPDATE] - Nouvelle version détectée | { remote_version }")


    try:
        from core.app import app

        app.config['REMOTE_VERSION'] = remote_version
        
        if is_debug:
            print(f"[DEBUG] - app.config REMOTE_VERSION = {app.config.get('REMOTE_VERSION')}")
        
        host_ip = flaskSettings.get("ip", "127.0.0.1")
        port_number = flaskSettings.get("port", 5000)

        app.run(
            host=host_ip,
            port=port_number,
            debug=is_debug 
        )

    except Exception as error:
        print(f"[ERROR] - Erreur fatale lors du lancement : {error}")
        input("Appuyez sur Entrée pour quitter...")

if __name__ == "__main__":
    main()