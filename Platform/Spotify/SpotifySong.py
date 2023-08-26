import colorama
import subprocess
import json
import rich
import os 


def sp_song(): 

    script_dir = os.path.dirname(os.path.realpath(__file__))
    config_path = os.path.join(script_dir, '..', '..', 'Configuration', 'config.json')

    with open(config_path, 'r') as file:
        data = json.load(file)

    sp_song_path = data['spotify']['song']['path']
    sp_song_format = data['spotify']['song']['format']

    while True:

        song_url = str(input(f"\n{colorama.Fore.LIGHTMAGENTA_EX}[{colorama.Fore.LIGHTWHITE_EX}~{colorama.Fore.LIGHTMAGENTA_EX}] {colorama.Fore.LIGHTWHITE_EX}Song URL: "))

        if song_url[:5] == "https": 
            try:
                subprocess.run(["spotdl", song_url, "--output", sp_song_path, "--format", sp_song_format])

            except Exception as e:
                print(f"\n{colorama.Fore.LIGHTRED_EX}The song didn't download  \n{colorama.Fore.LIGHTYELLOW_EX}Try another URL \n{colorama.Fore.LIGHTMAGENTA_EX}Error : {e}    ")

        else:
            rich.print('[red]Invalid URL.[/red]')