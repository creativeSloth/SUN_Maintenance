from PyQt5.QtWidgets import QDialog, QLineEdit, QMainWindow

from database.classes.cls_user_role_system import Users
from database.queries.q_users import login_user
from styles.styles_Handler import initialize_ui_style
from ui.classes.main_window import MainWindow
from ui.classes.register_form import RegisterForm
from ui.forms.loginform import Ui_LoginForm


class LoginForm(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Erstelle eine Instanz der Benutzeroberfläche aus der generierten Ui-Datei
        self.ui = Ui_LoginForm()
        self.ui.setupUi(self)
        self.setWindowTitle("Willkommen")
        self.main_window = None
        self.register_form = None
        self.PW: str = ""
        self.ui.login_pw_txt.setEchoMode(QLineEdit.Password)

        self.initialize()
        initialize_ui_style(self)

    def initialize(self) -> None:
        """Initializes all components of the form to be working properly.
        Contains severel methods"""
        self.map_btns()

    def map_btns(self):
        self.ui.register_btn.clicked.connect(self.on_register_btn_click)
        self.ui.login_btn.clicked.connect(self.on_login_btn_click)

    def on_register_btn_click(self) -> None:
        self.register_form: QDialog = RegisterForm()
        self.register_form.show()

    def on_login_btn_click(self) -> None:
        usr: str = self.ui.login_usr_txt.text()
        pwd: str = self.ui.login_pw_txt.text()

        # Prüfen ob Benutzername und Passwort gültig sind und bei Erfolg einloggen
        user_existed, pwd_verified, usr_id = login_user(usr=usr, pwd=pwd)
        if user_existed and pwd_verified:

            self.main_window: QMainWindow = MainWindow(session_user_id=usr_id)
            self.main_window.showMaximized()
            self.close()
            if getattr(self, "register_form", None):
                self.register_form.close()

        if not user_existed:
            self.ui.login_fdb_txt.setText("Benutzer existiert nicht")
            self.ui.login_usr_txt.setText("")
            self.ui.login_pw_txt.setText("")
        if user_existed and not pwd_verified:
            self.ui.login_fdb_txt.setText("Passwort ist falsch")
            self.ui.login_pw_txt.setText("")
