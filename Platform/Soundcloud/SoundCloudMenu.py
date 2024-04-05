import os
import colorama
import rich
import json
import yt_dlp
import requests
import send2trash
import uuid
from bs4 import BeautifulSoup
from .SoundCloudExtra import *



def sc_menu(): 

    os.system('cls')

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

    quietytdlp = data["user"]["quietytdlp"]
    download_in_progress_path = "./Platform/Soundcloud/InProgress"

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
                    for entry in info['entries']:

                        response = requests.get(entry['thumbnail'])
                        temp_cover_filename = f"{download_in_progress_path}/cover_{uuid.uuid4()}.jpg"

                        with open(f'{temp_cover_filename}', 'wb') as cover_file:
                            cover_file.write(response.content)
                            
                        filename_template = f"{download_in_progress_path}/%(title)s.%(ext)s"
                        filename = filename_template % {'title': clean_title(entry['title']), 'ext': sc_playlist_format}

                        ydl_opts = {
                            'quiet': quietytdlp,
                            'no_warnings': True,
                            'outtmpl': filename,
                            'format': 'bestaudio/best', 
                        }

                        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                          ydl.extract_info(entry['webpage_url'])

                        final_filename = f"{sc_playlist_path}/{entry['uploader']} - {clean_title(entry['title'])}.{sc_playlist_format}"
                        os.system(f'ffmpeg -loglevel 0 -i "{filename}" -i "{temp_cover_filename}" -map 0 -map 1 -c copy -id3v2_version 3 -metadata:s:v title="Album cover" -metadata:s:v comment="Cover (front)" "{final_filename}"')

                        send2trash.send2trash(temp_cover_filename)
                        send2trash.send2trash(filename)


            else:
                
                response = requests.get(url)
                soup = BeautifulSoup(response.text, 'html.parser')
                cover_url = soup.find("meta", property="og:image")["content"]
                cover_request = requests.get(cover_url, allow_redirects=True)
        
                temp_cover_filename = f"{download_in_progress_path}/cover_{uuid.uuid4()}.jpg"
        
                with open(temp_cover_filename, 'wb') as cover_file:
                  cover_file.write(cover_request.content)
        
                filename_template = f"{download_in_progress_path}/%(title)s.%(ext)s"
                filename = filename_template % {'title': clean_title(info['title']), 'ext': sc_song_format}
        
                ydl_opts = {
                    'quiet': quietytdlp,
                    'no_warnings': True,
                    'outtmpl': filename,
                    'format': 'bestaudio/best', 
                }
        
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                  ydl.extract_info(url)
        
                final_filename = f"{sc_song_path}/{info['uploader']} - {clean_title(info['title'])}.{sc_song_format}"
                os.system(f'ffmpeg -loglevel 0 -i "{filename}" -i "{temp_cover_filename}" -map 0 -map 1 -c copy -id3v2_version 3 -metadata:s:v title="Album cover" -metadata:s:v comment="Cover (front)" "{final_filename}"')

                send2trash.send2trash(temp_cover_filename)
                send2trash.send2trash(filename)


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