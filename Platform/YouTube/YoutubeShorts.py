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

    print(f"{colorama.Fore.LIGHTRED_EX}Path : {colorama.Fore.RED}{os.path.abspath(yt_short_path)}")
    print(f"{colorama.Fore.LIGHTRED_EX}Format : {colorama.Fore.RED}{yt_short_format}\n")

    rich.print("[green][[/green]" + "[bold white]0[/bold white]" + "[green]][/green]", "[cyan]Back to the main menu[/cyan]")
    rich.print("[green][[/green]" + "[bold white]9[/bold white]" + "[green]][/green]", "[cyan]Show/Edit configuration[/cyan]")

    rich.print(
        "\n\n[yellow][[/yellow]" + "[bold white]1[/bold white]" + "[yellow]][/yellow]", "[white]Download Short[/white]\n"
    )   


    choice = False

    while not choice:
        try:   
            option = int(input(f"\n{colorama.Fore.LIGHTMAGENTA_EX}[{colorama.Fore.LIGHTWHITE_EX}~{colorama.Fore.LIGHTMAGENTA_EX}] {colorama.Fore.LIGHTWHITE_EX}Chose an option : "))

            if option in [0, 1, 9]:
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
        yt_short_download(data)
        
    elif option == 9: 
        from Configuration.Youtube.YouTubeConfig import yt_config_menu
        yt_config_menu()



def yt_short_download(data): 

    yt_short_path = data['youtube']['shorts']['path']
    yt_short_format = data['youtube']['shorts']['format']

    while True:

        short_url = str(input(f"\n{colorama.Fore.LIGHTMAGENTA_EX}[{colorama.Fore.LIGHTWHITE_EX}~{colorama.Fore.LIGHTMAGENTA_EX}] {colorama.Fore.LIGHTWHITE_EX}Short URL : "))

        try:
            ydl_opts = {
                'format': f'bestvideo[ext={yt_short_format}]+bestaudio/best[ext={yt_short_format}]',
                'quiet': False,             
                'no_warnings': True,        
                'outtmpl': f"{yt_short_path}/%(title)s.%(ext)s",     
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([short_url])

        except Exception:
            try:
                ydl_opts = {
                    'format': f'ba+bv/best',
                    'quiet': False,             
                    'no_warnings': True,        
                    'outtmpl': f"{yt_short_path}/%(uploader)s - %(title)s.%(ext)s",     
                }

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([short_url])

            except Exception as err:
                print(err)