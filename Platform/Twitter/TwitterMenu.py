import os
import colorama
import rich
import subprocess
import json
from .TwitterExtra import *


def tx_menu():

    os.system('cls')

    script_dir = os.path.dirname(os.path.realpath(__file__))
    config_path = os.path.join(script_dir, '..', '..', 'Configuration', 'config.json')
    
    with open(config_path, 'r') as file:
        data = json.load(file)
    
    tx_video_path = data['twitter']['videos']['path']
    tx_video_format = data['twitter']['videos']['format']
    tx_video_cookie = data['twitter']['videos']['cookie-browser']
    tx_video_browsers_avaible = data['twitter']['valid_cookie_browser']

    if (tx_video_cookie != "undefined"): 

        logo()

        print(f"Path : {os.path.abspath(tx_video_path)}")
        print(f"Format : {tx_video_format}")
        print(f"Cookie from : {tx_video_cookie}\n")

        print(colorama.Fore.RESET)

        rich.print("[green][[/green]" + "[bold white]0[/bold white]" + "[green]][/green]", "[cyan]Back to the main menu[/cyan]")
        rich.print("[green][[/green]" + "[bold white]9[/bold white]" + "[green]][/green]", "[cyan]Show/Edit configuration[/cyan]\n")

        choice = False

        while not choice:

            option_or_url = str(input(f"\n{colorama.Fore.LIGHTMAGENTA_EX}[{colorama.Fore.LIGHTWHITE_EX}~{colorama.Fore.LIGHTMAGENTA_EX}] {colorama.Fore.LIGHTWHITE_EX}Option or URL: "))

            if option_or_url[:20] == "https://twitter.com/": 

                url = option_or_url

                tx_video_path = data['twitter']['videos']['path']
                tx_video_format = data['twitter']['videos']['format']
                tx_video_cookie = data['twitter']['videos']['cookie-browser']

                if (not os.path.isabs(tx_video_path)):
                    tx_video_path = os.getcwd() + "\Downloaded"
                    print("The provided path isn't absolute, your video will download in : ", tx_video_path)

                filename = "/%(title)s.%(ext)s"
                tx_video_path = tx_video_path + clean_title(filename)
                
                try:
                    subprocess.run(["yt-dlp", "-f", tx_video_format, "-o", tx_video_path, "--cookies-from-browser", tx_video_cookie, url])

                except Exception as e:
                    print(f"\n{colorama.Fore.LIGHTRED_EX}The video didn't download  \n{colorama.Fore.LIGHTYELLOW_EX}Try another URL \n{colorama.Fore.LIGHTMAGENTA_EX}Error : {e}    ")

            else:
                try: 
                    if eval(option_or_url) in [0, 1, 9]:
                        choice = True

                        if eval(option_or_url) == 0:
                            from StreamMenu import main_menu
                            main_menu()

                        elif eval(option_or_url) == 9: 
                            from Configuration.Twitter.TwitterConfig import tx_config_menu
                            tx_config_menu()

                except: 
                    rich.print(
                        "[red][[/red]" + "[bold white]![/bold white]" + "[red]][/red]",
                        "[white]Invalid option or URL.[/white]"
                    )


    else:

        from .TwitterExtra import logo
        logo()

        print("To download something via twitter/X, you need to provide the browser to extract the cookie from.")
        print("Streaming-Downloader do not save or retrace your personnal data, it is just like this to work with the current libraries (yt-dlp) and twiiter's policy.")
        print("When it's done, this message will no longer appear but you can always change the browser from the configuration page.")

        print(colorama.Fore.RESET)

        print("\nFormats available :", tx_video_browsers_avaible) 
        browser = str(input(f"{colorama.Fore.LIGHTMAGENTA_EX}[{colorama.Fore.LIGHTWHITE_EX}~{colorama.Fore.LIGHTMAGENTA_EX}] {colorama.Fore.LIGHTWHITE_EX}New format : "))

        platform = 'twitter'
        key = 'videos'
        value = {
            'path': tx_video_path,
            "format": tx_video_format,
            "cookie-browser": browser
        }

        with open(config_path, 'r') as file:
            data = json.load(file)

        data[platform][key] = value

        from time import sleep 

        if (browser not in tx_video_browsers_avaible):
            rich.print("[yellow]Please note that the browser is not in the list of valid browsers validated by the 'yt-dlp' librairie. You must choose one from the list to be able to download via twitter, otherwise an error will occur and no download will be done.[/yellow]")
            rich.print(f"List : [magenta]{tx_video_browsers_avaible}[/magenta]")
            sleep(6)
            rich.print("[red]Failed[/red]")
            sleep(2)
            tx_menu()

        elif (browser == tx_video_browsers_avaible):
            rich.print("[green]The new format was already in use[/green]")
            sleep(2)
            tx_menu()
            
        elif (browser in tx_video_browsers_avaible): 
            with open(config_path, 'w') as file:
                json.dump(data, file, indent=4)
            rich.print("[green]Success[/green]")
            sleep(2)
            tx_menu()

        else:
            rich.print("\n[red]Error[/rec]")
            sleep(3)
            tx_menu()