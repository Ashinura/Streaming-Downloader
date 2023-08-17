import colorama



def logo(music: bool, video: bool, short: bool):
    print(colorama.Fore.LIGHTRED_EX)
    print(" __   __        _        _         ")
    print(" \ \ / ___ _  _| |_ _  _| |__ ___  ")      # Category : Featured FIGlet fonts 
    print("  \ V / _ | || |  _| || | '_ / -_) ")      # Font : Small
    print("   |_|\___/\_,_|\__|\_,_|_.__\___| ")      # Print : Youtube     

    if (music and not video and not short): 
        print("\nMusic                                                                            ")

    elif (video and not music and not short): 
        print("\nVideo                                                                            ")

    elif (short and not music and not video): 
        print("\nShort                                                                            ")

    else: 
        print("                                                                                 ")
    print(colorama.Fore.RESET)



def show_progress(stream, chunk, bytes_remaining, new_file):

    total_size = stream._filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100

    progress_bar_length = 20
    progress_bar_filled = int(percentage_of_completion / 100 * progress_bar_length)
    progress_bar = "█" * progress_bar_filled + "░" * (progress_bar_length - progress_bar_filled)
    
    if bytes_remaining == 0:
        print(f"\r{colorama.Fore.LIGHTGREEN_EX}{new_file} has been successfully downloaded.{colorama.Fore.RESET}"+ " " * (progress_bar_length + 8)  )
    else:
        print(f"\r{new_file}   |   {progress_bar} - {percentage_of_completion:.2f}%", end='')


def pytube_fix(): 
    import os
    import site
    import fileinput
    print("YEEEE")

    pytube_folder = site.getusersitepackages() + '/pytube'

    file_to_modify = os.path.join(pytube_folder, 'cipher.py')
    with fileinput.FileInput(file_to_modify, inplace=True) as file:
        for line in file:
            # Effectuer les modifications nécessaires
            new_line = line.replace('var_regex = re.compile(r"^\w+\W")', 'var_regex = re.compile(r"^\$*\w+\W")')
            print(new_line, end='')