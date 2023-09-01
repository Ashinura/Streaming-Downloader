import os 
import rich
import colorama
from time import sleep
from ..ConfigExtras import *


def sc_config_menu():

    os.system('cls')
        
    import json
    from ..ConfigExtras import logo
    
    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(os.path.join(dir_path, '..', 'config.json'), 'r') as file: 
        data = json.load(file)

    sc_song_path = data['soundcloud']['song']['path']
    sc_playlist_path = data['soundcloud']['playlist']['path']
    sc_artist_path = data['soundcloud']['artist']['path']

    sc_song_format = data['soundcloud']['song']['format']
    sc_playlist_format = data['soundcloud']['playlist']['format']
    sc_artist_format = data['soundcloud']['artist']['format']


    logo()

    rich.print("[green][[/green]" + "[bold white]0[/bold white]" + "[green]][/green]", "[cyan]Back to the main menu[/cyan]")
    rich.print("[green][[/green]" + "[bold white]9[/bold white]" + "[green]][/green]", "[cyan]Back to the config menu[/cyan]\n\n")

    rich.print( "┌-----------------------------------------------------------------------------------------------------------┐")
    rich.print( "|                                                  SoundCloud                                                  |")
    rich.print( "├-----------------------------------------------------------------------------------------------------------┤\n")
    rich.print("    [bright_black]([/bright_black]" + "[bold white]![/bold white]" + "[bright_black])[/bright_black]", "Note that the metadata aren't set yet.\n")
    rich.print("    [yellow][[/yellow]" + "[bold white]1[/bold white]" + "[yellow]][/yellow]", f"Edit - Song | Path: [green]{sc_song_path}[/green] - Format : [green]{sc_song_format}[/green]")
    rich.print("    [yellow][[/yellow]" + "[bold white]2[/bold white]" + "[yellow]][/yellow]", f"Edit - Playlist | Path: [green]{sc_playlist_path}[/green] - Format : [green]{sc_playlist_format}[/green]")
    rich.print("    [yellow][[/yellow]" + "[bold white]3[/bold white]" + "[yellow]][/yellow]", f"Edit - Artist | Path: [green]{sc_artist_path}[/green] - Format : [green]{sc_artist_format}[/green]\n")
    rich.print("    [yellow][[/yellow]" + "[bold white]4[/bold white]" + "[yellow]][/yellow]", "Clear song folder files")
    rich.print("    [yellow][[/yellow]" + "[bold white]5[/bold white]" + "[yellow]][/yellow]", "Clear playlist folder files")
    rich.print("    [yellow][[/yellow]" + "[bold white]6[/bold white]" + "[yellow]][/yellow]", "Clear artist folder files")
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
        from .SCConfigSong import sc_config_menu_song
        sc_config_menu_song()

    elif option == 2:
        from .SCConfigPlaylist import sc_config_menu_playlist
        sc_config_menu_playlist()

    elif option == 3:
        from .SCConfigArtist import sc_config_menu_artist
        sc_config_menu_artist()

    elif option == 4:
        clear_folder(os.path.abspath(sc_song_path))
        if is_folder_empty(os.path.abspath(sc_song_path)):
            print(f"{colorama.Fore.LIGHTGREEN_EX}The song folder has been successfully cleared.{colorama.Fore.RESET}")
            sleep(1)
            sc_config_menu()

    elif option == 5:
        clear_folder(os.path.abspath(sc_playlist_path))
        if is_folder_empty(os.path.abspath(sc_playlist_path)):
            print(f"{colorama.Fore.LIGHTGREEN_EX}The playlist folder has been successfully cleared.{colorama.Fore.RESET}")
            sleep(1)
            sc_config_menu()

    elif option == 6:
        clear_folder(os.path.abspath(sc_artist_path))
        if is_folder_empty(os.path.abspath(sc_artist_path)):
            print(f"{colorama.Fore.LIGHTGREEN_EX}The artist folder has been successfully cleared.{colorama.Fore.RESET}")
            sleep(1)
            sc_config_menu()

    elif option == 9: 
        from Configuration.ConfigMenu import config_menu
        config_menu()