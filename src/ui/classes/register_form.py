from PyQt5.QtWidgets import QDialog, QLineEdit

from database.queries.q_users import update_db_user
from styles.styles_Handler import initialize_ui_style
from ui.forms.registerform import Ui_RegisterForm
from ui.utils.u_forms import change_text_color, check_form_inputs


class RegisterForm(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Erstelle eine Instanz der Benutzeroberfläche aus der generierten Ui-Datei
        self.ui = Ui_RegisterForm()
        self.ui.setupUi(self)
        self.setWindowTitle("Registrieren")
        self.ui.register_pw_txt.setEchoMode(QLineEdit.Password)
        self.ui.register_rpw_txt.setEchoMode(QLineEdit.Password)

        self.initialize()
        initialize_ui_style(self)

    def initialize(self) -> None:
        """Initializes all components of the form to be working properly.
        Contains severel methods"""
        self.map_btns()

    def map_btns(self):
        self.ui.assign_btn.clicked.connect(self.on_assign_btn_click)

    def on_assign_btn_click(self) -> None:
        name: str = self.ui.register_name_txt.text()
        family_name: str = self.ui.register_family_name_txt.text()
        usr: str = self.ui.register_usr_txt.text()
        pwd: str = self.ui.register_pw_txt.text()
        rpw: str = self.ui.register_rpw_txt.text()

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
