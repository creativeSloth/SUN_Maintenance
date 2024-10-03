from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from database.classes.cls_user_role_system import Users
from database.utils.u_db_sess import BASE
from styles.styles_Handler import initialize_ui_style
from ui.forms.manfacattrform import Ui_ManFacAttrDialog
from ui.forms.usrattrform import Ui_UsrAttrDialog


class UserAttrDialog(QDialog):

    def __init__(self, usr_inf: type(BASE) = None, parent=None):  # type: ignore
        super().__init__(parent)

        self.ui = Ui_UsrAttrDialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Benutzerinformation")
        self.setFixedSize(500, 550)
        self.mainwindow = parent

        self.ui.is_enabled_cbox.setCheckState(
            Qt.Checked if usr_inf.is_enabled else Qt.Unchecked
        )
        self.ui.usrname_txt.setText(usr_inf.username)
        self.ui.name_txt.setText(usr_inf.user_profile.name)
        self.ui.family_name_txt.setText(usr_inf.user_profile.family_name)

        self.set_roles_combo_box(usr_inf)

        self.ui.buttonBox.accepted.connect(
            lambda u=usr_inf: self.on_accept_btn_click(usr_inf=u)
        )
        initialize_ui_style(self)

    def set_roles_combo_box(self, usr_inf):
        from database.queries.q_roles import get_all_roles

        for role in get_all_roles():
            self.ui.roles_comboBox.addItem(role.role_name)
        usr_role: str = usr_inf.roles[0].role_name
        index = self.ui.roles_comboBox.findText(usr_role)
        if index >= 0:
            self.ui.roles_comboBox.setCurrentIndex(index)

    def on_accept_btn_click(self, usr_inf: type(BASE)):  # type: ignore
        from database.queries.q_users import refresh_usr_inf

        refresh_usr_inf(window=self, usr_inf=usr_inf)

        self.accept()


class ManufacturerAttrDialog(QDialog):

    def __init__(self, session_user_id: int = None, mf_inf: type(BASE) = None, parent=None):  # type: ignore
        super().__init__(parent)

        self.ui = Ui_ManFacAttrDialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Herstellerinformation")
        self.setFixedSize(500, 550)
        self.mainwindow = parent
        self.session_user_id: int = session_user_id

        if mf_inf:
            self.ui.is_enabled_cbox.setCheckState(
                Qt.Checked if mf_inf.is_enabled else Qt.Unchecked
            )
            self.ui.manufacturer_name_txt.setText(mf_inf.mf_name)
            self.ui.address_line_1_txt.setText(mf_inf.address.address_line1)
            self.ui.address_line_2_txt.setText(mf_inf.address.address_line2)
            self.ui.city_txt.setText(mf_inf.address.city)
            self.ui.postal_code_txt.setText(mf_inf.address.postal_code)
            self.ui.state_txt.setText(mf_inf.address.state)
            self.ui.country_txt.setText(mf_inf.address.country)

            self.ui.produces_modules_cbox.setCheckState(
                Qt.Checked
                if mf_inf.specialized_fields.produces_modules
                else Qt.Unchecked
            )
            self.ui.produces_inverters_cbox.setCheckState(
                Qt.Checked
                if mf_inf.specialized_fields.produces_inverters
                else Qt.Unchecked
            )
            self.ui.produces_batteries_cbox.setCheckState(
                Qt.Checked
                if mf_inf.specialized_fields.produces_batteries
                else Qt.Unchecked
            )
            self.ui.produces_chg_points_cbox.setCheckState(
                Qt.Checked
                if mf_inf.specialized_fields.produces_chg_points
                else Qt.Unchecked
            )
            self.ui.produces_com_cbox.setCheckState(
                Qt.Checked
                if mf_inf.specialized_fields.produces_com_products
                else Qt.Unchecked
            )
            self.ui.produces_misc_cbox.setCheckState(
                Qt.Checked if mf_inf.specialized_fields.produces_misc else Qt.Unchecked
            )

        self.ui.buttonBox.accepted.connect(
            lambda mf=mf_inf: self.on_accept_btn_click(mf_inf=mf)
        )
        initialize_ui_style(self)

    def on_accept_btn_click(self, mf_inf: type(BASE)):  # type: ignore
        from database.queries.q_manufacturers import refresh_mf_inf

        refresh_mf_inf(window=self, mf_inf=mf_inf)

        self.accept()
