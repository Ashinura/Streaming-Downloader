import colorama


def logo(music: bool, video: bool, short: bool):
    print(colorama.Fore.LIGHTRED_EX)
    print(" __   __        _        _         ")
    print(" \ \ / ___ _  _| |_ _  _| |__ ___  ")      # Category : Featured FIGlet fonts 
    print("  \ V / _ | || |  _| || | '_ / -_) ")      # Font : Small
    print("   |_|\___/\_,_|\__|\_,_|_.__\___| ")      # Print : Youtube     
    print("                                   ")

    if (music and not video and not short): 
        print("\nMusic                                                                            ")

    elif (video and not music and not short): 
        print("\nVideo                                                                            ")

    elif (short and not music and not video): 
        print("\nShort                                                                            ")

    else: 
        print("                                                                                 ")
    print(colorama.Fore.RESET)