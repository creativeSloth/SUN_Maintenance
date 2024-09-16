from PyQt5.QtWidgets import QHBoxLayout, QLabel, QPushButton, QWidget

from database.classes.cls_users import Users


class UserPageItem(QWidget):
    """
    A widget displaying user information.
    This widget is designed to be used in a list view or similar widget.

    """

    def __init__(self, usr: Users, parent=None):
        super().__init__(parent)

        self.usr: Users = usr

        self.username: str = usr.username
        self.name: str = usr.user_profile.name if usr.user_profile else "N/A"
        self.family_name: str = (
            usr.user_profile.family_name if usr.user_profile else "N/A"
        )

        # Falls es mehrere Rollen gibt, nimm an, dass du die erste Rolle anzeigen möchtest
        self.role = (
            ", ".join(role.role_name for role in usr.roles) if usr.roles else "N/A"
        )
        self.is_enabled = usr.is_enabled

        # Setup GUI
        self.create_usr_page_item()

    def create_usr_page_item(self):
        layout = QHBoxLayout()

        # Add widgets to display user information
        username_label = QLabel(f"Username: {self.username}")
        name_label = QLabel(f"Name: {self.name}")
        family_name_label = QLabel(f"Family Name: {self.family_name}")
        role_label = QLabel(f"Role: {self.role}")
        is_enabled_label = QLabel(f"Enabled: {'Yes' if self.is_enabled else 'No'}")

        layout.addWidget(username_label)
        layout.addWidget(name_label)
        layout.addWidget(family_name_label)
        layout.addWidget(role_label)
        layout.addWidget(is_enabled_label)

        # Add a button for custom functionality
        self.btn_func = QPushButton("Perform Action")
        self.btn_func.clicked.connect(self.on_button_click)
        layout.addWidget(self.btn_func)

        self.setLayout(layout)

    def on_button_click(self):
        # Define the action to perform when the button is clicked
        print(f"Button clicked for user {self.username}")
