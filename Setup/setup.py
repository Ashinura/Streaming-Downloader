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
    result = subprocess.run(["pip", "install", "-r", os.path.join(script_dir, "requirements.txt")])



def pytube_fix(): 

    pytube_folder = site.getusersitepackages() + '/pytube'
    file_to_modify = os.path.join(pytube_folder, 'cipher.py')

    if os.path.exists(file_to_modify):
        with fileinput.FileInput(file_to_modify, inplace=True) as file:
            for line in file:
                new_line = line.replace('var_regex = re.compile(r"^\w+\W")', 'var_regex = re.compile(r"^\$*\w+\W")')
                print(new_line, end='')

    else:
        print(f"File: {file_to_modify} not found.")
        print(f"Pytube module not fixed, you may get an error using Youtube Downloader.")


def installation():

    dl_packages()
    time.sleep(3)
    pytube_fix()

    
    pytube_folder = site.getusersitepackages() + '/pytube'
    file_to_read = os.path.join(pytube_folder, 'cipher.py')

    if os.path.exists(file_to_read):
        with open(file_to_read, 'r') as file:
            for line in file:
                if 'var_regex = re.compile(r"^\$*\w+\W")' in line:
                    fix = True   
 
    else:
        fix = False
    
    if result.returncode == 0:
        dependencies = True
    
    else:
        dependencies = (result.returncode, "missing dependencies.")


    if dependencies == True and fix == True:
        return print("\n\nInstallation completed successfully\n")
    
    elif dependencies == True and fix == False: 
        return print("\n\nAll modules are installed but Pytube module is not fixed, you may get an error using Youtube Downloader. Send a GitHub Issue or try to contact me ('ashinura' on discord) if you don't know how to fix it.\n")
    
    elif type(dependencies) == str and fix == True: 
        return print(f"\n\n{dependencies} Pytube module is fixed.\n")
    
    elif type(dependencies) == str and fix == False: 
        return print("\n\nThe installation went wrong, try again by reading the readme.md carefully. Send a GitHub Issue or try to contact me ('ashinura' on discord) if you still get issue\n")



installation()