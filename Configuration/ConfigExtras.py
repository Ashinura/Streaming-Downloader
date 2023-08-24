import colorama
import rich
import json
import os
import subprocess
from send2trash import send2trash



def logo(): 
    print(colorama.Fore.LIGHTMAGENTA_EX)
    print("   ___           __ _                    _   _          ")
    print("  / __|___ _ _  / _(_)__ _ _  _ _ _ __ _| |_(_)___ _ _  ")   # Category : Featured FIGlet fonts 
    print(" | (__/ _ \ ' \|  _| / _` | || | '_/ _` |  _| / _ \ ' \ ")   # Font : Small
    print("  \___\___/_||_|_| |_\__, |\_,_|_| \__,_|\__|_\___/_||_|")   # Print : Configuration
    print("                     |___/                              ")
    print("                                                        ")
    print(colorama.Fore.RESET)



def clear_folder(folder_path):
    for root, dirs, files in os.walk(folder_path, topdown=False):

        for file in files:
            file_path = os.path.join(root, file)
            send2trash(file_path)

        for dir in dirs:
            dir_path = os.path.join(root, dir)
            send2trash(dir_path)



def is_folder_empty(folder_path):
    return not any(os.scandir(folder_path))



def user_config(): 

    os.system('cls')

    logo()

    config_path = os.path.join('.', 'Configuration', 'config.json')
    with open(config_path, 'r') as file:
        data = json.load(file)

    user_autoupdate = data["user"]["autoupdate"]
    user_quietytdl = data["user"]["quietytdl"]

    if user_autoupdate == "True":
        autoupdate = "[green]True[/green]"
    else: 
        autoupdate = "[red]False[/red]"

    if user_quietytdl == "True":
        quietytdl = "[green]True[/green]"
    else: 
        quietytdl = "[red]False[/red]"

    rich.print("[green][[/green]" + "[bold white]0[/bold white]" + "[green]][/green]", "[cyan]Back to the main menu[/cyan]")
    rich.print("[green][[/green]" + "[bold white]9[/bold white]" + "[green]][/green]", "[cyan]Back to the config menu[/cyan]\n\n")

    rich.print(
        "[yellow][[/yellow]" + "[bold white]1[/bold white]" + "[yellow]][/yellow]", "Auto-Check-Update :", autoupdate,"\n"
        "[bright_black]([/bright_black]" + "[bold white]![/bold white]" + "[bright_black])[/bright_black]", "Enable/Disable Auto-Check-Update when you launch Streaming-Downloader.\n\n"
        "[yellow][[/yellow]" + "[bold white]2[/bold white]" + "[yellow]][/yellow]", "Quiet YT-DLP :", quietytdl,"\n"
        "[bright_black]([/bright_black]" + "[bold white]![/bold white]" + "[bright_black])[/bright_black]", "If enabled, does not show any output on youtube downloading\n"
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
                    "[white]Invalid option selected, doesn't exist yet.[/white]"
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
        user_config_ghautoupdt()

    elif option == 2:
        user_config_quietytdl()

    elif option == 9:
        from .ConfigMenu import config_menu
        config_menu()



def user_config_ghautoupdt():

    try:
        subprocess.check_output(["git", "--version"])
        print("Git is installed, auto-update will be set on.")

        script_dir = os.path.dirname(os.path.realpath(__file__))
        dir_path = os.path.join(script_dir, '.', 'config.json')

        with open(dir_path, 'r') as file:
            data = json.load(file)

        quietytdl_o = data["user"]["quietytdl"]
        ghautoupdt_o = data["user"]["autoupdate"]

        if ghautoupdt_o == "True":
            ghautoupdt_n = "False"

        elif ghautoupdt_o == "False":
            ghautoupdt_n = "True"
    
        param = 'user'
        value = {"autoupdate": ghautoupdt_n, "quietytdl": quietytdl_o}

        with open(dir_path, 'r') as file:
            data = json.load(file)

        data[param] = value

        with open(dir_path, 'w') as file:
            json.dump(data, file, indent=4)

        user_config()


    except FileNotFoundError as err: 
        print("The auto-update can't be set on because 'git' is not installed, look for install it in setup.bat or manually.\nError:", err)




def user_config_quietytdl():

    script_dir = os.path.dirname(os.path.realpath(__file__))
    dir_path = os.path.join(script_dir, '.', 'config.json')

    with open(dir_path, 'r') as file:
        data = json.load(file)

    quietytdl_o = data["user"]["quietytdl"]
    ghautoupdt_o = data["user"]["autoupdate"]

    if quietytdl_o == "True":
        quietytdl_n = "False"

    elif quietytdl_o == "False":
        quietytdl_n = "True"
  

    param = 'user'
    value = {"autoupdate": ghautoupdt_o, "quietytdl": quietytdl_n}
    
    with open(dir_path, 'r') as file:
        data = json.load(file)

    data[param] = value

    with open(dir_path, 'w') as file:
        json.dump(data, file, indent=4)

    user_config()