from typing import Any, Dict, List

from PyQt5.QtWidgets import QDialog

from database.classes.cls_project_data import Addresses
from ui.classes.app_context import ApplicationContext
from ui.forms.addressattrform import Ui_AddressAttrDialog


class AddressAttrDialog(QDialog):

    def __init__(
        self,
        session_user_id: int = None,
        address_id: int = None,
        parent=None,
        mode: str = None,
    ):

        super().__init__(parent)
        self.ui = Ui_AddressAttrDialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Adresseinformation")
        self.setFixedSize(1200, 800)
        self.session_user_id: int = session_user_id
        self.parent = parent
        self.mainwindow = ApplicationContext().get_main_window()
        self.address_id: int = address_id
        self.mode: str = mode

        from database.queries.q_ref_data import get_address_s_infos

        address_infs = get_address_s_infos(address_id=self.address_id)
        address_inf = address_infs[0] if address_infs else None

        if address_inf:
            self.ui.address_line_1_txt.setText(address_inf.address_line1)
            self.ui.address_line_2_txt.setText(address_inf.address_line2)
            self.ui.postal_code_txt.setText(address_inf.postal_code)
            self.ui.city_txt.setText(address_inf.city)
            self.ui.state_txt.setText(address_inf.state)
            self.ui.country_txt.setText(address_inf.country)
        else:
            self.ui.address_line_1_txt.clear()
            self.ui.address_line_2_txt.clear()
            self.ui.postal_code_txt.clear()
            self.ui.city_txt.clear()
            self.ui.state_txt.clear()
            self.ui.country_txt.clear()
            self.address_id = None

        if mode in ["customer_address", "loc_address"]:
            self.init_overview_table()

        self.ui.buttonBox.accepted.connect(lambda: self.on_accept_btn_click())

    def init_overview_table(self) -> None:
        from ui.tables.content_filler import fill_table, get_addresses_table_content

        table = self.ui.addresses_dlg_overview_tbl
        content: List[Dict[str, Any]]
        headers: List[str]
        content, headers = get_addresses_table_content(self, mode=self.mode)
        fill_table(table=table, content=content, headers=headers)

    def on_transfer_address_btn_click(self, address_id: int) -> None:
        from database.queries.q_ref_data import get_address_s_infos

        address_inf = get_address_s_infos(address_id=address_id)[0]
        self.ui.address_line_1_txt.setText(address_inf.address_line1)
        self.ui.address_line_2_txt.setText(address_inf.address_line2)
        self.ui.postal_code_txt.setText(address_inf.postal_code)
        self.ui.city_txt.setText(address_inf.city)
        self.ui.state_txt.setText(address_inf.state)
        self.ui.country_txt.setText(address_inf.country)
        self.address_id = address_inf.id

    def on_accept_btn_click(self):
        from database.queries.q_ref_data import refresh_address_inf

        refresh_address_inf(window=self)
        if self.mode is None:
            self.mainwindow.on_menu_addresses_btn_click()
        else:
            ...

        self.accept()
