import uuid
import requests
import subprocess
from bs4 import BeautifulSoup
import yt_dlp
import rich
import json
import os

from pyfiglet import figlet_format
from termcolor import colored
from Platforms.siteProcess import StreamDL



def check_file(filename):
    # Truncate filename if its too long 
    max_length = 255
    name, ext = os.path.splitext(filename)
    max_name_length = max_length - len(ext)
    if len(name) > max_name_length:
        name = uuid.uuid4()
    filename = name + ext
    filename = filename.split('#')[0]
    return filename


def ytdlpProcess(request: StreamDL):

    logo = colored((figlet_format(f'{request.name.capitalize()}', font='small', width = 200)), f'{request.color}')
    os.system('cls')
    print(logo)

    with open('./Config/config.json', 'r') as data:
        config = json.load(data)
    quietYtdlp = config["user"]["quietytdlp"]

    try: 
        check_url = {"quiet": True, 'no_warnings': True, 'simulate': True,}
        ydl_check = yt_dlp.YoutubeDL(check_url)
        info = ydl_check.extract_info(request.url, download=False)

        if 'entries' in info:
            total_entries = len(info["entries"])
            rich.print(f"{total_entries} entries found in URL\n")
            for entry in info['entries']:
                ydl_opts = {
                    'format': f'bestvideo[ext={request.format}]+bestaudio/best[ext={request.format}]',
                    'quiet': quietYtdlp,             
                    'no_warnings': True,        
                    'outtmpl': f"{request.path}/%(uploader)s - %(title)s.%(ext)s",     
                }

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.extract_info(entry['webpage_url'])    

            rich.print(f"[green]Downloaded[/green]")
            input("Press 'Enter' to be back on menu")
            from StreamingDL import main_menu
            main_menu()
    
    
        else: 
            try:
                ydl_opts = {
                    'format': f'bestvideo[ext={request.format}]+bestaudio/best[ext={request.format}]',
                    'quiet': quietYtdlp,             
                    'no_warnings': True,        
                    'outtmpl': f"{request.path}/%(uploader)s - %(title)s.%(ext)s",     
                }

                # Exception # 
                if (request.name == "tiktok"): ydl_opts['outtmpl'] = f"{request.path}/%(uploader)s - {check_file(ydl_check.prepare_filename(info))}.{request.format}"
                if (request.name == "twitter"): ydl_opts['outtmpl'] = f"{request.path}/{(ydl_check.prepare_filename(info)).split('-')[0]}- {uuid.uuid4()}"   # path/uploader - uuid.format
                # --------- #

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([request.url])

                rich.print(f"\n[green]Downloaded[/green]")
                input("\nPress 'Enter' to be back on menu")
                from StreamingDL import main_menu
                main_menu()

            except yt_dlp.DownloadError:
                ytdlpDefault(request.url)

    except: 
        print(yt_dlp.DownloadError)



