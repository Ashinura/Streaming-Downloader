import os
import colorama
import rich
import yt_dlp
from .YouTubeExtras import *



def yt_short():

    os.system('cls')

    import json

    script_dir = os.path.dirname(os.path.realpath(__file__))
    config_path = os.path.join(script_dir, '..', '..', 'Configuration', 'config.json')

    with open(config_path, 'r') as file:
        data = json.load(file)

    yt_short_path = data['youtube']['shorts']['path']
    yt_short_format = data['youtube']['shorts']['format']

    print(yt_short_path)


    logo(music=False, video=True, short=False)

    print(f"{colorama.Fore.RED}Path : {colorama.Fore.LIGHTRED_EX}{os.path.abspath(yt_short_path)}")
    print(f"{colorama.Fore.RED}Format : {colorama.Fore.LIGHTRED_EX}{yt_short_format}\n")

    rich.print("[green][[/green]" + "[bold white]0[/bold white]" + "[green]][/green]", "[cyan]Back to the main menu[/cyan]")
    rich.print("[green][[/green]" + "[bold white]9[/bold white]" + "[green]][/green]", "[cyan]Show/Edit configuration[/cyan]")

    choice = False

    while not choice:
             
        option_or_url = str(input(f"\n{colorama.Fore.LIGHTMAGENTA_EX}[{colorama.Fore.LIGHTWHITE_EX}~{colorama.Fore.LIGHTMAGENTA_EX}] {colorama.Fore.LIGHTWHITE_EX}Option or Short URL: "))

        if option_or_url[:5] == "https": 

            yt_short_path = data['youtube']['shorts']['path']
            yt_short_format = data['youtube']['shorts']['format']
            quietytdlp = data["user"]["quietytdlp"]

            try:
                ydl_opts = {
                    'format': f'bestvideo[ext={yt_short_format}]+bestaudio/best[ext={yt_short_format}]',
                    'quiet': eval(quietytdlp),             
                    'no_warnings': True,        
                    'outtmpl': f"{yt_short_path}/%(uploader)s - %(title)s.%(ext)s",     
                }
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([option_or_url])

            except yt_dlp.DownloadError:
                ydl_opts = {
                    'format': f'bv+ba/best',
                    'quiet': eval(quietytdlp),             
                    'no_warnings': True,        
                    'outtmpl': f"{yt_short_path}/%(uploader)s - %(title)s.%(ext)s",     
                }

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([option_or_url])

                print('') # Space
                if yt_short_format != "best": rich.print('[yellow]Your download could not be made in the desired format.[/yellow]')
                print('The download was made with the best parameters for the URL')


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