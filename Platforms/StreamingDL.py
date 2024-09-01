# Copyright (C) 2024 Ashinura, <dev.ashinura@protonmail.com>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

import os
import rich
from rich.prompt import Prompt
from pyfiglet import figlet_format
from termcolor import colored

logo = colored((figlet_format('Streaming  Downloader', font= 'chunky', width = 200)), "magenta")


def main_menu(): 

    os.system('cls')

    print(logo)

    rich.print("[green][[/green]" + "[bold white]0[/bold white]" + "[green]][/green]", "[cyan]Check for update[/cyan]")
    rich.print("[green][[/green]" + "[bold white]9[/bold white]" + "[green]][/green]", "[cyan]Show/Edit configuration[/cyan]\n")

    choice = False


    while not choice:
              
        option = Prompt.ask(f"\n[magenta][[/magenta][bold white]~[/bold white][magenta]][/magenta] Option / URL")

        try:
            intopt = int(option)   

            if intopt in [0, 9]:
                choice = True
                print('Options are not avaible yet')

            else:
                raise KeyError
            
        except KeyError:
            rich.print(
                "[red][[/red]" + "[bold white]![/bold white]" + "[red]][/red]",
                "[white]Invalid option selected.[/white]"
            )

        except ValueError:
            try:
                stropt = str(option)   
                
                if(stropt.startswith("https")):
                    choice = True
                    from siteProcess import siteProcess
                    siteProcess(stropt)
                
                else:
                    raise ValueError
            
            except ValueError:
                rich.print(
                   "[red][[/red]" + "[bold white]![/bold white]" + "[red]][/red]",
                   "[white]Invalid URL.[/white]"
                )
        
        
main_menu()