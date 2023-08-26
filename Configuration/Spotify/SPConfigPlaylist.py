import rich
import colorama
import json
import os
from ..ConfigExtras import logo



def sp_config_menu_playlist():
        
    os.system('cls')
    
    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(os.path.join(dir_path, '..', 'config.json'), 'r') as file: 
        data = json.load(file)

    sp_playlist_path = data['spotify']['playlist']['path']
    sp_playlist_format = data['spotify']['playlist']['format']


    logo()

    rich.print("[green][[/green]" + "[bold white]0[/bold white]" + "[green]][/green]", "[cyan]Back to the main menu[/cyan]")
    rich.print("[green][[/green]" + "[bold white]9[/bold white]" + "[green]][/green]", "[cyan]Back to the config menu[/cyan]\n")

    rich.print( "┌-----------------------------------------------------------------------------------------------------------┐")
    rich.print( "|                                           Spotify - Playlist                                                 |")
    rich.print( "├-----------------------------------------------------------------------------------------------------------┤\n")
    rich.print("    [yellow][[/yellow]" + "[bold white]1[/bold white]" + "[yellow]][/yellow]", f"Edit - Path & Format\n")
    rich.print("    [yellow][[/yellow]" + "[bold white]2[/bold white]" + "[yellow]][/yellow]", f"Edit - Path: [green]{sp_playlist_path}[/green]")
    rich.print("    [yellow][[/yellow]" + "[bold white]3[/bold white]" + "[yellow]][/yellow]", f"Edit - Format : [green]{sp_playlist_format}[/green]")
    rich.print("\n└----------------------------------------------------------------------------------------------------------┘\n")


    choice = False

    while not choice:
        try:   
            option = int(input(f"\n{colorama.Fore.LIGHTMAGENTA_EX}[{colorama.Fore.LIGHTWHITE_EX}~{colorama.Fore.LIGHTMAGENTA_EX}] {colorama.Fore.LIGHTWHITE_EX}Chose an option : "))

            if option in [0, 1, 2, 3, 9]:
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
        sp_config_menu_playlist_editpath(andformat=True)

    elif option == 2:
        sp_config_menu_playlist_editpath(andformat=False)

    elif option == 3:
        sp_config_menu_playlist_editformat()

    elif option == 9: 
        from Configuration.ConfigMenu import config_menu
        config_menu()





def sp_config_menu_playlist_editpath(andformat):

    from time import sleep
    import re

    script_dir = os.path.dirname(os.path.realpath(__file__))
    dir_path = os.path.join(script_dir, '..', 'config.json')
            
    new_path = str(input(f"\n{colorama.Fore.LIGHTMAGENTA_EX}[{colorama.Fore.LIGHTWHITE_EX}~{colorama.Fore.LIGHTMAGENTA_EX}] {colorama.Fore.LIGHTWHITE_EX}New path : "))
    new_path = re.sub(r"\\", "/", new_path)

    with open(dir_path, 'r') as file:
        data = json.load(file)
  
    sp_playlist_format = data['spotify']['playlist']['format']

    platform = 'spotify'
    key = 'playlist'
    value = {
        'path': new_path,
        'format': sp_playlist_format
    }
    
    data[platform][key] = value

    with open(dir_path, 'w') as file:
        json.dump(data, file, indent=4)

    sp_playlist_path = data['spotify']['playlist']['path']
    
    if (sp_playlist_path == new_path): 
        rich.print("[green]Success[/green]")
        if (andformat == True):
            sleep(1)
            sp_config_menu_playlist_editformat()
        else:
            sleep(2)
            sp_config_menu_playlist()

    else:
        rich.print("\n[red]Error[/red]")
        sleep(3)
        sp_config_menu_playlist()



def sp_config_menu_playlist_editformat():
            
    from time import sleep

    script_dir = os.path.dirname(os.path.realpath(__file__))
    dir_path = os.path.join(script_dir, '..', 'config.json')
    
    with open(dir_path, 'r') as file:
        data = json.load(file)

    valid_spotdl_format = data["spotify"]["valid_spotdl_format"]

    sp_playlist_path = data['spotify']['playlist']['path']
    sp_playlist_format = data['spotify']['playlist']['format']


    print("\nFormats available :", valid_spotdl_format)
    new_format = str(input(f"{colorama.Fore.LIGHTMAGENTA_EX}[{colorama.Fore.LIGHTWHITE_EX}~{colorama.Fore.LIGHTMAGENTA_EX}] {colorama.Fore.LIGHTWHITE_EX}New format : "))

    platform = 'spotify'
    key = 'playlist'
    value = {
        'path': sp_playlist_path,
        'format': new_format
    }
    
    with open(dir_path, 'r') as file:
        data = json.load(file)

    data[platform][key] = value

    with open(dir_path, 'w') as file:
        json.dump(data, file, indent=4)


    if (new_format not in valid_spotdl_format):
        rich.print("[yellow]Please note that the new format is not in the list of valid formats required by the 'spotdl' module. You must choose one from the list to be able to download via spotify, otherwise an error will occur in the 'spotdl' module.[/yellow]")
        rich.print(f"List : [magenta]{valid_spotdl_format}[/magenta]")
        sleep(12)
        rich.print("[red]Failed[/red]")
        sleep(2)
        sp_config_menu_playlist()

    elif (new_format == sp_playlist_format):
        rich.print("[green]The new format was already in use[/green]")
        sleep(2)
        sp_config_menu_playlist()
        
    elif (new_format in valid_spotdl_format): 
        rich.print("[green]Success[/green]")
        sleep(2)
        sp_config_menu_playlist()

    else:
        rich.print("\n[red]Error[/rec]")
        sleep(3)
        sp_config_menu_playlist()