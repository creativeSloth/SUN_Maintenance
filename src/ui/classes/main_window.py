from typing import List

from PyQt5.QtWidgets import QMainWindow

from database.queries.q_users import get_mapped_usr_infos
from styles.styles_Handler import initialize_ui_style
from ui.constants.c_tables import USR_OVERVIEW_TABL_HEADERS
from ui.forms.mainwindow import Ui_MainWindow
from ui.utils.u_forms import get_widget_index
from ui.utils.u_table_handling import fill_table

# from ui.utils.u_DB_content import create_list_into_base_widget, remove_existing_layouts


class MainWindow(QMainWindow):
    def __init__(self, USER: str = None, parent=None):
        super().__init__(parent)

        # Erstelle eine Instanz der Benutzeroberfläche aus der generierten Ui-Datei
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("SUN Maintenance")
        self.USER = USER
        self.initialize()
        initialize_ui_style(self)

    def initialize(self) -> None:
        """Initializes all components of the form to be working properly.
        Contains severel methods"""
        self.hide_dropdown_menus()
        self.map_btns()

    def hide_dropdown_menus(self) -> None:
        self.ui.usr_dropdown.hide()
        self.ui.ref_dat_dropdown.hide()
        self.ui.service_dropdown.hide()

    def map_btns(self):
        self.ui.menu_usr_btn.clicked.connect(self.on_menu_usr_btn_click)
        self.ui.menu_usr_overview_btn.clicked.connect(
            self.on_menu_usr_overview_btn_click
        )

        self.ui.menu_ref_dat_btn.clicked.connect(self.on_menu_ref_dat_btn_click)
        self.ui.menu_service_btn.clicked.connect(self.on_menu_service_btn_click)

    ########################## USER MENU ###########################
    def on_menu_usr_btn_click(self) -> None:
        if self.ui.usr_dropdown.isHidden():
            self.ui.usr_dropdown.show()
        else:
            self.ui.usr_dropdown.hide()

    def on_menu_usr_overview_btn_click(self) -> None:

        # Get index of needed widget in stacked widget
        index: int = get_widget_index(self.ui.stackedWidget, "usr_overview_page")
        table = self.ui.usr_overview_tbl

        content: List = get_mapped_usr_infos()

        fill_table(table=table, content=content)

        # # Get the page from the StackedWidget
        # usr_overview_page: QWidget = self.ui.stackedWidget.widget(index)
        # If there is an existing layout, remove it
        # remove_existing_layouts(widget=usr_overview_page)
        # create_list_into_base_widget(
        #     base_widget=usr_overview_page, DB_objs=usrs, layout_type=QVBoxLayout
        # )

        # Show the page in the StackedWidget
        self.ui.stackedWidget.setCurrentIndex(index)

    ################################################################
    def on_menu_ref_dat_btn_click(self) -> None:
        if self.ui.ref_dat_dropdown.isHidden():
            self.ui.ref_dat_dropdown.show()
        else:
            self.ui.ref_dat_dropdown.hide()

    def on_menu_service_btn_click(self) -> None:
        if self.ui.service_dropdown.isHidden():
            self.ui.service_dropdown.show()
        else:
            self.ui.service_dropdown.hide()
