# == Imports ==================================================================

import pathlib

# == INFORMATIONS GÉNÉRALES ===================================================

# Nom de la fenêtre du logiciel
NAME_WINDOW: str = "DreamTrad : Patcheur de AI - The Somnium Files"

# Indique si le jeu est une version Steam
IS_STEAM_GAME: bool = True
# Nom du dossier du jeu dans Steam (utilisé uniquement si IS_STEAM_GAME = True)
STEAM_FOLDER: str = "AI The Somnium Files"


# == OUTILS / ENVIRONNEMENT ===================================================

# Dossier où se trouvent les outils cmd (repack, etc.)
TOOL_FOLDER = pathlib.Path("tool")
# Dossier où se trouvent les fichiers patch
PATCH_FOLDER = pathlib.Path("patch")

# == VARIABLES INTERNES (à ne pas modifier manuellement) ======================

# Dossier du jeu, défini dynamiquement à l’exécution
GAME_FOLDER: pathlib.Path = pathlib.Path("")
