import subprocess
import os
import site
import fileinput
import re
import time
import sys

script_dir = os.path.dirname(os.path.realpath(__file__))
script_dir = re.sub(r"\\", "/", script_dir)

def installation_logo():
    print("  ___         _        _ _      _   _          ")
    print(" |_ _|_ _  __| |_ __ _| | |__ _| |_(_)___ _ _  ")
    print("  | || ' \(_-<  _/ _` | | / _` |  _| / _ \ ' \ ")
    print(" |___|_||_/__/\__\__,_|_|_\__,_|\__|_\___/_||_|")
    print("                                               ")



def installation_menu(): 

    installation_logo()

    print(
        "[0]", "Check for updates    |   https://github.com/Ashinura/Streaming-Downloader/releases\n\n"
        "[1]", "Full Installation    |   Recommended for first-time installation, does everything listed below.\n\n"
        "[2]", "Install all packages |   Download all packages required to run Streaming-Downloader.\n"
        "[3]", "Install FFmpeg       |   Quality of youtube videos downloaded was increased but you must install FFmpeg now.\n"
        "[4]", "Install GIT          |   Necessary for enable auto-check-update in user configuration.\n"
    )

    choice = False

    while not choice:
        try:   
            option = int(input("\nChose an option : "))

            if option in [0, 1, 2, 3, 4]:
                choice = True

            else:
                print(
                    "[!] Invalid option selected, doesn't exist yet."
                )

        except ValueError:
            print(
                "[!] Invalid option selected, must be int."
            )

    if option == 0:
        from Configuration.GHAutoUpdate import github_update
        github_update()

    elif option == 1:
        installation()

    elif option == 2:
        dl_packages()

    elif option == 3:
        install_ffmpeg()

    elif option == 4:
        install_git()



def dl_packages():

    global pip_upgrade
    global result
    
    os.system('cls')
    installation_logo()
    print("Full Installation...")

    pip_upgrade = subprocess.run(["python", "-m", "pip", "install", "--upgrade", "pip"])
    result = subprocess.run(["pip", "install", "-r", os.path.join(script_dir, "requirements.txt")])



def install_ffmpeg():
    
    global dlffmpeg

    dlffmpeg = False

    os.system('cls')
    installation_logo()
    print("FFmpeg installation...")

    try:
        dlffmpeg = subprocess.run(["spotdl", "--download-ffmpeg"], check=True)
        print("FFmpeg installé avec succès.")
        print("\nYou must have the .spotdl folder in your variable path to download youtube video better than 720p quality")
        print(".spotdl is normally in 'C:/User/user_name/.spotdl'")
    except subprocess.CalledProcessError:
        print("Une erreur s'est produite lors de l'installation de FFmpeg.")



def install_git():

    os.system('cls')
    installation_logo()
    print("GIT installation...")

    try:
        subprocess.check_output(["git", "--version"])
        print("Git is already installed.")

    except FileNotFoundError:

        try:
            subprocess.run(['winget', 'install', '--id', 'Git.Git', '-e', '--source', 'winget'])

        except subprocess.CalledProcessError as err:
            print("Error while opening Git download page:", err)
            print("Please download and install Git from the official website.")
            print("After installation, please exit and run this script again.")
            time.sleep(3)
            git_installer_url = "https://git-scm.com/download/win"
            subprocess.run(["start", git_installer_url], shell=True, check=True)



def set_python_path():

    if any("python" in p.lower() for p in os.environ["PATH"].split(os.pathsep)):
        print("Python is already in the PATH. No modifications necessary.")
        return

    python_executable_path = sys.executable
    print(f"Path to python.exe: {python_executable_path}")

    site_packages_path = site.getsitepackages()
    print("Path to site-packages directory:", site_packages_path)

    new_path = re.sub(r"\\", '\\\\', site_packages_path[0])
    print("New path to site-packages directory:", new_path)

    os.environ['Path'] = os.environ['Path'] + ';' + python_executable_path + ';' + new_path

    subprocess.run(['pip', 'install', 'pyuac'])
    import pyuac

    try:
        if not pyuac.isUserAdmin():
            print("You are not running in admin.")
            print("Running as admin...")
            pyuac.runAsAdmin(subprocess.run(['setx', '/M', 'Path', os.environ['Path']], check=True))

        print("The PATH variable has been successfully updated.")
        
    except subprocess.CalledProcessError as err:
        print("Error updating the PATH variable:", err)


def installation():

    dl_packages()
    install_ffmpeg()
    install_git()

    os.system('cls')
    installation_logo()
    print("Installation Informations : ")
    

    if result.returncode == 0:
        dependencies = True

    else:
        dependencies = (result.returncode, "missing dependencies.")


    if dlffmpeg != False and dlffmpeg.returncode == 0:
        ytdlp = True

    else:
        ytdlp = ("FFmpeg is missing.")
    

    if dependencies == True and ytdlp == True:
        return print("\n\nInstallation completed successfully\n")
    
    elif dependencies == True and ytdlp == False: 
        return print(f"\n\nAll modules are installed but FFmpeg is not installed, you may get an error using Youtube Downloader. Try to rerun setup.bat or submit a new github issue if it doesn't help\n")
    
    elif type(dependencies) == str and ytdlp == True: 
        return print(f"\n\n{dependencies} FFmpeg is not installed")
    
    elif type(dependencies) == str and ytdlp == False: 
        return print(f"\n\nThe installation went wrong, try again by reading the readme.md carefully then rerun setup.bat or submit a new github issue if it doesn't help\n")

    if pip_upgrade.returncode == 0: 
        print("Pip was updated")


installation_menu()