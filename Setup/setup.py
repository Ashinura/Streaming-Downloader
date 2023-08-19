import subprocess
import os
import site
import fileinput
import re
import time

script_dir = os.path.dirname(os.path.realpath(__file__))
script_dir = re.sub(r"\\", "/", script_dir)

def dl_packages():

    global result
    global pip_upgrade

    pip_upgrade = subprocess.run(["python", "-m", "pip", "install", "--upgrade", "pip"])
    result = subprocess.run(["pip", "install", "-r", os.path.join(script_dir, "requirements.txt")])



def pytube_fix(): 

    global file_to_modify

    pytube_folder = site.getusersitepackages() + '/pytube'
    file_to_modify = os.path.join(pytube_folder, 'cipher.py')

    if os.path.exists(file_to_modify):

        with fileinput.FileInput(file_to_modify, inplace=True) as file:
            for line in file:
                new_line = line.replace('var_regex = re.compile(r"^\w+\W")', 'var_regex = re.compile(r"^\$*\w+\W")')
                print(new_line, end='')

    elif os.path.exists(file_to_modify) == False:
        try:
            import pytube
        except ImportError:
            print("\nPytube package is missing.")

        else:
            pytube_folder = os.path.dirname(pytube.__file__)
            file_to_modify = os.path.join(pytube_folder, 'cipher.py')

            if os.path.exists(file_to_modify):
                with fileinput.FileInput(file_to_modify, inplace=True) as file:
                    for line in file:
                        new_line = line.replace('var_regex = re.compile(r"^\w+\W")', 'var_regex = re.compile(r"^\$*\w+\W")')
                        print(new_line, end='')

    else: 
        print("Pytube fix can't be done, if you are at this stage, do the steps of pytube fix manually on readme.md and please submit a new github issue.")



def installation():

    dl_packages()
    time.sleep(3)
    pytube_fix()

    with open(file_to_modify, 'r') as file:
        for line in file:
            if 'var_regex = re.compile(r"^\$*\w+\W")' in line:
                fix = True

    
    if result.returncode == 0:
        dependencies = True
    
    else:
        dependencies = (result.returncode, "missing dependencies.")


    if dependencies == True and fix == True:
        return print("\n\nInstallation completed successfully\n")
    
    elif dependencies == True and fix == False: 
        return print(f"\n\nAll modules are installed but Pytube module is not fixed, you may get an error using Youtube Downloader. Try to rerun setup.bat or submit a new github issue if it doesn't help\n")
    
    elif type(dependencies) == str and fix == True: 
        return print(f"\n\n{dependencies} Pytube module is fixed.\n")
    
    elif type(dependencies) == str and fix == False: 
        return print(f"\n\nThe installation went wrong, try again by reading the readme.md carefully then rerun setup.bat or submit a new github issue if it doesn't help\n")

    if pip_upgrade.returncode == 0: 
        print("Pip was updated")



installation()