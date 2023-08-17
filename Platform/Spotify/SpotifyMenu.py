import os
import colorama
import rich



def sp_menu(): 

    os.system('cls')

    from .SpotifyExtras import logo


    logo()

    rich.print("[green][[/green]" + "[bold white]0[/bold white]" + "[green]][/green]", "[cyan]Back to the main menu[/cyan]")
    rich.print("[green][[/green]" + "[bold white]9[/bold white]" + "[green]][/green]", "[cyan]Show/Edit configuration[/cyan]\n\n")

    rich.print(
        "[yellow][[/yellow]" + "[bold white]1[/bold white]" + "[yellow]][/yellow]", "[white]Song[/white]\n"
        "[yellow][[/yellow]" + "[bold white]2[/bold white]" + "[yellow]][/yellow]", "[white]Playlist[/white]\n"
        "[yellow][[/yellow]" + "[bold white]3[/bold white]" + "[yellow]][/yellow]", "[white]Artist[/white]\n"
    )


    choice = False

    while not choice:
        try:   
            option = int(input(f"\n{colorama.Fore.LIGHTMAGENTA_EX}[{colorama.Fore.LIGHTWHITE_EX}~{colorama.Fore.LIGHTMAGENTA_EX}] {colorama.Fore.LIGHTWHITE_EX}Chose an option : "))

            if option in [0, 1, 2, 3, 9]:
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
        from .SpotifySong import sp_song
        sp_song()

    elif option == 2:
        from .SpotifyPlaylist import sp_playlist
        sp_playlist()

    elif option == 3:
        from .SpotifyArtist import sp_artist
        sp_artist()

    elif option == 9: 
        from Configuration.Spotify.SpotifyConfig import sp_config_menu
        sp_config_menu()