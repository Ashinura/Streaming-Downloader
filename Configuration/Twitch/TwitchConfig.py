import os 
import rich
import colorama
from time import sleep
from ..ConfigExtras import *


def tw_config_menu():

    os.system('cls')
        
    import json
    from ..ConfigExtras import logo
    
    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(os.path.join(dir_path, '..', 'config.json'), 'r') as file: 
        data = json.load(file)

    tw_redif_path = data['twitch']['redif']['path']
    tw_redif_format = data['twitch']['redif']['format']



    logo()

    rich.print("[green][[/green]" + "[bold white]0[/bold white]" + "[green]][/green]", "[cyan]Back to the main menu[/cyan]")
    rich.print("[green][[/green]" + "[bold white]9[/bold white]" + "[green]][/green]", "[cyan]Back to the config menu[/cyan]\n\n")

    rich.print( "┌-----------------------------------------------------------------------------------------------------------┐")
    rich.print( "|                                                  Twitch                                                  |")
    rich.print( "├-----------------------------------------------------------------------------------------------------------┤\n")
    rich.print("    [bright_black]([/bright_black]" + "[bold white]![/bold white]" + "[bright_black])[/bright_black]", "Note that the metadata aren't set yet.\n")
    rich.print("    [yellow][[/yellow]" + "[bold white]1[/bold white]" + "[yellow]][/yellow]", f"Edit - redif | Path: [green]{tw_redif_path}[/green] - Format : [green]{tw_redif_format}[/green]")
    rich.print("\n    [yellow][[/yellow]" + "[bold white]2[/bold white]" + "[yellow]][/yellow]", "Clear redif folder files")
    rich.print( "\n└-----------------------------------------------------------------------------------------------------------┘")


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
        from .TWConfigRedif import tw_config_menu_redif
        tw_config_menu_redif()

    elif option == 4:
        clear_folder(os.path.abspath(tw_redif_path))
        if is_folder_empty(os.path.abspath(tw_redif_path)):
            print(f"{colorama.Fore.LIGHTGREEN_EX}The redif folder has been successfully cleared.{colorama.Fore.RESET}")
            sleep(1)
            tw_config_menu()

    elif option == 9: 
        from Configuration.ConfigMenu import config_menu
        config_menu()