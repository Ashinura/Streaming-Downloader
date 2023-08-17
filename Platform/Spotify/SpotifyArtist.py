import colorama
import subprocess
import os 
import json

def sp_artist(): 

    script_dir = os.path.dirname(os.path.realpath(__file__))
    config_path = os.path.join(script_dir, '..', '..', 'Configuration', 'config.json')

    with open(config_path, 'r') as file:
        data = json.load(file)

    sp_artist_path = data['spotify']['artist']['path']
    sp_artist_format = data['spotify']['artist']['format']

    while True:

        artist_url = str(input(f"\n{colorama.Fore.LIGHTMAGENTA_EX}[{colorama.Fore.LIGHTWHITE_EX}~{colorama.Fore.LIGHTMAGENTA_EX}] {colorama.Fore.LIGHTWHITE_EX}artist URL: "))

        try:
            subprocess.run(["spotdl", artist_url, "--output", sp_artist_path, "--format", sp_artist_format])

        except Exception as e:
            print(f"\n{colorama.Fore.LIGHTRED_EX}The artist didn't download  \n{colorama.Fore.LIGHTYELLOW_EX}Try another URL \n{colorama.Fore.LIGHTMAGENTA_EX}Error : {e}    ")