import os
import colorama
import rich
import subprocess
import json
import yt_dlp


def sc_menu(): 

    os.system('cls')

    from .SoundCloudExtra import logo


    logo()

    rich.print("[green][[/green]" + "[bold white]0[/bold white]" + "[green]][/green]", "[cyan]Back to the main menu[/cyan]")
    rich.print("[green][[/green]" + "[bold white]9[/bold white]" + "[green]][/green]", "[cyan]Show/Edit configuration[/cyan]\n")

    script_dir = os.path.dirname(os.path.realpath(__file__))
    config_path = os.path.join(script_dir, '..', '..', 'Configuration', 'config.json')

    with open(config_path, 'r') as file:
        data = json.load(file)

    sc_song_path = data['soundcloud']['song']['path']
    sc_song_format = data['soundcloud']['song']['format']

    sc_playlist_path = data['soundcloud']['playlist']['path']
    sc_playlist_format = data['soundcloud']['playlist']['format']

    sc_artist_path = data['soundcloud']['artist']['path']
    sc_artist_format = data['soundcloud']['artist']['format']

    quietytdlp = data["user"]["quietytdlp"]

    choice = False

    while not choice:

        option_or_url = str(input(f"\n{colorama.Fore.LIGHTMAGENTA_EX}[{colorama.Fore.LIGHTWHITE_EX}~{colorama.Fore.LIGHTMAGENTA_EX}] {colorama.Fore.LIGHTWHITE_EX}Option or URL: "))

        if option_or_url[:23] == "https://soundcloud.com/":

            url = option_or_url

            url_infos = {'extract_info': True, 'quiet': True}

            with yt_dlp.YoutubeDL(url_infos) as ydl:
                info = ydl.extract_info(url, download=False)
                
            if "entries" in info: 

                if "sets" or "playlist" in url:
                        
                        ydl_opts = {
                            'format': f'bestaudio[ext={sc_playlist_format}]',
                            'quiet': eval(quietytdlp),             
                            'no_warnings': True,        
                            'outtmpl': f"{sc_playlist_path}/%(uploader)s - %(title)s.%(ext)s",     
                        }

                        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                            ydl.extract_info(url)
                
                else:
                    ydl_opts = {
                        'format': f'bestaudio[ext={sc_artist_format}]',
                        'quiet': eval(quietytdlp),             
                        'no_warnings': True,        
                        'outtmpl': f"{sc_artist_path}/%(uploader)s - %(title)s.%(ext)s",     
                    }

                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        ydl.extract_info(url)


            else:
                ydl_opts = {
                    'format': f'bestaudio[ext={sc_song_format}]',
                    'quiet': eval(quietytdlp),             
                    'no_warnings': True,        
                    'outtmpl': f"{sc_song_path}/%(uploader)s - %(title)s.%(ext)s",     
                }

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.extract_info(url)


        else:
            try: 
                if eval(option_or_url) in [0, 1, 9]:
                    choice = True

                    if eval(option_or_url) == 0:
                        from StreamMenu import main_menu
                        main_menu()

                    elif eval(option_or_url) == 9: 
                        from Configuration.Soundcloud.SoundCloudConfig import sc_config_menu
                        sc_config_menu()

            except: 
                rich.print(
                    "[red][[/red]" + "[bold white]![/bold white]" + "[red]][/red]",
                    "[white]Invalid option or URL.[/white]"
                )