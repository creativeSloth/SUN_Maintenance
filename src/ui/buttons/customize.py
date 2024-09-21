from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QIcon, QPainter, QPixmap

from ui.buttons.misc import create_button_type_map


def get_color_combo(buttoncolor=None):
    combos = {
        "blue": {
            "normal": QColor(19, 33, 59, 255),
            "hover": QColor(19, 33, 59, 60),
            "click": QColor(19, 33, 59, 20),
        },
        "red": {
            "normal": QColor(226, 24, 57, 255),
            "hover": QColor(226, 24, 57, 61),
            "click": QColor(226, 24, 57, 20),
        },
        "yellow": {
            "normal": QColor(255, 255, 0, 255),
            "hover": QColor(255, 255, 0, 60),
            "click": QColor(255, 255, 0, 20),
        },
        "green": {
            "normal": QColor(0, 255, 0, 255),
            "hover": QColor(0, 255, 0, 60),
            "click": QColor(0, 255, 0, 20),
        },
        "violet": {
            "normal": QColor(172, 32, 218, 255),
            "hover": QColor(172, 32, 218, 60),
            "click": QColor(172, 32, 218, 20),
        },
        "black": {
            "normal": QColor(0, 0, 0, 255),
            "hover": QColor(0, 0, 0, 60),
            "click": QColor(0, 0, 0, 20),
        },
        "white": {
            "normal": QColor(255, 255, 255, 255),
            "hover": QColor(255, 255, 255, 60),
            "click": QColor(255, 255, 255, 20),
        },
        "gold": {
            "normal": QColor(218, 165, 32, 255),
            "hover": QColor(218, 165, 32, 60),
            "click": QColor(218, 165, 32, 20),
        },
        "orange": {
            "normal": QColor(191, 70, 26, 255),
            "hover": QColor(191, 70, 26, 100),
            "click": QColor(191, 70, 26, 80),
        },
    }
    if buttoncolor is not None and buttoncolor in combos:
        return combos[buttoncolor]


def change_color_of_pixmap(pixmap, new_color):
    # Erstellen eines neuen Pixmap in der gleichen Größe wie das Original
    colored_pixmap = QPixmap(pixmap.size())
    colored_pixmap.fill(Qt.transparent)

    # Verwenden von QPainter, um die Farbe zu ändern
    painter = QPainter(colored_pixmap)
    painter.setCompositionMode(QPainter.CompositionMode_Source)
    painter.drawPixmap(0, 0, pixmap)
    painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
    painter.fillRect(colored_pixmap.rect(), new_color)
    painter.end()

    return colored_pixmap


def customize_dynamic_pb(self, pb):
    BUTTON_TYPE_MAP = create_button_type_map()
    button_type = getattr(pb, "button_type", None)
    if button_type in BUTTON_TYPE_MAP:
        icon_path, color_combo = BUTTON_TYPE_MAP[button_type]
    icon_varieties = create_icon_variaties(icon_path, color_combo)
    set_icon_event_behavior(self, pb, icon_varieties)


def create_icon_variaties(icon_path: str, color_combo):
    original_pixmap = QPixmap(icon_path)
    normal_icon = change_color_of_pixmap(original_pixmap, color_combo["normal"])
    hover_icon = change_color_of_pixmap(original_pixmap, color_combo["hover"])
    click_icon = change_color_of_pixmap(original_pixmap, color_combo["click"])

    return normal_icon, hover_icon, click_icon


def set_icon_event_behavior(self, pb, icon_varieties):
    normal_icon_path, hover_icon_path, click_icon_path = icon_varieties
    pb.setIcon(QIcon(normal_icon_path))
    pb.setIconSize(pb.size())

    # Icons als Button-Attribute speichern
    pb.normal_icon = QIcon(normal_icon_path)
    pb.hover_icon = QIcon(hover_icon_path)
    pb.click_icon = QIcon(click_icon_path)

    # Event-Filter hinzufügen
    pb.installEventFilter(self)
