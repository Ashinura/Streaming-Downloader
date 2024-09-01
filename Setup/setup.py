import os
import winreg
import venv

# Venv Name: Str-DL
venv_path = os.path.join(os.path.abspath('../'), '.venv', 'Str-DL')

def create_venv():
    venv.create(venv_path, with_pip=True)
    created_venv = os.path.join(venv_path, "Scripts", "activate.bat")
    print(f"Virtual Env: {created_venv}")
    

def add_to_path(new_path):
    with winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) as root:
        with winreg.OpenKey(root, "Environment", 0, winreg.KEY_ALL_ACCESS) as key:

            existing_path = winreg.QueryValueEx(key, "PATH")[0]
            abspath = new_path

            if new_path not in existing_path:
                new_path = f"{existing_path};{new_path}"
                winreg.SetValueEx(key, "PATH", 0, winreg.REG_EXPAND_SZ, new_path)
                os.environ["PATH"] = new_path
                print(f"{abspath} added to user PATH")

            else:
                print(f"{new_path} is already in PATH.")


def set_path():
    windows_drive = os.environ['SystemDrive'] + "\\" # Add \   →   C:\
    username = os.getlogin()
    ffmpeg_path = os.path.join(windows_drive, "Users", username, ".spotdl")
    venv_lib_path = os.path.join(venv_path, "Lib", "site-packages")
    venv_scripts_path = os.path.join(venv_path, "Scripts")

    if os.path.isdir(ffmpeg_path): add_to_path(ffmpeg_path)
    else : raise FileNotFoundError("Le chemin de FFmpeg n'est pas valide")

    if os.path.isdir(venv_lib_path): add_to_path(venv_lib_path)
    else : raise FileNotFoundError("Le chemin vers l'environnement virtuel n'est pas valide")

    if os.path.isdir(venv_scripts_path): add_to_path(venv_scripts_path)
    else : raise FileNotFoundError("Le chemin vers l'environnement virtuel n'est pas valide")