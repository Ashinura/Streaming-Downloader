import os
import colorama
import rich
import yt_dlp
from .YouTubeExtras import *



def yt_music():

    os.system('cls')

    import json

    script_dir = os.path.dirname(os.path.realpath(__file__))
    config_path = os.path.join(script_dir, '..', '..', 'Configuration', 'config.json')

    with open(config_path, 'r') as file:
        data = json.load(file)

    yt_music_path = data['youtube']['musics']['path']
    yt_music_format = data['youtube']['musics']['format']


    logo(music=True, video=False, short=False)

    print(f"{colorama.Fore.LIGHTRED_EX}Path : {colorama.Fore.RED}{os.path.abspath(yt_music_path)}")
    print(f"{colorama.Fore.LIGHTRED_EX}Format : {colorama.Fore.RED}{yt_music_format}\n")

    rich.print("[green][[/green]" + "[bold white]0[/bold white]" + "[green]][/green]", "[cyan]Back to the main menu[/cyan]")
    rich.print("[green][[/green]" + "[bold white]9[/bold white]" + "[green]][/green]", "[cyan]Show/Edit configuration[/cyan]")

    rich.print(
        "\n\n[yellow][[/yellow]" + "[bold white]1[/bold white]" + "[yellow]][/yellow]", "[white]Individually[/white]", "            ",
        "[yellow][[/yellow]" + "[bold white]2[/bold white]" + "[yellow]][/yellow]", "[white]Playlist[/white]\n"
    )   


    choice = False

    while not choice:
        try:   
            option = int(input(f"\n{colorama.Fore.LIGHTMAGENTA_EX}[{colorama.Fore.LIGHTWHITE_EX}~{colorama.Fore.LIGHTMAGENTA_EX}] {colorama.Fore.LIGHTWHITE_EX}Chose an option : "))

            if option in [0, 1, 2, 9]:
                choice = True 

            else:
                rich.print(
                    "[red][[/red]" + "[bold white]![/bold white]" + "[red]][/red]",
                    "[white]Invalid option selected, doesn't exist.[/white]"
                )

        except ValueError:
            rich.print(
                "[red][[/red]" + "[bold white]![/bold white]" + "[red]][/red]",
                "[white]Invalid option selected, must be int.[/white]"
            )

    if option == 0:
        from StreamMenu import main_menu
        main_menu()
        
    elif option == 1:
        yt_music_individually(data)

    elif option == 2:
        yt_music_playlist(data)

    elif option == 9: 
        from Configuration.Youtube.YouTubeConfig import yt_config_menu
        yt_config_menu()



def yt_music_individually(data): 

    yt_music_path = data['youtube']['musics']['path']
    yt_music_format = data['youtube']['musics']['format']

    while True:

        try:

            music_url = str(input(f"\n{colorama.Fore.LIGHTMAGENTA_EX}[{colorama.Fore.LIGHTWHITE_EX}~{colorama.Fore.LIGHTMAGENTA_EX}] {colorama.Fore.LIGHTWHITE_EX}music URL : "))

            check_url = {"quiet": True, 'no_warnings': True, 'simulate': True,}
            ydl_check = yt_dlp.YoutubeDL(check_url)
            info = ydl_check.extract_info(music_url, download=False)

            if 'entries' in info:
                choice_continue = str(input("The URL is a playlist, continue ? [y/n] : "))

                if choice_continue in ["y", "yes"]:

                    ydl_opts = {
                        'format': f'bestaudio[ext={yt_music_format}]',
                        'quiet': False,             
                        'no_warnings': True,        
                        'outtmpl': f"{yt_music_path}/%(uploader)s - %(title)s.%(ext)s",     
                    }

                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([music_url])

                else:
                    yt_music()
            
            else:
                ydl_opts = {
                    'format': f'bestaudio[ext={yt_music_format}]',
                    'quiet': False,             
                    'no_warnings': True,        
                    'outtmpl': f"{yt_music_path}/%(uploader)s - %(title)s.%(ext)s",     
                }

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([music_url])

        except Exception:
            try:
                ydl_opts = {
                    'format': f'ba',
                    'quiet': False,             
                    'no_warnings': True,        
                    'outtmpl': f"{yt_music_path}/%(uploader)s - %(title)s.%(ext)s",     
                }

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([music_url])

            except Exception as err:
                print(err)



def yt_music_playlist(data):

    yt_music_path = data['youtube']['musics']['path']
    yt_music_format = data['youtube']['musics']['format']

    while True:

        try:

            playlist_url = str(input(f"\n{colorama.Fore.LIGHTMAGENTA_EX}[{colorama.Fore.LIGHTWHITE_EX}~{colorama.Fore.LIGHTMAGENTA_EX}] {colorama.Fore.LIGHTWHITE_EX}playlist URL : "))

            check_url = {"quiet": True, 'no_warnings': True, 'simulate': True,}
            ydl_check = yt_dlp.YoutubeDL(check_url)
            info = ydl_check.extract_info(playlist_url, download=False)

            if 'entries' not in info:
                choice_continue = str(input("The URL isn't a playlist, continue ? [y/n] : "))

                if choice_continue in ["y", "yes"]:

                    ydl_opts = {
                        'format': f'bestaudio[ext={yt_music_format}]',
                        'quiet': False,             
                        'no_warnings': True,        
                        'outtmpl': f"{yt_music_path}/%(uploader)s - %(title)s.%(ext)s",     
                    }

                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([playlist_url])

                else:
                    yt_music()
            
            else:
                ydl_opts = {
                    'format': f'bestaudio[ext={yt_music_format}]',
                    'quiet': False,             
                    'no_warnings': True,        
                    'outtmpl': f"{yt_music_path}/%(uploader)s - %(title)s.%(ext)s",     
                }

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([playlist_url])

        except Exception:
            try:
                ydl_opts = {
                    'format': f'ba',
                    'quiet': False,             
                    'no_warnings': True,        
                    'outtmpl': f"{yt_music_path}/%(uploader)s - %(title)s.%(ext)s",     
                }

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([playlist_url])

            except Exception as err:
                print(err)