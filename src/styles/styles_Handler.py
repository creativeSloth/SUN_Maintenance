from directories.constants.c_directories import DIRS
from styles.constants import *


def initialize_ui_style(self) -> None:
    # Pfad zur .qss-Datei
    stylesheet_path = DIRS.paths["stylesheet_path"]

    # Stylesheet aus der Datei einlesen
    with open(stylesheet_path, "r") as qss_file:
        stylesheet = qss_file.read()

    # Platzhalter im Stylesheet durch die entsprechenden Farben ersetzen
    for placeholder, color in STYLE_MAP_6.items():
        stylesheet = stylesheet.replace(placeholder, color)

    # Stylesheet auf das Hauptfenster anwenden
    self.setStyleSheet(stylesheet)
