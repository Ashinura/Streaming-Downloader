import os 
import rich
import colorama
from time import sleep
from ..ConfigExtras import *


def yt_config_menu():

    os.system('cls')
    logo()
        
    import json
    
    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(os.path.join(dir_path, '..', 'config.json'), 'r') as file: 
        data = json.load(file)

    yt_music_path = data['youtube']['musics']['path']
    yt_videos_path = data['youtube']['videos']['path']
    yt_shorts_path = data['youtube']['shorts']['path']

    yt_music_format = data['youtube']['musics']['format']
    yt_videos_format = data['youtube']['videos']['format']
    yt_shorts_format = data['youtube']['shorts']['format']


    rich.print("[green][[/green]" + "[bold white]0[/bold white]" + "[green]][/green]", "[cyan]Back to the main menu[/cyan]")
    rich.print("[green][[/green]" + "[bold white]9[/bold white]" + "[green]][/green]", "[cyan]Back to the config menu[/cyan]\n\n")

    rich.print( "┌-----------------------------------------------------------------------------------------------------------┐")
    rich.print( "|                                                  YouTube                                                  |")
    rich.print( "├-----------------------------------------------------------------------------------------------------------┤\n")
    rich.print("    [bright_black]([/bright_black]" + "[bold white]![/bold white]" + "[bright_black])[/bright_black]", "Note that the best video quality (8k 60fps) is generated only with the 'best' or 'webm' format.\n")
    rich.print("    [yellow][[/yellow]" + "[bold white]1[/bold white]" + "[yellow]][/yellow]", f"Edit - Musics | Path: [green]{yt_music_path}[/green] - Format : [green]{yt_music_format}[/green]")
    rich.print("    [yellow][[/yellow]" + "[bold white]2[/bold white]" + "[yellow]][/yellow]", f"Edit - Videos | Path: [green]{yt_videos_path}[/green] - Format : [green]{yt_videos_format}[/green]")
    rich.print("    [yellow][[/yellow]" + "[bold white]3[/bold white]" + "[yellow]][/yellow]", f"Edit - Shorts | Path: [green]{yt_shorts_path}[/green] - Format : [green]{yt_shorts_format}[/green]\n")
    rich.print("    [yellow][[/yellow]" + "[bold white]4[/bold white]" + "[yellow]][/yellow]", "Clear Musics folder files")
    rich.print("    [yellow][[/yellow]" + "[bold white]5[/bold white]" + "[yellow]][/yellow]", "Clear Videos folder files")
    rich.print("    [yellow][[/yellow]" + "[bold white]6[/bold white]" + "[yellow]][/yellow]", "Clear Shorts folder files")
    rich.print( "\n└-----------------------------------------------------------------------------------------------------------┘")


    choice = False

    while not choice:
        try:   
            option = int(input(f"\n{colorama.Fore.LIGHTMAGENTA_EX}[{colorama.Fore.LIGHTWHITE_EX}~{colorama.Fore.LIGHTMAGENTA_EX}] {colorama.Fore.LIGHTWHITE_EX}Chose an option : "))

            if option in [0, 1, 2, 3, 4, 5, 6, 9]:
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
        from .YTConfigMusic import yt_config_menu_music
        yt_config_menu_music()

    elif option == 2:
        from .YTConfigVideo import yt_config_menu_video
        yt_config_menu_video()

    elif option == 3:
        from .YTConfigShort import yt_config_menu_short
        yt_config_menu_short()

    elif option == 4:
        clear_folder(os.path.abspath(yt_music_path))
        if is_folder_empty(os.path.abspath(yt_music_path)):
            print(f"{colorama.Fore.LIGHTGREEN_EX}The musics folder has been successfully cleared.{colorama.Fore.RESET}")
            sleep(1)
            yt_config_menu()

    elif option == 5:
        clear_folder(os.path.abspath(yt_videos_path))
        if is_folder_empty(os.path.abspath(yt_videos_path)):
            print(f"{colorama.Fore.LIGHTGREEN_EX}The videos folder has been successfully cleared.{colorama.Fore.RESET}")
            sleep(1)
            yt_config_menu()

    elif option == 6:
        clear_folder(os.path.abspath(yt_shorts_path))
        if is_folder_empty(os.path.abspath(yt_shorts_path)):
            print(f"{colorama.Fore.LIGHTGREEN_EX}The shorts folder has been successfully cleared.{colorama.Fore.RESET}")
            sleep(1)
            yt_config_menu()

    elif option == 9: 
        from Configuration.ConfigMenu import config_menu
        config_menu()