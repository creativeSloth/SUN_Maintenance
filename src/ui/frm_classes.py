from PyQt5.QtWidgets import QDialog, QMainWindow

from database.queries.q_users import update_db_user
from styles.styles_Handler import initialize_ui_style
from ui.forms.loginform import Ui_LoginForm
from ui.forms.registerform import Ui_RegisterForm
from ui.utils.u_forms import change_text_color, check_form_inputs


class LoginForm(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Erstelle eine Instanz der Benutzeroberfläche aus der generierten Ui-Datei
        self.ui = Ui_LoginForm()
        self.ui.setupUi(self)
        self.setWindowTitle("Willkommen")
        self.register_form = None
        self.USER: str = ""
        self.PW: str = ""

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
        usr: str = self.ui.login_usr_txt.toPlainText()
        pw: str = self.ui.login_pw_txt.toPlainText()


class RegisterForm(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Erstelle eine Instanz der Benutzeroberfläche aus der generierten Ui-Datei
        self.ui = Ui_RegisterForm()
        self.ui.setupUi(self)
        self.setWindowTitle("Registrieren")

        self.initialize()
        initialize_ui_style(self)

    def initialize(self) -> None:
        """Initializes all components of the form to be working properly.
        Contains severel methods"""
        self.map_btns()

    def map_btns(self):
        self.ui.assign_btn.clicked.connect(self.on_assign_btn_click)

    def on_assign_btn_click(self) -> None:
        name: str = self.ui.register_name_txt.toPlainText()
        family_name: str = self.ui.register_family_name_txt.toPlainText()
        usr: str = self.ui.register_usr_txt.toPlainText()
        pwd: str = self.ui.register_pw_txt.toPlainText()
        rpw: str = self.ui.register_rpw_txt.toPlainText()

        is_valid = check_form_inputs(
            obj=self.ui.assign_feedback_lbl, usr=usr, pw=pwd, rpw=rpw
        )

        if is_valid == False:
            return

        usr_existed, usr_created = update_db_user(
            usr=usr, pwd=pwd, name=name, family_name=family_name
        )

        if usr_existed:
            self.ui.assign_feedback_lbl.setText("Der Benutzer existiert bereits.")
            change_text_color(label=self.ui.assign_feedback_lbl, color="#ff0000")
            return

        if usr_created:
            self.ui.assign_feedback_lbl.setText(
                "Für den Benutzer wurde erfolgreich ein Account angelegt"
            )
            change_text_color(label=self.ui.assign_feedback_lbl, color="#00ff44")
            return