def scYtdlpProcess(request: StreamDL):
    
    logo = colored((figlet_format(f'{request.name.capitalize()}', font= 'small', width = 200)), f'{request.color}')
    os.system('cls')
    print(logo)

    try:
        check_url = {"quiet": True, 'no_warnings': True, 'simulate': True,}
        ydl_check = yt_dlp.YoutubeDL(check_url)
        info = ydl_check.extract_info(request.url, download=False)


        if 'entries' in info:

            total_tracks = len(info["entries"])
            rich.print(f"{total_tracks} tracks found in URL\n")
            
            for index, track in enumerate(info['entries'], start=1):
                try:
                    title = f"{track['uploader']} - {track['title']}"
                    final_filename = os.path.join(request.path, f"{title}.{request.format}")

                    # Skip on existing
                    if os.path.exists(final_filename):
                        rich.print(f"[cyan]Skipped (already exists)[/cyan]: {title} ({index}/{total_tracks})")
                        continue

                    ydl_opts = {
                        'quiet': True,
                        'format': 'bestaudio/best',
                        'postprocessors': [{
                            'key': 'FFmpegExtractAudio',
                            'preferredcodec': 'mp3',
                            'preferredquality': '192',
                        }],
                        'outtmpl': os.path.join(request.path, '%(title)s.%(ext)s'),
                    }

                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        track_info = ydl.extract_info(track['webpage_url'], download=True)
                        filename = ydl.prepare_filename(track_info)
                        filename = filename.rsplit(".", 1)[0] + f".{request.format}"                

                    cover_url = track_info.get('thumbnail')  
                    cover_request = requests.get(cover_url, allow_redirects=True)
                    temp_cover_filename = os.path.join(request.path, f"cover_{uuid.uuid4()}.jpg")

                    with open(temp_cover_filename, 'wb') as cover_file:
                        cover_file.write(cover_request.content)

                    with subprocess.Popen(f'ffmpeg -i "{filename}" -i "{temp_cover_filename}" -map 0:0 -map 1:0 -c copy -id3v2_version 3 -metadata:s:v title="Album cover" -metadata:s:v comment="Cover (front)" "{final_filename}" > NUL 2>&1', shell=True) as proc:
                        proc.wait()
                    
                    os.remove(temp_cover_filename)
                    os.remove(filename)
                    rich.print(f"[green]Downloaded[/green]: {title} ({index}/{total_tracks})")


                except requests.exceptions.RequestException as e:
                    print(f"Error downloading cover: {e}")
                except yt_dlp.DownloadError as e:
                    print(f"Error downloading video: {e}")

            rich.print("\n[green]Playlist downloaded[/green]")
            input("\nPress 'Enter' to be back on menu")
            from StreamingDL import main_menu
            main_menu()
    
    


        else:
            try:
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                    'outtmpl': os.path.join(request.path, '%(title)s.%(ext)s'),
                }

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(request.url, download=True)
                    filename = ydl.prepare_filename(info)
                    filename = filename.rsplit(".", 1)[0] + f".{request.format}"

                response = requests.get(request.url)
                soup = BeautifulSoup(response.text, 'html.parser')
                cover_url = soup.find("meta", property="og:image")["content"]
                cover_request = requests.get(cover_url, allow_redirects=True)

                temp_cover_filename = os.path.join(request.path, f"cover_{uuid.uuid4()}.jpg")

                with open(temp_cover_filename, 'wb') as cover_file:
                    cover_file.write(cover_request.content)

                title = f"{info['uploader']} - {info['title']}"
                final_filename = os.path.join(request.path, f"{title}.{request.format}")

                with subprocess.Popen(f'ffmpeg -i "{filename}" -i "{temp_cover_filename}" -map 0:0 -map 1:0 -c copy -id3v2_version 3 -metadata:s:v title="Album cover" -metadata:s:v comment="Cover (front)" "{final_filename}" > NUL 2>&1', shell=True) as proc:
                    proc.wait()

                os.remove(temp_cover_filename)
                os.remove(filename)

                rich.print("\n[green]Downloaded[/green]")
                input("\nPress 'Enter' to be back on menu")
                from StreamingDL import main_menu
                main_menu()
    

            except requests.exceptions.RequestException as e:
                print(f"Error downloading cover: {e}")
            except yt_dlp.DownloadError as e:
                print(f"Error downloading video: {e}")
            except Exception as e:
                print(f"An error occurred: {e}")

    except yt_dlp.DownloadError:
        ytdlpDefault(request.url)




def ytdlpDefault(request: StreamDL):

    logo = colored((figlet_format(f'{request.name.capitalize()}', font= 'small', width = 200)), f'{request.color}')
    os.system('cls')
    print(logo)
    
    ydl_opts = {
        'format': f'bv+ba/best',
        'quiet': False,             
        'no_warnings': False,        
        'outtmpl': f"./DL/file - {uuid.uuid4()}.%(ext)s",     
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([request.url])
        
    rich.print("\n[green]Downloaded[/green]")
    print('The download was made with the best parameters for the URL')
    input("\nPress 'Enter' to be back on menu")
    from StreamingDL import main_menu
    main_menu()