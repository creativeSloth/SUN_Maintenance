from typing import List

from PyQt5.QtWidgets import QDialog

from database.classes.cls_project_data import Addresses, Projects
from styles.styles_Handler import initialize_ui_style
from ui.classes.dlg_address import AddressAttrDialog
from ui.forms.projectattrform import Ui_ProjectAttrDialog
from ui.utils.u_DB_content import conc_DB_table_contents


class ProjectAttrDialog(QDialog):

    def __init__(
        self, session_user_id: int = None, project_id: Projects = None, parent=None
    ):
        from database.queries.q_ref_data import refresh_project_inf

        super().__init__(parent)

        self.ui = Ui_ProjectAttrDialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Projektinformation")
        self.setFixedSize(1200, 600)
        self.mainwindow = parent
        self.session_user_id: int = session_user_id
        self.project_id: int = project_id

        if project_id:
            from database.queries.q_ref_data import get_project_s_infos

            project_inf = get_project_s_infos(projects_id=project_id)[0]
            self.ui.project_no_txt.setText((project_inf.project_no))
            self.ui.project_name_txt.setText((project_inf.project_name))
            self.ui.sys_perf_txt.setText((project_inf.sys_perf))
            self.ui.comission_date_txt.setText((project_inf.comission_date))

            cust_addr: Addresses = project_inf.customer_address
            loc_addr: Addresses = project_inf.loc_address

            self.ui.customer_address_txt.setText(
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
            )
            self.ui.loc_address_txt.setText(
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
            )
        else:
            self.ui.project_no_txt.clear()
            self.ui.project_name_txt.clear()
            self.ui.sys_perf_txt.clear()
            self.ui.comission_date_txt.clear()
            self.ui.customer_address_txt.clear()
            self.ui.loc_address_txt.clear()

            refresh_project_inf(window=self)

        self.map_btns()

        self.ui.buttonBox.accepted.connect(lambda: self.on_accept_btn_click())
        initialize_ui_style(self)

    def map_btns(self):
        self.ui.change_customer_adress_btn.clicked.connect(
            lambda: self.on_change_customer_address_btn_click()
        )
        self.ui.change_customer_adress_btn.clicked.connect(
            lambda: self.on_change_loc_address_btn_click()
        )

    def on_change_customer_address_btn_click(self) -> None:
        from database.queries.q_ref_data import get_address_s_infos, get_project_s_infos

        project_inf = get_project_s_infos(projects_id=self.project_id)[0]
        self.project_inf = project_inf
        if project_inf:
            address_id = getattr(project_inf, "customer_address_id", None)
        else:
            address_id = None

        address_dialog = AddressAttrDialog(
            session_user_id=self.session_user_id,
            address_id=address_id,
            parent=self,
            mode="customer_address",
        )

        if address_dialog.exec_() == QDialog.Accepted:
            # fetching the address information that are being set in the accepted address dialog
            new_address_id = address_dialog.address_id
            new_address_inf = get_address_s_infos(address_id=new_address_id)[0]

            self.ui.customer_address_txt.setText(
                conc_DB_table_contents(
                    columns=[
                        new_address_inf.address_line1,
                        new_address_inf.address_line2,
                        new_address_inf.postal_code,
                        new_address_inf.city,
                        new_address_inf.state,
                        new_address_inf.country,
                    ],
                )
            )

    def on_change_loc_address_btn_click(self) -> None:
        from database.queries.q_ref_data import get_address_s_infos, get_project_s_infos

        project_inf = get_project_s_infos(projects_id=self.project_id)[0]
        self.project_inf = project_inf
        if project_inf:
            address_id = getattr(project_inf, "loc_address_id", None)
        else:
            address_id = None

        address_dialog = AddressAttrDialog(
            session_user_id=self.session_user_id,
            address_id=address_id,
            parent=self,
            mode="loc_address",
        )

        if address_dialog.exec_() == QDialog.Accepted:
            # fetching the address information that are being set in the accepted address dialog
            new_address_id = address_dialog.address_id
            new_address_inf = get_address_s_infos(address_id=new_address_id)[0]

            self.ui.loc_address_txt.setText(
                conc_DB_table_contents(
                    columns=[
                        new_address_inf.address_line1,
                        new_address_inf.address_line2,
                        new_address_inf.postal_code,
                        new_address_inf.city,
                        new_address_inf.state,
                        new_address_inf.country,
                    ],
                )
            )

    def on_accept_btn_click(self):
        from database.queries.q_ref_data import refresh_project_inf

        refresh_project_inf(window=self)

        self.mainwindow.on_menu_projects_btn_click()

        self.accept()
