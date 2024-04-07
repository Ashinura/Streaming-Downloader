import rich
import colorama
import json
import os
import re
from time import sleep
from ..ConfigExtras import logo



def tx_config_menu_videos():
        
    os.system('cls')
    
    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(os.path.join(dir_path, '..', 'config.json'), 'r') as file: 
        data = json.load(file)

    tx_videos_path = data['twitter']['videos']['path']
    tx_videos_format = data['twitter']['videos']['format']
    tx_videos_cookie = data['twitter']['videos']['cookie-browser']


    logo()

    rich.print("[green][[/green]" + "[bold white]0[/bold white]" + "[green]][/green]", "[cyan]Back to the main menu[/cyan]")
    rich.print("[green][[/green]" + "[bold white]9[/bold white]" + "[green]][/green]", "[cyan]Back to the config menu[/cyan]\n")

    rich.print( "┌-----------------------------------------------------------------------------------------------------------┐")
    rich.print( "|                                           Twitter - videos                                                |")
    rich.print( "├-----------------------------------------------------------------------------------------------------------┤\n")
    rich.print("    [yellow][[/yellow]" + "[bold white]1[/bold white]" + "[yellow]][/yellow]", f"Edit - All\n")
    rich.print("    [yellow][[/yellow]" + "[bold white]2[/bold white]" + "[yellow]][/yellow]", f"Edit - Path: [green]{tx_videos_path}[/green]")
    rich.print("    [yellow][[/yellow]" + "[bold white]3[/bold white]" + "[yellow]][/yellow]", f"Edit - Format : [green]{tx_videos_format}[/green]")
    rich.print("    [yellow][[/yellow]" + "[bold white]4[/bold white]" + "[yellow]][/yellow]", f"Edit - Browser : [green]{tx_videos_cookie}[/green]")
    rich.print("\n└----------------------------------------------------------------------------------------------------------┘\n")

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
        from StreamMenu import main_menu
        main_menu()

    elif option == 1:
        tx_config_menu_videos_editpath(andformat=True, andbrowser=True)

    elif option == 2:
        tx_config_menu_videos_editpath(andformat=False, andbrowser=False)

    elif option == 3:
        tx_config_menu_videos_editformat(andbrowser=False)

    elif option == 4:
        tx_config_menu_videos_editbrowser()

    elif option == 9: 
        from Configuration.ConfigMenu import config_menu
        config_menu()



def tx_config_menu_videos_editpath(andformat, andbrowser):

    script_dir = os.path.dirname(os.path.realpath(__file__))
    dir_path = os.path.join(script_dir, '..', 'config.json')
            
    new_path = str(input(f"\n{colorama.Fore.LIGHTMAGENTA_EX}[{colorama.Fore.LIGHTWHITE_EX}~{colorama.Fore.LIGHTMAGENTA_EX}] {colorama.Fore.LIGHTWHITE_EX}New path : "))
    new_path = re.sub(r"\\", "/", new_path)

    with open(dir_path, 'r') as file:
        data = json.load(file)
  
    tx_videos_path = data['twitter']['videos']['path']
    tx_videos_format = data['twitter']['videos']['format']
    tx_videos_cookie = data['twitter']['videos']['cookie-browser']

    platform = 'twitter'
    key = 'videos'
    value = {
        'path': new_path,
        'format': tx_videos_format,
        'cookie-browser': tx_videos_cookie
    }
    
    data[platform][key] = value

    with open(dir_path, 'w') as file:
        json.dump(data, file, indent=4)

    tx_videos_path = data['twitter']['videos']['path']
    
    if (tx_videos_path == new_path): 
        rich.print("[green]Success[/green]")
        if (andformat == True and andbrowser == True):
            sleep(1)
            tx_config_menu_videos_editformat(andbrowser=True)
        else:
            sleep(2)
            tx_config_menu_videos()

    else:
        rich.print("\n[red]Error[/red]")
        sleep(3)
        tx_config_menu_videos()



