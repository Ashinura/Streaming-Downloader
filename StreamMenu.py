import colorama
import rich
import os



def main_logo():

    print(colorama.Fore.LIGHTMAGENTA_EX)
    rich.print(" _______ __                             __                  _____                       __                __            ")
    rich.print("|     __|  |_.----.-----.---.-.--------|__.-----.-----.    |     \.-----.--.--.--.-----|  .-----.---.-.--|  .-----.----.")   # Category : Regular FIGlet fonts
    rich.print("|__     |   _|   _|  -__|  _  |        |  |     |  _  |    |  --  |  _  |  |  |  |     |  |  _  |  _  |  _  |  -__|   _|")   # Font : Chunky
    rich.print("|_______|____|__| |_____|___._|__|__|__|__|__|__|___  |    |_____/|_____|________|__|__|__|_____|___._|_____|_____|__|  ")   # Print : Streaming Downloader
    rich.print("                                                |_____|                                                                 ")
    rich.print("                                                                         [pink]Tool made by Ashinura[/pink]             ")
    print(colorama.Fore.RESET)



def main_menu(): 

    os.system('cls')


    main_logo()

    rich.print("[green][[/green]" + "[bold white]9[/bold white]" + "[green]][/green]", "[cyan]Show/Edit configuration[/cyan]\n\n")

    rich.print(
        "[yellow][[/yellow]" + "[bold white]1[/bold white]" + "[yellow]][/yellow]", "[white]YouTube[/white]\n"
        "[yellow][[/yellow]" + "[bold white]2[/bold white]" + "[yellow]][/yellow]", "[white]Spotify[/white]\n"
    )


    choice = False

    while not choice:
        try:   
            option = int(input(f"\n{colorama.Fore.LIGHTMAGENTA_EX}[{colorama.Fore.LIGHTWHITE_EX}~{colorama.Fore.LIGHTMAGENTA_EX}] {colorama.Fore.LIGHTWHITE_EX}Chose an option : "))

            if option in [1, 2, 9]:
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

    if option == 1:
        from Platform.YouTube.YouTubeMenu import yt_menu
        yt_menu()

    elif option == 2:
        from Platform.Spotify.SpotifyMenu import sp_menu
        sp_menu()

    elif option == 9:
        from Configuration.ConfigMenu import config_menu
        config_menu()



if __name__ == "__main__":
    main_menu()