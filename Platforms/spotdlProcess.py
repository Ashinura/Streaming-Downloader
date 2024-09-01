import os
import rich
import subprocess

from pyfiglet import figlet_format
from termcolor import colored
from siteProcess import StreamDL



def spotdlProcess(request: StreamDL): 

    os.system('cls')

    logo = colored((figlet_format(f'{request.name.capitalize()}', font='small', width = 200)), f'{request.color}')

    os.system('cls')
    print(logo)

    try:
        with subprocess.Popen(f"spotdl {request.url} --output {request.path}", shell=True) as proc:
            proc.wait()

        rich.print("\n[green]Downloaded[/green]")
        input("\nPress 'Enter' to be back on menu")
        from StreamingDL import main_menu
        main_menu()

    except Exception as err:
        print(f"Error: {err}")