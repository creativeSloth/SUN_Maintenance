from typing import Dict, List, Tuple

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QTableWidget, QTableWidgetItem, QWidget

from database.classes.cls_article_data import Articles, Manufacturers
from database.classes.cls_project_data import Addresses, Projects
from database.classes.cls_user_role_system import Users
from database.queries.q_ref_data import (
    get_address_s_infos,
    get_articles_infos,
    get_manufacturers_infos,
    get_project_s_infos,
)
from database.queries.q_users import get_usrs_infos
from ui.buttons.create import create_pb
from ui.constants.c_buttons import ADDRESS_TYPES
from ui.tables.decorators import customize_table_row
from ui.utils.u_DB_content import conc_DB_table_contents


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
        "Herst. bearbeiten",
        "Name",
        "Batterien",
        "Module",
        "Wechselrichter",
        "Ladestationen",
        "Komm-Technik",
        "sonstige Produkte",
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
            (
                "Ja"
                if getattr(mf_inf.specialized_fields, "produces_batteries", False)
                else "Nein"
            ),
            (
                "Ja"
                if getattr(mf_inf.specialized_fields, "produces_modules", False)
                else "Nein"
            ),
            (
                "Ja"
                if getattr(mf_inf.specialized_fields, "produces_inverters", False)
                else "Nein"
            ),
            (
                "Ja"
                if getattr(mf_inf.specialized_fields, "produces_chg_points", False)
                else "Nein"
            ),
            (
                "Ja"
                if getattr(mf_inf.specialized_fields, "produces_com_products", False)
                else "Nein"
            ),
            (
                "Ja"
                if getattr(mf_inf.specialized_fields, "produces_misc", False)
                else "Nein"
            ),
        ]

        unpacked_mf_info = dict(zip(headers, values))

        unpacked_mf_infos.append(unpacked_mf_info)

    return unpacked_mf_infos, headers


def get_articles_table_content(self) -> List[Dict]:
    r"""
    Get the content for the QTableWidget.

    :param self: Main window
    :type self: MainWindow
    :return: A list of dictionaries containing the data for the table.
    :rtype: List[Dict]
    """
    articles_infs: List[Articles] = get_articles_infos()

    headers = ["Artikel bearbeiten", "Artikelnummer", "Artikelname", "Hersteller"]
    unpacked_articles_infos = []

    for article_infs in articles_infs:
        pb = create_pb(
            self,
            on_btn_pressed=lambda _, article=article_infs: self.on_article_attr_btn_click(
                article_infs=article
            ),
            btn_type="user_attrs",
            source_obj=article_infs,
        )

        values = [
            pb,
            article_infs.article_no,
            article_infs.article_name,
            article_infs.manufacturer.mf_name,
        ]
        unpacked_article_info = dict(zip(headers, values))

        unpacked_articles_infos.append(unpacked_article_info)

    return unpacked_articles_infos, headers


def get_projects_table_content(self) -> List[Dict]:
    """
    Get the content for the QTableWidget.
    :param self: Main window
    :type self: MainWindow
    :return: A list of dictionaries containing the data for the table.
    :rtype: List[Dict]

    """

    projects_infs: List[Projects] = get_project_s_infos()

    headers = [
        "Projekt bearbeiten",
        "Projektnummer",
        "Projektname",
        "Anlagenleistung",
        "Inbetriebnahmedatum",
        "Betreiber",
        "Standort",
    ]
    unpacked_projects_infos = []
    project_inf: Projects = None
    for project_inf in projects_infs:
        pb = create_pb(
            self,
            on_btn_pressed=lambda _, proj_id=project_inf.id: self.on_project_attr_btn_click(
                project_id=proj_id
            ),
            btn_type="user_attrs",
            source_obj=project_inf,
        )
        cust_addr: Addresses = project_inf.customer_address
        loc_addr: Addresses = project_inf.loc_address

        values = [
            pb,
            project_inf.project_no,
            project_inf.project_name,
            project_inf.sys_perf,
            project_inf.comission_date,
            conc_DB_table_contents(
                columns=[
                    getattr(cust_addr, "address_line1", None),
                    getattr(cust_addr, "address_line2", None),
                    getattr(cust_addr, "postal_code", None),
                    getattr(cust_addr, "city", None),
                    getattr(cust_addr, "state", None),
                    getattr(cust_addr, "country", None),
                ],
            ),
            conc_DB_table_contents(
                columns=[
                    getattr(loc_addr, "address_line1", None),
                    getattr(loc_addr, "address_line2", None),
                    getattr(loc_addr, "postal_code", None),
                    getattr(loc_addr, "city", None),
                    getattr(loc_addr, "state", None),
                    getattr(loc_addr, "country", None),
                ],
            ),
        ]

        unpacked_project_info = dict(zip(headers, values))

        unpacked_projects_infos.append(unpacked_project_info)
    return unpacked_projects_infos, headers


def get_addresses_table_content(self, mode: str = None) -> List[Dict]:
    """
    Get the content for the QTableWidget.
    :param self: Main window
    :type self: MainWindow
    :return: A list of dictionaries containing the data for the table.
    :rtype: List[Dict]
    """
    address_infs: List[Addresses] = get_address_s_infos()
    headers = [
        "Adresse bearbeiten",
        "Name",
        "Strasse und Nr.",
        "Ort",
        "Postleitzahl",
        "Bundesland",
        "Land",
    ]
    unpacked_addresses_infos = []
    address_inf: Addresses = None
    for address_inf in address_infs:
        pb = set_pb_by_mode(self, address_inf.id, mode)
        values = [
            pb,
            address_inf.address_line1,
            address_inf.address_line2,
            address_inf.city,
            address_inf.postal_code,
            address_inf.state,
            address_inf.country,
        ]
        unpacked_address_info = dict(zip(headers, values))
        unpacked_addresses_infos.append(unpacked_address_info)
    return unpacked_addresses_infos, headers


def set_pb_by_mode(self, address_id: int, mode: str = None):

    if mode is None:
        pb = create_pb(
            self,
            on_btn_pressed=lambda _, addr_id=address_id: self.on_address_attr_btn_click(
                address_id=addr_id
            ),
            btn_type="user_attrs",
            source_obj=get_address_s_infos(address_id=address_id)[0],
        )
    elif mode in ADDRESS_TYPES:
        pb = create_pb(
            self,
            on_btn_pressed=lambda _, addr_id=address_id: self.on_transfer_address_btn_click(
                address_id=addr_id
            ),
            btn_type="user_attrs",
            source_obj=get_address_s_infos(address_id=address_id)[0],
        )
    return pb
