import os
import sys
from properties import getConfig

remote_version = None

def main():
    global remote_version
    config = getConfig()
    flaskSettings = config.get("flask", {})
    userSettings = config.get("user", {})
    
    is_debug = flaskSettings.get("debug", False)
    
    print("[INFO] - Vérification des mises à jour")
    if userSettings.get("autoupdate", False) and not is_debug:
        try:
            from utils.updater import updateProject
            if updateProject():
                print("[INFO] - Mise à jour installée. Redémarrage...")
                os.execv(sys.executable, [sys.executable] + sys.argv)
        except Exception as error:
            print(f"[ERROR] - Erreur MAJ : {error}")
    elif is_debug:
        if os.environ.get('WERKZEUG_RUN_MAIN') != 'true':
                print("[INFO] - Mode Debug actif : Mise à jour automatique désactivée")
    else: 
        from utils.updater import checkRemoteVersion
        remote_version = checkRemoteVersion()
        if remote_version:
            print(f"[UPDATE] - Nouvelle version détectée | { remote_version }")



    try:
        from app import app

        app.config['REMOTE_VERSION'] = remote_version
        
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