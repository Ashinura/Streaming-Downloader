import colorama
import os
import re
from send2trash import send2trash



def logo(): 
    print(colorama.Fore.LIGHTMAGENTA_EX)
    print("   ___           __ _                    _   _          ")
    print("  / __|___ _ _  / _(_)__ _ _  _ _ _ __ _| |_(_)___ _ _  ")   # Category : Featured FIGlet fonts 
    print(" | (__/ _ \ ' \|  _| / _` | || | '_/ _` |  _| / _ \ ' \ ")   # Font : Small
    print("  \___\___/_||_|_| |_\__, |\_,_|_| \__,_|\__|_\___/_||_|")   # Print : Configuration
    print("                     |___/                              ")
    print(colorama.Fore.RESET)



def clear_folder(folder_path):
    for root, dirs, files in os.walk(folder_path, topdown=False):

        for file in files:
            file_path = os.path.join(root, file)
            send2trash(file_path)

        for dir in dirs:
            dir_path = os.path.join(root, dir)
            send2trash(dir_path)



def is_folder_empty(folder_path):
    return not any(os.scandir(folder_path))