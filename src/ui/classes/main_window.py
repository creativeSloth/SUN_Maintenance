from typing import Any, Dict, List

from PyQt5.QtWidgets import QDialog, QMainWindow

from database.classes.cls_user_role_system import Users
from database.utils.u_db_sess import BASE
from styles.styles_Handler import initialize_ui_style
from ui.classes.dialog_forms import ManufacturerAttrDialog, UserAttrDialog
from ui.forms.mainwindow import Ui_MainWindow
from ui.tables.content_filler import (
    fill_table,
    get_manufacturer_table_content,
    get_usr_table_content,
)
from ui.utils.u_forms import get_widget_index

# from ui.utils.u_DB_content import create_list_into_base_widget, remove_existing_layouts


class MainWindow(QMainWindow):
    def __init__(self, session_user_id: int = None, parent=None):
        super().__init__(parent)

        # Erstelle eine Instanz der Benutzeroberfläche aus der generierten Ui-Datei
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("SUN Maintenance")
        self.session_user_id: int = session_user_id

        self.initialize()
        initialize_ui_style(self)

        self.dialog: QDialog = None

    def initialize(self) -> None:
        """Initializes all components of the form to be working properly.
        Contains severel methods"""

        self.hide_dropdown_menus()
        self.map_btns()
        index: int = get_widget_index(self.ui.stackedWidget, "dashboard")
        self.ui.stackedWidget.setCurrentIndex(index)

    def hide_dropdown_menus(self) -> None:
        self.ui.usr_dropdown.hide()
        self.ui.ref_dat_dropdown.hide()
        self.ui.service_dropdown.hide()
        self.ui.articles_dropdown.hide()

    def map_btns(self):
        # USER #
        self.ui.menu_usr_btn.clicked.connect(self.on_menu_usr_btn_click)

        self.ui.menu_usr_overview_btn.clicked.connect(
            self.on_menu_usr_overview_btn_click
        )
        # REF DATA #
        self.ui.menu_ref_dat_btn.clicked.connect(self.on_menu_ref_dat_btn_click)

        self.ui.menu_articles_btn.clicked.connect(self.on_menu_articles_btn_click)
        self.ui.menu_manufacturers_btn.clicked.connect(
            self.on_menu_manufacturers_btn_click
        )
        self.ui.new_manufacturer_btn.clicked.connect(self.on_new_manufacturer_btn_click)

        # SERVICE #
        self.ui.menu_service_btn.clicked.connect(self.on_menu_service_btn_click)

        # MISC #
        self.ui.exit_btn.clicked.connect(self.on_exit_btn_click)

    ########################## USER MENU ###########################
    def on_menu_usr_btn_click(self) -> None:
        if self.ui.usr_dropdown.isHidden():
            self.ui.usr_dropdown.show()
        else:
            self.ui.usr_dropdown.hide()

    def on_menu_usr_overview_btn_click(self) -> None:

        table = self.ui.usr_overview_tbl
        content: List[Dict[str, Any]]
        headers: List[str]
        content, headers = get_usr_table_content(self)
        fill_table(table=table, content=content, headers=headers)

        # Get index of needed widget in stacked widget
        index: int = get_widget_index(self.ui.stackedWidget, "usr_overview_page")
        self.ui.stackedWidget.setCurrentIndex(index)

    def on_usr_attr_btn_click(self, usr_inf: type(BASE)):  # type: ignore
        try:
            usr_attr_dlg: QDialog = UserAttrDialog(usr_inf=usr_inf, parent=self)
            self.dialog = usr_attr_dlg
            self.dialog.exec_()  # Öffnet den Dialog modal
        except Exception as e:
            print(f"Fehler beim Öffnen des Benutzerdialogs: {e}")

    ########################## REF DATA ############################
    def on_menu_ref_dat_btn_click(self) -> None:
        if self.ui.ref_dat_dropdown.isHidden():
            self.ui.ref_dat_dropdown.show()
        else:
            self.ui.ref_dat_dropdown.hide()

    def on_menu_articles_btn_click(self) -> None:
        if self.ui.articles_dropdown.isHidden():
            self.ui.articles_dropdown.show()
        else:
            self.ui.articles_dropdown.hide()

    def on_menu_manufacturers_btn_click(self):
        table = self.ui.manufacturers_overview_tbl
        content: List[Dict[str, Any]]
        headers: List[str]
        content, headers = get_manufacturer_table_content(self)
        fill_table(table=table, content=content, headers=headers)

        # Get index of needed widget in stacked widget
        index: int = get_widget_index(self.ui.stackedWidget, "manufacturers_page")
        self.ui.stackedWidget.setCurrentIndex(index)

    def on_new_manufacturer_btn_click(self):
        try:

            mf_attr_dlg: QDialog = ManufacturerAttrDialog(
                session_user_id=self.session_user_id, parent=self
            )
            self.dialog = mf_attr_dlg
            self.dialog.exec_()  # Öffnet den Dialog modal
        except Exception as e:
            print(f"Fehler beim Öffnen des Herstellerdialogs: {e}")

    def on_mf_attr_btn_click(self, mf_inf: type(BASE)):  # type: ignore
        try:
            mf_attr_dlg: QDialog = ManufacturerAttrDialog(mf_inf=mf_inf, parent=self)
            self.dialog = mf_attr_dlg
            self.dialog.exec_()  # Öffnet den Dialog modal
        except Exception as e:
            print(f"Fehler beim Öffnen des Herstellerdialogs: {e}")

    ########################## SERVICE ############################
    def on_menu_service_btn_click(self) -> None:
        if self.ui.service_dropdown.isHidden():
            self.ui.service_dropdown.show()
        else:
            self.ui.service_dropdown.hide()

    def on_exit_btn_click(self):
        self.close()
