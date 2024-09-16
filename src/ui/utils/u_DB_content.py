from typing import List, Type, Union

from PyQt5.QtWidgets import QHBoxLayout, QScrollArea, QVBoxLayout, QWidget

from database.utils.u_db_sess import BASE
from ui.main_body.usr_overview import UserPageItem

"""
    This module contains functions for creating custom widgets from database objects and arranging them in specified layouts.
    The custom widget class should inherit from QWidget and have a constructor that takes a database object as an argument.
    """


def create_widget_from_DB_content(
    DB_objs: List[
        Type[BASE]  # type: ignore
    ],  # List of database objects; the type depends on what you're storing
    custom_widget: Type[QWidget],  # Type of the custom widgets
    layout_type: Type[
        Union[QVBoxLayout, QHBoxLayout]
    ],  # Layout type, either QVBoxLayout or QHBoxLayout
) -> QWidget:
    """
    Creates a custom widget for each database object and arranges them in a specified layout.

    Note: The custom widget class must have a constructor that takes a database object as an argument.

    Example usage:
    db_objs = [User(name="John Doe", email="johndoe@example.com"),...]

    :param DB_objs: A list of database objects to create custom widgets for.
    :type DB_objs: list[Type[BASE]]
    :param custom_widget: The custom widget class to create for each database object.
    :type custom_widget: Type[QWidget]
    :param layout_type: The layout type to use, either QVBoxLayout or QHBoxLayout.
    :type layout_type: Type[Union[QVBoxLayout, QHBoxLayout]]
    :return: A QWidget containing the custom widgets arranged in the specified layout.
    :rtype: QWidget

    """
    layout: Type[Union[QVBoxLayout, QHBoxLayout]] = (
        layout_type()
    )  # Create an instance of the specified layout type
    for DB_obj in DB_objs:
        cstm_widget = custom_widget(DB_obj)  # Create a custom widget for each DB object
        layout.addWidget(cstm_widget)  # Add the custom widget to the layout
        # Create a QWidget to hold the layout
    content_widget: QWidget = QWidget()
    content_widget.setLayout(layout)

    return content_widget


def create_scrollable_content(scrollable_content_widget: QWidget) -> QScrollArea:
    """
    Creates a scrollable content area containing the provided widget.

    :param scrollable_content_widget: The widget to be scrollable.
    :type scrollable_content_widget: QWidget
    :return: A scrollable content area containing the provided widget.
    :rtype: QScrollArea
    """
    scroll_area: QScrollArea = QScrollArea()
    scroll_area.setWidget(scrollable_content_widget)
    scroll_area.setWidgetResizable(True)  # Make the widget resize with the scroll area

    return scroll_area


def create_new_layout_with_content(
    page_widget: QWidget,
    content: QScrollArea,
    layout_type: Type[Union[QVBoxLayout, QHBoxLayout]],
):
    """
    Creates a new layout with the provided scrollable content area and sets it on the provided widget.

    :param page_widget: The widget on which to set the new layout.
    :type page_widget: QWidget
    :param content: The scrollable content area to be added to the new layout.
    :type content: QScrollArea
    :param layout_type: The type of layout to use, either QVBoxLayout or QHBoxLayout.
    :return: None
    :rtype: None
    """
    page_layout: Type[Union[QVBoxLayout, QHBoxLayout]] = layout_type()
    page_layout.addWidget(content)

    # Set the new layout on the page
    page_widget.setLayout(page_layout)


def create_list_into_base_widget(
    base_widget: QWidget,
    layout_type: Type[Union[QVBoxLayout, QHBoxLayout]],
    DB_objs: List[Type[BASE]],  # type: ignore
):
    """
    Creates a custom widget for each database object and arranges them in a specified layout.
    This function assumes that the custom widget class has a constructor that takes a database object as an argument.
    Example usage:
    create_list_into_base_widget(
        base_widget=usr_overview_page,
        layout_type=QVBoxLayout,
        DB_objs=[User(name="John Doe", email="johndoe@example.com"),...],
    )

    :param base_widget: The widget on which to create the custom widget list.
    :type base_widget: QWidget
    :param layout_type: The type of layout to use, either QVBoxLayout or QHBoxLayout.
    :param DB_objs: A list of database objects to create custom widgets for.
    :return: None
    :rtype: None

    """
    content_widget = create_widget_from_DB_content(
        DB_objs=DB_objs, custom_widget=UserPageItem, layout_type=layout_type
    )

    # Create a QScrollArea and set the QWidget as its widget
    scrollable_content: QScrollArea = create_scrollable_content(
        scrollable_content_widget=content_widget
    )

    # Create a new layout for the page and add the QScrollArea to it
    create_new_layout_with_content(
        page_widget=base_widget,
        content=scrollable_content,
        layout_type=QVBoxLayout,
    )


def remove_existing_layouts(widget: QWidget):
    """
    Removes all existing layouts from the provided widget.

    :param widget: The widget from which to remove the existing layouts.
    :type widget: QWidget

    """
    cur_layout = widget.layout()
    if cur_layout:
        # Remove all widgets from the old layout
        while cur_layout.count():
            item = cur_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        # Remove the old layout from the page
        widget.setLayout(None)
