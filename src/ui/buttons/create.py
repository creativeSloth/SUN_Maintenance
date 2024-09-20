from typing import Any

from PyQt5.QtWidgets import QPushButton

from database.utils.u_db_sess import BASE
from ui.buttons.customize import customize_dynamic_pb
from ui.utils.u_obj_handling import create_and_set_obj_property


def create_pb(
    self, btn_type: str = "", on_btn_pressed: Any = None, source_obj: type(BASE) = None  # type: ignore
) -> QPushButton:

    pb: QPushButton = set_pushbutton_for_cell(btn_type, on_btn_pressed, source_obj)
    customize_dynamic_pb(self, pb)
    return pb


def set_pushbutton_for_cell(
    button_type: str, on_btn_pressed: Any, source_obj: type(BASE)  # type: ignore
):

    pb: QPushButton = QPushButton("")
    create_and_set_obj_property(
        obj=pb, property_type="db_source_obj", property_value=source_obj
    )
    create_and_set_obj_property(
        obj=pb, property_type="button_type", property_value=button_type
    )
    pb.setFixedSize(25, 25)
    if on_btn_pressed:
        pb.clicked.connect(lambda _, btn=pb: on_btn_pressed(btn))
    return pb