def tx_config_menu_videos_editformat(andbrowser):

    script_dir = os.path.dirname(os.path.realpath(__file__))
    dir_path = os.path.join(script_dir, '..', 'config.json')
    
    with open(dir_path, 'r') as file:
        data = json.load(file)

    tx_videos_browsers_avaible = data["twitter"]["valid_twitter_format"]
    tx_videos_path = data['twitter']['videos']['path']
    tx_videos_format = data['twitter']['videos']['format']
    tx_videos_cookie = data['twitter']['videos']['cookie-browser']


    print("\nFormats available :", tx_videos_browsers_avaible) 
    new_format = str(input(f"{colorama.Fore.LIGHTMAGENTA_EX}[{colorama.Fore.LIGHTWHITE_EX}~{colorama.Fore.LIGHTMAGENTA_EX}] {colorama.Fore.LIGHTWHITE_EX}New format : "))

    platform = 'twitter'
    key = 'videos'
    value = {
        'path': tx_videos_path,
        'format': new_format,
        'cookie-browser': tx_videos_cookie       
    }
    
    with open(dir_path, 'r') as file:
        data = json.load(file)

    data[platform][key] = value

    if (new_format not in tx_videos_browsers_avaible):
        rich.print("[yellow]Please note that the new format is not in the list of valid formats required by the 'twitter' module. You must choose one from the list to be able to download via twitter, otherwise an error will occur in the 'twitter' module.[/yellow]")
        rich.print(f"List : [magenta]{tx_videos_browsers_avaible}[/magenta]")
        sleep(6)
        rich.print("[red]Failed[/red]")
        sleep(2)
        tx_config_menu_videos()

    elif (new_format == tx_videos_format):
        rich.print("[green]The new format was already in use[/green]")
        sleep(2)
        if (andbrowser == True):
            tx_config_menu_videos_editbrowser()
        else:
            tx_config_menu_videos()
        
    elif (new_format in tx_videos_browsers_avaible): 
        with open(dir_path, 'w') as file:
            json.dump(data, file, indent=4)
        rich.print("[green]Success[/green]")
        sleep(2)
        if (andbrowser == True):
            tx_config_menu_videos_editbrowser()
        else:
            tx_config_menu_videos()

    else:
        rich.print("\n[red]Error[/rec]")
        sleep(3)
        tx_config_menu_videos()



def tx_config_menu_videos_editbrowser():
        
    script_dir = os.path.dirname(os.path.realpath(__file__))
    dir_path = os.path.join(script_dir, '..', 'config.json')
    
    with open(dir_path, 'r') as file:
        data = json.load(file)

    tx_videos_path = data['twitter']['videos']['path']
    tx_videos_format = data['twitter']['videos']['format']
    tx_videos_cookie = data['twitter']['videos']['cookie-browser']
    tx_videos_browsers_avaible = data['twitter']['valid_cookie_browser']


    print("\nBrowsers available :", tx_videos_browsers_avaible) 
    new_browser = str(input(f"{colorama.Fore.LIGHTMAGENTA_EX}[{colorama.Fore.LIGHTWHITE_EX}~{colorama.Fore.LIGHTMAGENTA_EX}] {colorama.Fore.LIGHTWHITE_EX}New browser : "))

    platform = 'twitter'
    key = 'videos'
    value = {
        'path': tx_videos_path,
        'format': tx_videos_format,
        'cookie-browser': new_browser     
    }
    
    with open(dir_path, 'r') as file:
        data = json.load(file)

    data[platform][key] = value

    if (new_browser not in tx_videos_browsers_avaible):
        rich.print("[yellow]Please note that the new format is not in the list of valid formats required by the 'twitter' module. You must choose one from the list to be able to download via twitter, otherwise an error will occur in the 'twitter' module.[/yellow]")
        rich.print(f"List : [magenta]{tx_videos_browsers_avaible}[/magenta]")
        sleep(6)
        rich.print("[red]Failed[/red]")
        sleep(2)
        tx_config_menu_videos()

    elif (new_browser == tx_videos_cookie):
        rich.print("[green]The new format was already in use[/green]")
        sleep(2)
        tx_config_menu_videos()
        
    elif (new_browser in tx_videos_browsers_avaible): 
        with open(dir_path, 'w') as file:
            json.dump(data, file, indent=4)
        rich.print("[green]Success[/green]")
        sleep(2)
        tx_config_menu_videos()

    else:
        rich.print("\n[red]Error[/rec]")
        sleep(3)
        tx_config_menu_videos()