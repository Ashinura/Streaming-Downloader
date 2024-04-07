import os
import colorama
import rich
import subprocess
import json


def sp_menu(): 

    os.system('cls')

    from .SpotifyExtras import logo
    logo()

    rich.print("[green][[/green]" + "[bold white]0[/bold white]" + "[green]][/green]", "[cyan]Back to the main menu[/cyan]")
    rich.print("[green][[/green]" + "[bold white]9[/bold white]" + "[green]][/green]", "[cyan]Show/Edit configuration[/cyan]\n")

    script_dir = os.path.dirname(os.path.realpath(__file__))
    config_path = os.path.join(script_dir, '..', '..', 'Configuration', 'config.json')

    with open(config_path, 'r') as file:
        data = json.load(file)

    sp_song_path = data['spotify']['song']['path']
    sp_song_format = data['spotify']['song']['format']

    sp_playlist_path = data['spotify']['playlist']['path']
    sp_playlist_format = data['spotify']['playlist']['format']

    sp_artist_path = data['spotify']['artist']['path']
    sp_artist_format = data['spotify']['artist']['format']

    choice = False

    while not choice:

        option_or_url = str(input(f"\n{colorama.Fore.LIGHTMAGENTA_EX}[{colorama.Fore.LIGHTWHITE_EX}~{colorama.Fore.LIGHTMAGENTA_EX}] {colorama.Fore.LIGHTWHITE_EX}Option or URL: "))

        if option_or_url[:25] == "https://open.spotify.com/":

            url = option_or_url

            if "track" in url: 
                try:
                    subprocess.run(["spotdl", option_or_url, "--output", sp_song_path, "--format", sp_song_format])

                except Exception as e:
                    print(f"\n{colorama.Fore.LIGHTRED_EX}The song didn't download  \n{colorama.Fore.LIGHTYELLOW_EX}Try another URL \n{colorama.Fore.LIGHTMAGENTA_EX}Error : {e}    ")

            elif "playlist" or "album" in url: 
                try:
                    subprocess.run(["spotdl", url, "--output", sp_playlist_path, "--format", sp_playlist_format])

                except Exception as e:
                    print(f"\n{colorama.Fore.LIGHTRED_EX}The song didn't download  \n{colorama.Fore.LIGHTYELLOW_EX}Try another URL \n{colorama.Fore.LIGHTMAGENTA_EX}Error : {e}    ")


            elif "artist" in url: 
                try:
                    subprocess.run(["spotdl", url, "--output", sp_artist_path, "--format", sp_artist_format])

                except Exception as e:
                    print(f"\n{colorama.Fore.LIGHTRED_EX}The song didn't download  \n{colorama.Fore.LIGHTYELLOW_EX}Try another URL \n{colorama.Fore.LIGHTMAGENTA_EX}Error : {e}    ")

            else:
                rich.print('[red]Invalid URL.[/red]')


        else:
            try: 
                if eval(option_or_url) in [0, 1, 9]:
                    choice = True

                    if eval(option_or_url) == 0:
                        from StreamMenu import main_menu
                        main_menu()

                    elif eval(option_or_url) == 9: 
                        from Configuration.Youtube.YouTubeConfig import yt_config_menu
                        yt_config_menu()

            except: 
                rich.print(
                    "[red][[/red]" + "[bold white]![/bold white]" + "[red]][/red]",
                    "[white]Invalid option or URL.[/white]"
                )