# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginform.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        if not LoginForm.objectName():
            LoginForm.setObjectName(u"LoginForm")
        LoginForm.resize(425, 397)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoginForm.sizePolicy().hasHeightForWidth())
        LoginForm.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(LoginForm)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_3 = QFrame(self.frame_4)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.login_usr_lbl = QLabel(self.frame_3)
        self.login_usr_lbl.setObjectName(u"login_usr_lbl")
        self.login_usr_lbl.setEnabled(True)
        sizePolicy.setHeightForWidth(self.login_usr_lbl.sizePolicy().hasHeightForWidth())
        self.login_usr_lbl.setSizePolicy(sizePolicy)
        self.login_usr_lbl.setMinimumSize(QSize(0, 30))
        self.login_usr_lbl.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_2.addWidget(self.login_usr_lbl)

        self.login_usr_txt = QLineEdit(self.frame_3)
        self.login_usr_txt.setObjectName(u"login_usr_txt")
        sizePolicy.setHeightForWidth(self.login_usr_txt.sizePolicy().hasHeightForWidth())
        self.login_usr_txt.setSizePolicy(sizePolicy)
        self.login_usr_txt.setMinimumSize(QSize(0, 30))
        self.login_usr_txt.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_2.addWidget(self.login_usr_txt)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.frame = QFrame(self.frame_4)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.login_pw_lbl = QLabel(self.frame)
        self.login_pw_lbl.setObjectName(u"login_pw_lbl")
        self.login_pw_lbl.setEnabled(True)
        sizePolicy.setHeightForWidth(self.login_pw_lbl.sizePolicy().hasHeightForWidth())
        self.login_pw_lbl.setSizePolicy(sizePolicy)
        self.login_pw_lbl.setMinimumSize(QSize(0, 30))
        self.login_pw_lbl.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout.addWidget(self.login_pw_lbl)

        self.login_pw_txt = QLineEdit(self.frame)
        self.login_pw_txt.setObjectName(u"login_pw_txt")
        sizePolicy.setHeightForWidth(self.login_pw_txt.sizePolicy().hasHeightForWidth())
        self.login_pw_txt.setSizePolicy(sizePolicy)
        self.login_pw_txt.setMinimumSize(QSize(0, 30))
        self.login_pw_txt.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout.addWidget(self.login_pw_txt)


        self.verticalLayout_3.addWidget(self.frame)


        self.verticalLayout_2.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.frame_2)

        self.login_fdb_txt = QLabel(self.centralwidget)
        self.login_fdb_txt.setObjectName(u"login_fdb_txt")
        sizePolicy.setHeightForWidth(self.login_fdb_txt.sizePolicy().hasHeightForWidth())
        self.login_fdb_txt.setSizePolicy(sizePolicy)
        self.login_fdb_txt.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.login_fdb_txt)

        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.login_btn = QPushButton(self.frame_5)
        self.login_btn.setObjectName(u"login_btn")
        sizePolicy.setHeightForWidth(self.login_btn.sizePolicy().hasHeightForWidth())
        self.login_btn.setSizePolicy(sizePolicy)
        self.login_btn.setMinimumSize(QSize(0, 50))
        self.login_btn.setMaximumSize(QSize(150, 50))

        self.verticalLayout_4.addWidget(self.login_btn, 0, Qt.AlignHCenter)

        self.register_btn = QPushButton(self.frame_5)
        self.register_btn.setObjectName(u"register_btn")
        sizePolicy.setHeightForWidth(self.register_btn.sizePolicy().hasHeightForWidth())
        self.register_btn.setSizePolicy(sizePolicy)
        self.register_btn.setMinimumSize(QSize(0, 35))
        self.register_btn.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_4.addWidget(self.register_btn, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.frame_5)

        LoginForm.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.login_usr_txt, self.login_pw_txt)
        QWidget.setTabOrder(self.login_pw_txt, self.register_btn)
        QWidget.setTabOrder(self.register_btn, self.login_btn)

        self.retranslateUi(LoginForm)

        QMetaObject.connectSlotsByName(LoginForm)
    # setupUi

    def retranslateUi(self, LoginForm):
        LoginForm.setWindowTitle(QCoreApplication.translate("LoginForm", u"LoginForm", None))
        self.login_usr_lbl.setText(QCoreApplication.translate("LoginForm", u"Benutzer", None))
        self.login_usr_txt.setPlaceholderText(QCoreApplication.translate("LoginForm", u"Benutzer eingeben...", None))
        self.login_pw_lbl.setText(QCoreApplication.translate("LoginForm", u"Passwort", None))
        self.login_pw_txt.setPlaceholderText(QCoreApplication.translate("LoginForm", u"Passwort eingeben...", None))
        self.login_fdb_txt.setText("")
        self.login_btn.setText(QCoreApplication.translate("LoginForm", u"LOGIN", None))
        self.register_btn.setText(QCoreApplication.translate("LoginForm", u"REGISTRIEREN", None))
    # retranslateUi

