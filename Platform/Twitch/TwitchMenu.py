import os
import colorama
import rich
import yt_dlp
from .TwitchExtra import *



def tw_menu():

    os.system('cls')

    import json

    script_dir = os.path.dirname(os.path.realpath(__file__))
    config_path = os.path.join(script_dir, '..', '..', 'Configuration', 'config.json')

    with open(config_path, 'r') as file:
        data = json.load(file)

    tw_redif_path = data['twitch']['redif']['path']
    tw_redif_format = data['twitch']['redif']['format']


    logo()

    rich.print(f"[purple]Path : {os.path.abspath(tw_redif_path)}[/purple]")
    rich.print(f"[purple]Format : {tw_redif_format}\n[/purple]")

    rich.print("[green][[/green]" + "[bold white]0[/bold white]" + "[green]][/green]", "[cyan]Back to the main menu[/cyan]")
    rich.print("[green][[/green]" + "[bold white]9[/bold white]" + "[green]][/green]", "[cyan]Show/Edit configuration[/cyan]\n")

    choice = False

    while not choice:
             
        option_or_url = str(input(f"\n{colorama.Fore.LIGHTMAGENTA_EX}[{colorama.Fore.LIGHTWHITE_EX}~{colorama.Fore.LIGHTMAGENTA_EX}] {colorama.Fore.LIGHTWHITE_EX}Option or redif URL: "))

        if option_or_url[:22] == "https://www.twitch.tv/": 

            tw_redif_path = data['twitch']['redif']['path']
            tw_redif_format = data['twitch']['redif']['format']
            quietytdlp = data["user"]["quietytdlp"]

            try:
                ydl_opts = {
                    'format': f'bestvideo[ext={tw_redif_format}]+bestaudio/best[ext={tw_redif_format}]',
                    'quiet': eval(quietytdlp),             
                    'no_warnings': True,        
                    'outtmpl': f"{tw_redif_path}/%(uploader)s - %(title)s.%(ext)s",     
                }
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([option_or_url])

            except yt_dlp.DownloadError:
                ydl_opts = {
                    'format': f'bv+ba/best',
                    'quiet': eval(quietytdlp),             
                    'no_warnings': True,        
                    'outtmpl': f"{tw_redif_path}/%(uploader)s - %(title)s.%(ext)s",     
                }

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([option_or_url])

                print('') # Space
                if tw_redif_format != "best": rich.print('[yellow]Your download could not be made in the desired format.[/yellow]')
                print('The download was made with the best parameters for the URL')


        else:
            try: 
                if eval(option_or_url) in [0, 1, 9]:
                    choice = True

                    if eval(option_or_url) == 0:
                        from StreamMenu import main_menu
                        main_menu()

                    elif eval(option_or_url) == 9: 
                        from Configuration.Twitch.TwitchConfig import tw_config_menu
                        tw_config_menu()

            except: 
                rich.print(
                    "[red][[/red]" + "[bold white]![/bold white]" + "[red]][/red]",
                    "[white]Invalid option or URL.[/white]"
                )