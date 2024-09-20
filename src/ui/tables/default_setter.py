from PyQt5.QtWidgets import QApplication, QHeaderView, QTableWidget


def resize_columns_to_contents(table: QTableWidget):
    columns = table.columnCount()
    header = table.horizontalHeader()
    for i in range(columns):
        header.setSectionResizeMode(i, QHeaderView.ResizeToContents)

    # Eine Verzögerung einfügen, um sicherzustellen, dass die Größenanpassung abgeschlossen ist
    QApplication.processEvents()
    for i in range(columns):
        header.setSectionResizeMode(i, QHeaderView.Interactive)
