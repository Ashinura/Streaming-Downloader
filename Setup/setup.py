import subprocess
import os
import site
import fileinput
import re
import time

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
        "[4]", "Install all packages |   Download all packages required to run Streaming-Downloader.\n"
        "[5]", "Install FFmpeg       |   Quality of youtube videos downloaded was increased but you must install FFmpeg now.\n"
        "[6]", "Install GIT          |   Necessary for enable auto-check-update in user configuration.\n"
    )

    choice = False

    while not choice:
        try:   
            option = int(input("Chose an option : "))

            if option in [0, 1, 2, 4, 5]:
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
        print('not aviable yet, this opt will come soon :>')
        exit()

    elif option == 1:
        installation()

    elif option == 4:
        dl_packages()

    elif option == 5:
        install_ffmpeg()



def dl_packages():

    global result
    global pip_upgrade

    os.system('cls')
    installation_logo()
    print("Full Installation...")

    pip_upgrade = subprocess.run(["python", "-m", "pip", "install", "--upgrade", "pip"])
    result = subprocess.run(["pip", "install", "-r", os.path.join(script_dir, "requirements.txt")])



def pytube_fix(): 

    global file_to_modify

    pytube_folder = site.getusersitepackages() + '/pytube'
    file_to_modify = os.path.join(pytube_folder, 'cipher.py')
    fix = False

    with open(file_to_modify, 'r') as file:
        for line in file:
            if 'var_regex = re.compile(r"^\$*\w+\W")' in line:
                fix = True

    if fix == False:

        os.system('cls')
        installation_logo()
        print("Pytube fix...")

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

    else: 
        pass



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
    try:
        # Check if Git is already installed by trying to run it
        subprocess.check_output(["git", "--version"])
        print("Git is already installed.")
    except FileNotFoundError:
        try:
            # Download the Git installer for Windows
            git_installer_url = "https://github.com/git-for-windows/git/releases/latest/download/Git-2.33.0-64-bit.exe"
            git_installer_path = "GitInstaller.exe"
            subprocess.run(["curl", "-Lo", git_installer_path, git_installer_url], shell=True, check=True)

            # Run the Git installer in silent mode
            subprocess.run([git_installer_path, "/SILENT"], shell=True, check=True)

            # Add the Git installation path to PATH
            git_install_dir = os.path.join(os.environ["ProgramFiles(x86)"], "Git", "cmd")
            os.environ["PATH"] += os.pathsep + git_install_dir

            print("Git has been successfully installed.")

        except subprocess.CalledProcessError as err:
            print("Error while installing Git:", err)
        finally:
            # Remove the installer after use
            if os.path.exists(git_installer_path):
                os.remove(git_installer_path)



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