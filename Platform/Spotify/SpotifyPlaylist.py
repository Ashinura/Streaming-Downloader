import colorama
import subprocess
import os 
import json

def sp_playlist(): 

    script_dir = os.path.dirname(os.path.realpath(__file__))
    config_path = os.path.join(script_dir, '..', '..', 'Configuration', 'config.json')

    with open(config_path, 'r') as file:
        data = json.load(file)

    sp_playlist_path = data['spotify']['playlist']['path']
    sp_playlist_format = data['spotify']['playlist']['format']

    while True:

        playlist_url = str(input(f"\n{colorama.Fore.LIGHTMAGENTA_EX}[{colorama.Fore.LIGHTWHITE_EX}~{colorama.Fore.LIGHTMAGENTA_EX}] {colorama.Fore.LIGHTWHITE_EX}Playlist URL: "))

        try:
            subprocess.run(["spotdl", playlist_url, "--output", sp_playlist_path, "--format", sp_playlist_format])

        except Exception as e:
            print(f"\n{colorama.Fore.LIGHTRED_EX}The playlist didn't download  \n{colorama.Fore.LIGHTYELLOW_EX}Try another URL \n{colorama.Fore.LIGHTMAGENTA_EX}Error : {e}    ")