from ast import Dict
from typing import Dict, List, Tuple

from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QWidget

from database.classes.cls_users import Users
from database.queries.q_users import get_all_usrs_infos
from ui.buttons.create import create_pb
from ui.tables.decorators import customize_table_row


@customize_table_row
def fill_table(table: QTableWidget, content: List[Dict]) -> None:
    """
    Fill a QTableWidget with data from a list of dictionaries.

    :param table: The QTableWidget instance.
    :param content: A list of dictionaries containing the data to be displayed in the table.
    :return: None
    """

    table.setRowCount(0)
    header = [key for key, _ in content[0].items()]
    table.setColumnCount(len(header))
    table.setHorizontalHeaderLabels(header)

    for content_itm in content:
        data_row: tuple = tuple(val for _, val in content_itm.items())
        import_from_df_row(table=table, data_row=data_row)


def get_table_headers(table_widget: QTableWidget) -> List[str]:
    """
    Get the horizontal header labels from a QTableWidget instance.

    :param table_widget: The QTableWidget instance.
    :return: A dictionary containing the column names as keys and their respective indices as values.
    Note: The order of the column names in the returned dictionary matches the order of the columns in the table.
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
    """
    Import data from a tuple (representing a row) into a QTableWidget.

    :param table: The QTableWidget instance.
    :param data_row: A tuple representing a row of data.
    :return: None
    """

    column_count: int = len(data_row)
    tw_row = table.rowCount()
    table.insertRow(tw_row)

    for i in range(column_count):
        value = data_row[i]

        if not isinstance(data_row, tuple) and value is None:
            return

        if isinstance(
            value, QWidget
        ):  # Check if the value is a QWidget (e.g. QPushButton)
            # If it's a widget, set it directly as the cell widget
            table.setCellWidget(tw_row, i, value)
        else:
            # Otherwise, treat it as a string and set it as an item
            item_col = QTableWidgetItem(str(value))
            table.setItem(tw_row, i, item_col)


def get_mapped_usr_infos(self) -> List[Dict]:
    usrs_infs: List[Users] = get_all_usrs_infos()

    unpacked_usrs_inf = []
    for usr_inf in usrs_infs:
        pb = create_pb(self, btn_type="user_attrs", source_obj=usr_inf)
        unpacked_user_info = {
            "Profil bearbeiten": pb,
            "Username": usr_inf.username,
            "Vorname": usr_inf.user_profile.name,
            "Familienname": usr_inf.user_profile.family_name,
            "Rollen": (
                ", ".join(role.role_name for role in usr_inf.roles)
                if usr_inf.roles
                else "N/A"
            ),
            "Erstelldatum": usr_inf.date_created,
            "Letzter Login": (
                sorted([itm.login_date for itm in usr_inf.login_dates])[-1]
                if usr_inf.login_dates
                else "N/A"
            ),
        }

        unpacked_usrs_inf.append(unpacked_user_info)
    return unpacked_usrs_inf
