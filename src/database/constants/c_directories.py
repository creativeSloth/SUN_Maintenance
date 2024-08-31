"""
Name of Software
"""

SOFTWARE_NAME = "SUN_Maintenance"
VERSION = "0.1"

"""
keywords for Directory-Dict-Object
"""
LOG_SUBF = "log_subfolder_path"
LOG_SUBF_2 = "log_subfolder_2_path"
DB = "SUN_DOC_db_path"
STYLESHEET = "stylesheet_path"
ICONS_FOLDER = "icons_folder_path"

"""
Static Directories
"""
# Folder
LOG_SUBF_NAME = "logs"
LOG_SUBF_2_NAME = "hist"
ICONSSUPERF_NAME = "ui"
STYLESHEETF_NAME = "styles"
ICONSF_NAME = "icons"
# Files
DB_NAME = f"{SOFTWARE_NAME}_DB.db"
STYLESHEET_NAME = "stylesheet.qss"
ICON_NAME = "launch.ico"
INCLUDING_PATHS = "paths.txt"
MAIN = "main.py"


class Paths:
    def __init__(self):
        self.paths = {
            LOG_SUBF: "",
            LOG_SUBF_2: "",
            DB: "",
            STYLESHEET: "",
            ICONS_FOLDER: "",
        }

    def set_path(self, key, value):
        if key in self.paths:
            # Umformung des Strings: Alle Backslashes zu Slashes
            self.paths[key] = value.replace("\\", "/")
        else:
            raise KeyError(f"Key '{key}' does not exist in the paths dictionary.")

    def get_path(self, key):
        if key in self.paths:
            return self.paths[key]
        else:
            raise KeyError(f"Key '{key}' does not exist in the paths dictionary.")


DIRS: Paths = Paths()
