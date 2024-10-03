from typing import Dict, List, Tuple

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QTableWidget, QTableWidgetItem, QWidget

from database.classes.cls_article_data import Manufacturers
from database.classes.cls_user_role_system import Users
from database.queries.q_manufacturers import get_manufacturers_infos
from database.queries.q_users import get_usrs_infos
from ui.buttons.create import create_pb
from ui.tables.decorators import customize_table_row


@customize_table_row
def fill_table(table: QTableWidget, content: List[Dict], headers: List[str]) -> None:
    r"""
    Fill a QTableWidget with data from a list of dictionaries, ensuring headers are set.

    :param table: The QTableWidget instance.
    :type table: QTableWidget
    :param content: A list of dictionaries containing the data to be displayed in the table.
    :type content: List of dictionaries
    :param headers: A list of headers for the table.
    :type headers: List of strings
    :return: None
    :rtype: None
    """

    table.setRowCount(0)

    # Setze die Anzahl der Spalten und die Header
    table.setColumnCount(len(headers))
    table.setHorizontalHeaderLabels(headers)

    # Füge die Daten nur hinzu, wenn `content` nicht leer ist
    if content:
        for content_itm in content:
            data_row: tuple = tuple(val for val in content_itm.values())
            import_from_df_row(table=table, data_row=data_row)


def get_table_headers(table_widget: QTableWidget) -> List[str]:
    r"""
    Get the horizontal header labels from a QTableWidget instance.

    :param table_widget: The QTableWidget instance.
    :return: A list containing the column names as strings.
    :rtype: List[str]
    """
    # Get the horizontal header labels
    horizontal_header_labels = [
        table_widget.horizontalHeaderItem(i).text()
        for i in range(table_widget.columnCount())
        if table_widget.horizontalHeaderItem(i) is not None
    ]
    return horizontal_header_labels


def import_from_df_row(
    table: QTableWidget,
    data_row: Tuple,
) -> None:
    r"""
    Import data from a tuple (representing a row) into a QTableWidget.

    :param table: The QTableWidget instance.
    :type table: QTableWidget
    :param data_row: A tuple representing a row of data.
    :type data_row: Tuple[Any,...]
    :return: None
    :rtype: None

    """

    column_count: int = len(data_row)
    row = table.rowCount()
    table.insertRow(row)

    for col in range(column_count):
        value = data_row[col]

        if not isinstance(data_row, tuple) and value is None:
            return

        if isinstance(
            value, QWidget
        ):  # Check if the value is a QWidget (e.g. QPushButton)
            # Create a container widget with a layout to center the widget
            container_widget = QWidget()
            layout = QHBoxLayout()
            layout.addWidget(value)
            layout.setAlignment(Qt.AlignCenter)  # Center the widget
            container_widget.setLayout(layout)

            # Set the container widget as the cell widget
            table.setCellWidget(row, col, container_widget)

        else:
            # Otherwise, treat it as a string and set it as an item
            item_col = QTableWidgetItem(str(value))
            table.setItem(row, col, item_col)


def get_usr_table_content(self) -> List[Dict]:
    r"""
    Get the content for the QTableWidget.

    :param self: Main window
    :type self: MainWindow
    :return: A list of dictionaries containing the data from the table.
    :rtype: List[Dict]
    """
    usrs_infs: List[Users] = get_usrs_infos()

    # Definiere die Header nur an einer Stelle
    headers = [
        "Profil bearbeiten",
        "Username",
        "Vorname",
        "Familienname",
        "Rollen",
        "Erstelldatum",
        "Letzter Login",
        "Aktiviert",
    ]

    unpacked_usrs_inf = []
    for usr_inf in usrs_infs:
        pb = create_pb(
            self,
            on_btn_pressed=lambda _, u=usr_inf: self.on_usr_attr_btn_click(usr_inf=u),
            btn_type="user_attrs",
            source_obj=usr_inf,
        )

        # Erstelle die zugehörigen Werte basierend auf den Daten aus usr_inf
        values = [
            pb,
            usr_inf.username,
            usr_inf.user_profile.name,
            usr_inf.user_profile.family_name,
            (
                ", ".join(role.role_name for role in usr_inf.roles)
                if usr_inf.roles
                else "N/A"
            ),
            usr_inf.date_created,
            (
                sorted([itm.login_date for itm in usr_inf.login_dates])[-1]
                if usr_inf.login_dates
                else "N/A"
            ),
            "Ja" if usr_inf.is_enabled else "Nein",
        ]

        # Erstelle das Dictionary dynamisch durch Kombination der Header und Werte
        unpacked_usr_inf = dict(zip(headers, values))

        # Füge das Dictionary zur Liste hinzu
        unpacked_usrs_inf.append(unpacked_usr_inf)

    return unpacked_usrs_inf, headers


def get_manufacturer_table_content(self) -> List[Dict]:
    r"""
    Get the content for the QTableWidget.

    :param self: Main window
    :type self: MainWindow
    :return: A list of dictionaries containing the data for the table.
    :rtype: List[Dict]
    """
    mf_infs: List[Manufacturers] = get_manufacturers_infos()

    headers = [
        "Hersteller bearbeiten",
        "Firmenname",
        "Batteriehersteller.",
        "Modulhersteller",
        "Wechselrichterhersteller",
        "Ladestationshersteller",
        "Komm-Tech-Hersteller",
        "Hersteller sonstiger Produkte",
    ]
    unpacked_mf_infos = []

    for mf_inf in mf_infs:
        pb = create_pb(
            self,
            on_btn_pressed=lambda _, mf=mf_inf: self.on_mf_attr_btn_click(mf_inf=mf),
            btn_type="user_attrs",
            source_obj=mf_inf,
        )

        values = [
            pb,
            mf_inf.mf_name,
            "Ja" if mf_inf.specialized_fields.produces_batteries else "Nein",
            "Ja" if mf_inf.specialized_fields.produces_modules else "Nein",
            "Ja" if mf_inf.specialized_fields.produces_inverters else "Nein",
            "Ja" if mf_inf.specialized_fields.produces_chg_points else "Nein",
            "Ja" if mf_inf.specialized_fields.produces_com_products else "Nein",
            "Ja" if mf_inf.specialized_fields.produces_misc else "Nein",
        ]
        unpacked_mf_info = dict(zip(headers, values))

        unpacked_mf_infos.append(unpacked_mf_info)

    return unpacked_mf_infos, headers
