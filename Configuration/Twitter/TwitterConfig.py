import os 
import rich
import colorama
from time import sleep
from ..ConfigExtras import *


def tx_config_menu():

    os.system('cls')
        
    import json

    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(os.path.join(dir_path, '..', 'config.json'), 'r') as file: 
        data = json.load(file)

    tx_videos_path = data['twitter']['videos']['path']
    tx_videos_format = data['twitter']['videos']['format']
    tx_videos_cookie = data['twitter']['videos']['cookie-browser']

    from ..ConfigExtras import logo
    logo()

    rich.print("[green][[/green]" + "[bold white]0[/bold white]" + "[green]][/green]", "[cyan]Back to the main menu[/cyan]")
    rich.print("[green][[/green]" + "[bold white]9[/bold white]" + "[green]][/green]", "[cyan]Back to the config menu[/cyan]\n\n")

    rich.print( "┌------------------------------------------------------------------------------------------------------------┐")
    rich.print( "|                                                  Twitter                                                   |")
    rich.print( "├------------------------------------------------------------------------------------------------------------┤\n")
    rich.print("    [bright_black]([/bright_black]" + "[bold white]![/bold white]" + "[bright_black])[/bright_black]", "Note that the metadata aren't set yet.")
    rich.print("    [bright_black]([/bright_black]" + "[bold white]![/bold white]" + "[bright_black])[/bright_black]", "The path must be an absolute path.\n")
    rich.print("    [yellow][[/yellow]" + "[bold white]1[/bold white]" + "[yellow]][/yellow]", f"Edit - videos | Path: [green]{tx_videos_path}[/green] - Format : [green]{tx_videos_format}[/green] - Browser : [green]{tx_videos_cookie}[/green]")
    rich.print("\n    [yellow][[/yellow]" + "[bold white]2[/bold white]" + "[yellow]][/yellow]", "Clear videos folder files")
    rich.print( "\n└------------------------------------------------------------------------------------------------------------┘")


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
        from .TXConfigVideos import tx_config_menu_videos
        tx_config_menu_videos()

    elif option == 4:
        clear_folder(os.path.abspath(tx_videos_path))
        if is_folder_empty(os.path.abspath(tx_videos_path)):
            print(f"{colorama.Fore.LIGHTGREEN_EX}The videos folder has been successfully cleared.{colorama.Fore.RESET}")
            sleep(1)
            tx_config_menu()

    elif option == 9: 
        from Configuration.ConfigMenu import config_menu
        config_menu()