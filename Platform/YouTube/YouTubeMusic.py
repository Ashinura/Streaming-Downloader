import os
import colorama
import rich
from pytube import YouTube
from pytube import Playlist
from .YouTubeExtras import *

colorama.init()

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



def clean_filename(filename):
    import re
    # Remove characters that might cause issues in file names
    cleaned_filename = re.sub(r'[<>:"/\\|?*]', '', filename)
    return cleaned_filename



def yt_music_individually(data): 

    yt_music_path = data['youtube']['musics']['path']
    yt_music_format = data['youtube']['musics']['format']

    while True:

        music_url = str(input(f"\n{colorama.Fore.LIGHTMAGENTA_EX}[{colorama.Fore.LIGHTWHITE_EX}~{colorama.Fore.LIGHTMAGENTA_EX}] {colorama.Fore.LIGHTWHITE_EX}Music URL: "))

        try:
            yt = YouTube(music_url)
            video = yt.streams.filter(only_audio=True).first()

            if '-' in yt.title:
                new_file = yt.title + yt_music_format
                new_file = clean_filename(new_file)
            else:
                new_file = yt.author + ' - ' + yt.title + yt_music_format
                new_file = clean_filename(new_file)

            if os.path.exists(os.path.join(yt_music_path, new_file)):
                print(f'{colorama.Fore.LIGHTYELLOW_EX}' + new_file + ' is already downloaded in the folder')

            else:
                yt.register_on_progress_callback(lambda stream, chunk, bytes_remaining: show_progress(stream, chunk, bytes_remaining, new_file))
                out_file = video.download(output_path=yt_music_path, filename=new_file)
                os.rename(out_file, os.path.join(yt_music_path, new_file))

        except Exception as e:
            print(f"\n{colorama.Fore.LIGHTRED_EX}The music didn't download  \n{colorama.Fore.LIGHTYELLOW_EX}Try another URL \n{colorama.Fore.LIGHTMAGENTA_EX}Error : {e}    ")



def yt_music_playlist(data):

    yt_music_path = data['youtube']['musics']['path']
    yt_music_format = data['youtube']['musics']['format']

    while True:

        playlist_url = str(input(f"\n{colorama.Fore.LIGHTMAGENTA_EX}[{colorama.Fore.LIGHTWHITE_EX}~{colorama.Fore.LIGHTMAGENTA_EX}] {colorama.Fore.LIGHTWHITE_EX}Playlist URL : "))

        try:
            playlist = Playlist(playlist_url)
            if not playlist:
                raise ValueError("Playlist not found or private.")
            
            for video in playlist.videos:
                try:

                    title = video.title
                    author = video.author

                    video_stream = video.streams.filter(only_audio=True).first()

                    if '-' in title:
                        new_file = title + yt_music_format
                        new_file = clean_filename(new_file)
                    else:
                        new_file = author + ' - ' + title + yt_music_format
                        new_file = clean_filename(new_file)
                    


                    if os.path.exists(os.path.join(yt_music_path, new_file)):
                        print(f'{colorama.Fore.LIGHTYELLOW_EX}' + new_file + ' is already downloaded in the folder')
        
                    else:
                        video.register_on_progress_callback(lambda stream, chunk, bytes_remaining: show_progress(stream, chunk, bytes_remaining, new_file))
                        out_file = video_stream.download(output_path=yt_music_path, filename=new_file)
                        os.rename(out_file, os.path.join(yt_music_path, new_file))

                except Exception as err:
                    print(f"{colorama.Fore.LIGHTMAGENTA_EX}Error : {err}")

        except Exception as err:
            print(f"\n{colorama.Fore.LIGHTRED_EX}The playlist couldn't be accessed or is private. \n{colorama.Fore.LIGHTYELLOW_EX}Try another URL \n{colorama.Fore.LIGHTMAGENTA_EX}Error : {err}")
