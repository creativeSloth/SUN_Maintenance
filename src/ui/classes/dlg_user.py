from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from database.utils.u_db_sess import BASE
from styles.styles_Handler import initialize_ui_style
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
        from database.queries.q_role_system import get_all_roles

        for role in get_all_roles():
            self.ui.roles_comboBox.addItem(role.role_name)
        usr_role: str = usr_inf.roles[0].role_name
        index = self.ui.roles_comboBox.findText(usr_role)
        if index >= 0:
            self.ui.roles_comboBox.setCurrentIndex(index)

    def on_accept_btn_click(self, usr_inf: type(BASE)):  # type: ignore
        from database.queries.q_users import refresh_usr_inf

        refresh_usr_inf(window=self, usr_inf=usr_inf)
        self.mainwindow.on_menu_usr_overview_btn_click()

        self.accept()
