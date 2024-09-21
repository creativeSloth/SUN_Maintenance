from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from database.queries.q_users import refresh_usr_inf
from database.utils.u_db_sess import BASE
from ui.forms.usrattrform import Ui_UsrAttrDialog


class UserAttrDialog(QDialog):

    def __init__(self, usr_inf: type(BASE) = None, parent=None):  # type: ignore
        super().__init__(parent)

        self.ui = Ui_UsrAttrDialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Benutzerinformation")
        self.setFixedSize(300, 250)
        self.mainwindow = parent

        self.ui.is_enabled_cbox.setCheckState(
            Qt.Checked if usr_inf.is_enabled else Qt.Unchecked
        )
        self.ui.usrname_txt.setText(usr_inf.username)
        self.ui.name_txt.setText(usr_inf.user_profile.name)
        self.ui.family_name_txt.setText(usr_inf.user_profile.family_name)

        self.ui.buttonBox.accepted.connect(
            lambda u=usr_inf: self.on_accept_btn_click(usr_inf=u)
        )

    def on_accept_btn_click(self, usr_inf: type(BASE)):  # type: ignore
        refresh_usr_inf(window=self, usr_inf=usr_inf)

        self.accept()
