from typing import Dict, List, Tuple

from PyQt5.QtWidgets import (
    QCheckBox,
    QHBoxLayout,
    QTableWidget,
    QTableWidgetItem,
    QWidget,
)


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
        data_row: tuple = tuple(val for key, val in content_itm.items())
        print(data_row)
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

    for index in range(column_count):

        if isinstance(data_row, tuple) and data_row[index] is not None:
            item_col = QTableWidgetItem(str(data_row[index]))
            table.setItem(tw_row, index, item_col)
