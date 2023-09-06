import colorama
import rich
import json
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



def check_update(requested: bool):

    from Configuration.GHAutoUpdate import github_update
    config_path = os.path.join('.', 'Configuration', 'config.json')

    with open(config_path, 'r') as file:
        data = json.load(file)

    check_autoupdt = data["user"]["autoupdate"]

    if check_autoupdt == "True":
        github_update()

    elif requested == True:
        github_update()



def main_menu(): 

    os.system('cls')

    main_logo()

    rich.print("[green][[/green]" + "[bold white]0[/bold white]" + "[green]][/green]", "[cyan]Check for update[/cyan]")
    rich.print("[green][[/green]" + "[bold white]9[/bold white]" + "[green]][/green]", "[cyan]Show/Edit configuration[/cyan]\n\n")

    rich.print(
        "[yellow][[/yellow]" + "[bold white]1[/bold white]" + "[yellow]][/yellow]", "[white]YouTube[/white]", "        "
        "[yellow][[/yellow]" + "[bold white]3[/bold white]" + "[yellow]][/yellow]", "[white]Spotify[/white]\n" + 
        "[yellow][[/yellow]" + "[bold white]2[/bold white]" + "[yellow]][/yellow]", "[white]Twitch[/white]", "         "
        "[yellow][[/yellow]" + "[bold white]4[/bold white]" + "[yellow]][/yellow]", "[white]SoundCloud[/white]\n"
    )

    choice = False

    while not choice:
        try:   
            option = int(input(f"\n{colorama.Fore.LIGHTMAGENTA_EX}[{colorama.Fore.LIGHTWHITE_EX}~{colorama.Fore.LIGHTMAGENTA_EX}] {colorama.Fore.LIGHTWHITE_EX}Chose an option : "))

            if option in [0, 1, 2, 3, 4, 9]:
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
        check_update(requested=True)

    elif option == 1:
        from Platform.YouTube.YouTubeMenu import yt_menu
        yt_menu()
        
    elif option == 2:
        from Platform.Twitch.TwitchMenu import tw_menu
        tw_menu()

    elif option == 3:
        from Platform.Spotify.SpotifyMenu import sp_menu
        sp_menu()

    elif option == 4:
        from Platform.Soundcloud.SoundCloudMenu import sc_menu
        sc_menu()

    elif option == 9:
        from Configuration.ConfigMenu import config_menu
        config_menu()



if __name__ == "__main__":
    check_update(requested=False)
    main_menu()