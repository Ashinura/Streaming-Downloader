import rich
import json
import os 

from rich.prompt import Prompt
from pyfiglet import figlet_format
from termcolor import colored

script_dir = os.path.dirname(os.path.realpath(__file__))
json_path = os.path.join(script_dir, '.', 'config.json')



def config_menu():

    logo = colored((figlet_format('Configuration', font='small', width = 200)), 'white')
    os.system('cls')
    print(logo)

    rich.print("[green][[/green]" + "[bold white]0[/bold white]" + "[green]][/green]", "[cyan]Back to the main menu[/cyan]")
    rich.print("[green][[/green]" + "[bold white]9[/bold white]" + "[green]][/green]", "[cyan]Show/Edit user configuration[/cyan]\n")
    
    with open(json_path, 'r') as file:
        config = json.load(file)

    user_quietytdlp = config["user"]["quietytdlp"]

    if user_quietytdlp == "True": quietytdlp = "[green]True[/green]"
    else: quietytdlp = "[red]False[/red]"

    rich.print(
        "[yellow][[/yellow]" + "[bold white]1[/bold white]" + "[yellow]][/yellow]", "Quiet yt-dlp :", quietytdlp, "         [bright_black]([/bright_black]" + "[bold white]![/bold white]" + "[bright_black])[/bright_black]", "If enabled, hide output of yt-dlp proccess on download\n"
    )

    choice = False

    while not choice:
              
        option = Prompt.ask(f"\n[magenta][[/magenta][bold white]~[/bold white][magenta]][/magenta] Option")

        try:
            option = int(option)   

            if option in [0, 1]:
                if option == 0:
                    choice = True
                    from StreamingDL import main_menu 
                    main_menu()
                
                if option == 1:
                    choice = True
                    user_config_quietytdl()

            else:
                raise KeyError
            
        except KeyError:
            rich.print(
                "[red][[/red]" + "[bold white]![/bold white]" + "[red]][/red]",
                "[white]Invalid option selected.[/white]"
            )


def user_config_quietytdl():

    with open(json_path, 'r') as file:
        config = json.load(file)

    quietytdlpSettings = config["user"]["quietytdlp"]

    if quietytdlpSettings == "True": quietytdlpSettings = "False"
    elif quietytdlpSettings == "False": quietytdlpSettings = "True"
  

    param = 'user'
    value = {"quietytdlp": quietytdlpSettings}
    
    with open(json_path, 'r') as file:
        config = json.load(file)

    config[param] = value

    with open(json_path, 'w') as file:
        json.dump(config, file, indent=4)

    config_menu()