import rich
import colorama
import json
import os
from ..ConfigExtras import logo



def sc_config_menu_artist():
        
    os.system('cls')
    
    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(os.path.join(dir_path, '..', 'config.json'), 'r') as file: 
        data = json.load(file)

    sc_artist_path = data['soundcloud']['artist']['path']
    sc_artist_format = data['soundcloud']['artist']['format']


    logo()

    rich.print("[green][[/green]" + "[bold white]0[/bold white]" + "[green]][/green]", "[cyan]Back to the main menu[/cyan]")
    rich.print("[green][[/green]" + "[bold white]9[/bold white]" + "[green]][/green]", "[cyan]Back to the config menu[/cyan]\n")

    rich.print( "┌-----------------------------------------------------------------------------------------------------------┐")
    rich.print( "|                                           SoundCloud - Artist                                                 |")
    rich.print( "├-----------------------------------------------------------------------------------------------------------┤\n")
    rich.print("    [yellow][[/yellow]" + "[bold white]1[/bold white]" + "[yellow]][/yellow]", f"Edit - Path & Format\n")
    rich.print("    [yellow][[/yellow]" + "[bold white]2[/bold white]" + "[yellow]][/yellow]", f"Edit - Path: [green]{sc_artist_path}[/green]")
    rich.print("    [yellow][[/yellow]" + "[bold white]3[/bold white]" + "[yellow]][/yellow]", f"Edit - Format : [green]{sc_artist_format}[/green]")
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
        sc_config_menu_artist_editpath(andformat=True)

    elif option == 2:
        sc_config_menu_artist_editpath(andformat=False)

    elif option == 3:
        sc_config_menu_artist_editformat()

    elif option == 9: 
        from Configuration.ConfigMenu import config_menu
        config_menu()





def sc_config_menu_artist_editpath(andformat):

    from time import sleep
    import re

    script_dir = os.path.dirname(os.path.realpath(__file__))
    dir_path = os.path.join(script_dir, '..', 'config.json')
            
    new_path = str(input(f"\n{colorama.Fore.LIGHTMAGENTA_EX}[{colorama.Fore.LIGHTWHITE_EX}~{colorama.Fore.LIGHTMAGENTA_EX}] {colorama.Fore.LIGHTWHITE_EX}New path : "))
    new_path = re.sub(r"\\", "/", new_path)

    with open(dir_path, 'r') as file:
        data = json.load(file)
  
    sc_artist_format = data['soundcloud']['artist']['format']

    platform = 'soundcloud'
    key = 'artist'
    value = {
        'path': new_path,
        'format': sc_artist_format
    }
    
    data[platform][key] = value

    with open(dir_path, 'w') as file:
        json.dump(data, file, indent=4)

    sc_artist_path = data['soundcloud']['artist']['path']
    
    if (sc_artist_path == new_path): 
        rich.print("[green]Success[/green]")
        if (andformat == True):
            sleep(1)
            sc_config_menu_artist_editformat()
        else:
            sleep(2)
            sc_config_menu_artist()

    else:
        rich.print("\n[red]Error[/red]")
        sleep(3)
        sc_config_menu_artist()



def sc_config_menu_artist_editformat():
            
    from time import sleep

    script_dir = os.path.dirname(os.path.realpath(__file__))
    dir_path = os.path.join(script_dir, '..', 'config.json')

    with open(dir_path, 'r') as file:
        data = json.load(file)

    valid_soundcloud_format = data["soundcloud"]["valid_soundcloud_format"]
  
    sc_artist_path = data['soundcloud']['artist']['path']
    sc_artist_format = data['soundcloud']['artist']['format']


    print("\nFormats available :", valid_soundcloud_format)           
    new_format = str(input(f"{colorama.Fore.LIGHTMAGENTA_EX}[{colorama.Fore.LIGHTWHITE_EX}~{colorama.Fore.LIGHTMAGENTA_EX}] {colorama.Fore.LIGHTWHITE_EX}New format : "))

    platform = 'soundcloud'
    key = 'artist'
    value = {
        'path': sc_artist_path,
        'format': new_format
    }
    
    with open(dir_path, 'r') as file:
        data = json.load(file)

    data[platform][key] = value


    if (new_format not in valid_soundcloud_format):
        rich.print("[yellow]Please note that the new format is not in the list of valid formats required by the 'soundcloud' module. You must choose one from the list to be able to download via soundcloud, otherwise an error will occur in the 'soundcloud' module.[/yellow]")
        rich.print(f"List : [magenta]{valid_soundcloud_format}[/magenta]")
        sleep(6)
        rich.print("[red]Failed[/red]")
        sleep(2)
        sc_config_menu_artist()

    elif (new_format == sc_artist_format):
        rich.print("[green]The new format was already in use[/green]")
        sleep(2)
        sc_config_menu_artist()
        
    elif (new_format in valid_soundcloud_format): 
        with open(dir_path, 'w') as file:
            json.dump(data, file, indent=4)
        rich.print("[green]Success[/green]")
        sleep(2)
        sc_config_menu_artist()

    else:
        rich.print("\n[red]Error[/rec]")
        sleep(3)
        sc_config_menu_artist()