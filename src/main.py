import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from database.classes.cls_users import init_local_db
from directories.directories_handler import set_static_directories
from ui.frm_classes import LoginForm

# Führe das Programm aus, wenn es direkt gestartet wird
if __name__ == "__main__":

    set_static_directories()
    init_local_db()

    app = QApplication(sys.argv)
    login_form: QMainWindow = LoginForm()
    login_form.show()

    sys.exit(app.exec_())
