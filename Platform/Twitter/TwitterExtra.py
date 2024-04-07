import colorama
import re

def logo():
    print(colorama.Fore.LIGHTBLACK_EX)
    print("  _____        _ _   _           ")
    print(" |_   _|_ __ _(_) |_| |_ ___ _ _ ")      # Category : Featured FIGlet fonts 
    print("   | | \ V  V / |  _|  _/ -_) '_|")      # Font : Small
    print("   |_|  \_/\_/|_|\__|\__\___|_|  ")      # Print : Twitter    
    print("                                 ")



def clean_title(file):

  # Remplacer les espaces par des tirets bas
  filename = file.replace(" ", "_")

  # Supprimer les caractères spéciaux
  filename = re.sub(r"[^\w\d_.]", "", filename)

  # Convertir en minuscules
  filename = filename.lower()

  # Tronquer la longueur du nom de fichier
  if len(filename) > 255:
    filename = filename[:252] + "..."

  return filename