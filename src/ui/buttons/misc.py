import os

from directories.constants.c_directories import DIRS, ICONS_FOLDER


def get_paths_of_icons(icon_name: str = None) -> str:
    icon_folder_path: str = DIRS.paths[ICONS_FOLDER]
    default_color_appendix: str = "_48dp_WHITE.png"

    if icon_name is not None:
        button_icon_path: str = os.path.join(
            icon_folder_path, f"{icon_name}{default_color_appendix}"
        )
        button_icon_path = button_icon_path.replace("\\", "/")
    else:
        button_icon_path = None

    return button_icon_path


def create_button_type_map():
    from ui.buttons.customize import get_color_combo

    return {
        "documents": (get_paths_of_icons("documents"), get_color_combo("gold")),
        "list_remove": (get_paths_of_icons("list_remove"), get_color_combo("red")),
        "list_add": (get_paths_of_icons("list_add"), get_color_combo("green")),
        "search": (get_paths_of_icons("search"), get_color_combo("blue")),
        "preview_off": (get_paths_of_icons("preview_off"), get_color_combo("black")),
        "database": (get_paths_of_icons("database"), get_color_combo("red")),
        "load_files": (
            get_paths_of_icons("home_storage"),
            get_color_combo("red"),
        ),
        "drive_folder": (get_paths_of_icons("drive_folder"), get_color_combo("blue")),
        "user_attrs": (get_paths_of_icons("user_attrs"), get_color_combo("blue")),
    }
