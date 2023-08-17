import rich
import colorama
import json
import os
from ..ConfigExtras import logo



def yt_config_menu_video():
        
    os.system('cls')
    
    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(os.path.join(dir_path, '..', 'config.json'), 'r') as file: 
        data = json.load(file)

    yt_videos_path = data['youtube']['videos']['path']
    yt_videos_format = data['youtube']['videos']['format']


    logo()

    rich.print("[green][[/green]" + "[bold white]0[/bold white]" + "[green]][/green]", "[cyan]Back to the main menu[/cyan]")
    rich.print("[green][[/green]" + "[bold white]9[/bold white]" + "[green]][/green]", "[cyan]Back to the config menu[/cyan]\n")

    rich.print( "┌-----------------------------------------------------------------------------------------------------------┐")
    rich.print( "|                                           YouTube - Video                                                 |")
    rich.print( "├-----------------------------------------------------------------------------------------------------------┤\n")
    rich.print("    [yellow][[/yellow]" + "[bold white]1[/bold white]" + "[yellow]][/yellow]", f"Edit - Path & Format\n")
    rich.print("    [yellow][[/yellow]" + "[bold white]2[/bold white]" + "[yellow]][/yellow]", f"Edit - Path: [green]{yt_videos_path}[/green]")
    rich.print("    [yellow][[/yellow]" + "[bold white]3[/bold white]" + "[yellow]][/yellow]", f"Edit - Format : [green]{yt_videos_format}[/green]")
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
        yt_config_menu_video_editpath(andformat=True)

    elif option == 2:
        yt_config_menu_video_editpath(andformat=False)

    elif option == 3:
        yt_config_menu_video_editformat()

    elif option == 9: 
        from Configuration.ConfigMenu import config_menu
        config_menu()





def yt_config_menu_video_editpath(andformat):

    from time import sleep
    import re

    script_dir = os.path.dirname(os.path.realpath(__file__))
    dir_path = os.path.join(script_dir, '..', 'config.json')
            
    new_path = str(input(f"\n{colorama.Fore.LIGHTMAGENTA_EX}[{colorama.Fore.LIGHTWHITE_EX}~{colorama.Fore.LIGHTMAGENTA_EX}] {colorama.Fore.LIGHTWHITE_EX}New path : "))
    new_path = re.sub(r"\\", "/", new_path)

    with open(dir_path, 'r') as file:
        data = json.load(file)
  
    yt_videos_format = data['youtube']['videos']['format']

    platform = 'youtube'
    key = 'videos'
    value = {
        'path': new_path,
        'format': yt_videos_format
    }
    
    data[platform][key] = value

    with open(dir_path, 'w') as file:
        json.dump(data, file, indent=4)

    yt_videos_path = data['youtube']['videos']['path']
    
    if (yt_videos_path == new_path): 
        rich.print("[green]Success[/green]")
        if (andformat == True):
            sleep(1)
            yt_config_menu_video_editformat()
        else:
            sleep(2)
            yt_config_menu_video()

    else:
        rich.print("\n[red]Error[/red]")
        sleep(3)
        yt_config_menu_video()



def yt_config_menu_video_editformat():
            
    from time import sleep

    script_dir = os.path.dirname(os.path.realpath(__file__))
    dir_path = os.path.join(script_dir, '..', 'config.json')
            
    new_format = str(input(f"\n{colorama.Fore.LIGHTMAGENTA_EX}[{colorama.Fore.LIGHTWHITE_EX}~{colorama.Fore.LIGHTMAGENTA_EX}] {colorama.Fore.LIGHTWHITE_EX}New format : "))

    with open(dir_path, 'r') as file:
        data = json.load(file)

    most_used_formats = data["most_used_formats"]["video"]
  
    yt_videos_path = data['youtube']['videos']['path']
    yt_videos_format = data['youtube']['videos']['format']

    platform = 'youtube'
    key = 'videos'
    value = {
        'path': yt_videos_path,
        'format': new_format
    }
    
    with open(dir_path, 'r') as file:
        data = json.load(file)

    data[platform][key] = value

    with open(dir_path, 'w') as file:
        json.dump(data, file, indent=4)

    if (new_format == yt_videos_format):
        rich.print("[green]The new format was already in use[/green]")
        sleep(2)
        yt_config_menu_video()

    elif (new_format in most_used_formats): 
        rich.print("[green]Success[/green]")
        sleep(2)
        yt_config_menu_video()

    elif (new_format not in most_used_formats):
        rich.print("[yellow]Warning, the new format is not in the list of most frequently used formats, so note this if an error occurs later.[/yellow]")
        rich.print(f"List : [magenta]{most_used_formats}[/magenta]")
        sleep(8)
        rich.print("[green]Success[/green]")
        sleep(2)
        yt_config_menu_video()

    else:
        rich.print("\n[red]Error[/rec]")
        sleep(3)
        yt_config_menu_video()