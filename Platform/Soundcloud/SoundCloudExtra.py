import rich
import re



def logo():
    rich.print("[dark_orange]  ___                   _  ___ _             _ [/dark_orange]")
    rich.print("[dark_orange] / __| ___ _  _ _ _  __| |/ __| |___ _  _ __| |[/dark_orange]")      # Category : Featured FIGlet fonts 
    rich.print("[dark_orange] \__ \/ _ \ || | ' \/ _` | (__| / _ \ || / _` |[/dark_orange]")      # Font : Small
    rich.print("[dark_orange] |___/\___/\_,_|_||_\__,_|\___|_\___/\_,_\__,_|[/dark_orange]")      # Print : SoundCloud     
    rich.print("[dark_orange]                                               [/dark_orange]\n")



def clean_title(song_name):

  # Remplacer les espaces par des tirets bas
  filename = song_name.replace(" ", "_")

  # Supprimer les caractères spéciaux
  filename = re.sub(r"[^\w\d_.]", "", filename)

  # Convertir en minuscules
  filename = filename.lower()

  # Tronquer la longueur du nom de fichier
  if len(filename) > 255:
    filename = filename[:252] + "..."

  return filename