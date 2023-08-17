import os
import colorama
import rich



def yt_menu(): 

    os.system('cls')

    from .YouTubeExtras import logo


    logo(music=False, video=False, short=False)

    rich.print("[green][[/green]" + "[bold white]0[/bold white]" + "[green]][/green]", "[cyan]Back to the main menu[/cyan]")
    rich.print("[green][[/green]" + "[bold white]9[/bold white]" + "[green]][/green]", "[cyan]Show/Edit configuration[/cyan]\n\n")

    rich.print(
        "[yellow][[/yellow]" + "[bold white]1[/bold white]" + "[yellow]][/yellow]", "[white]Music[/white]\n"
        "[yellow][[/yellow]" + "[bold white]2[/bold white]" + "[yellow]][/yellow]", "[white]Videos[/white]\n"
        "[yellow][[/yellow]" + "[bold white]3[/bold white]" + "[yellow]][/yellow]", "[white]Shorts[/white]\n"
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
        from .YouTubeMusic import yt_music
        yt_music()

    elif option == 2:
        from .YouTubeVideo import yt_video
        yt_video()

    elif option == 3:
        from .YoutubeShorts import yt_short
        yt_short()

    elif option == 9: 
        from Configuration.Youtube.YouTubeConfig import yt_config_menu
        yt_config_menu()