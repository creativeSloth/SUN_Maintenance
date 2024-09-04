# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registerform.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QPlainTextEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_RegisterForm(object):
    def setupUi(self, RegisterForm):
        if not RegisterForm.objectName():
            RegisterForm.setObjectName(u"RegisterForm")
        RegisterForm.resize(500, 383)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RegisterForm.sizePolicy().hasHeightForWidth())
        RegisterForm.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(RegisterForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(RegisterForm)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_8 = QFrame(self.frame_4)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.register_name_lbl = QLabel(self.frame_8)
        self.register_name_lbl.setObjectName(u"register_name_lbl")
        self.register_name_lbl.setEnabled(True)
        sizePolicy.setHeightForWidth(self.register_name_lbl.sizePolicy().hasHeightForWidth())
        self.register_name_lbl.setSizePolicy(sizePolicy)
        self.register_name_lbl.setMinimumSize(QSize(0, 30))
        self.register_name_lbl.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_4.addWidget(self.register_name_lbl)

        self.register_name_txt = QPlainTextEdit(self.frame_8)
        self.register_name_txt.setObjectName(u"register_name_txt")
        self.register_name_txt.setEnabled(True)
        sizePolicy.setHeightForWidth(self.register_name_txt.sizePolicy().hasHeightForWidth())
        self.register_name_txt.setSizePolicy(sizePolicy)
        self.register_name_txt.setMinimumSize(QSize(0, 30))
        self.register_name_txt.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_4.addWidget(self.register_name_txt)


        self.verticalLayout_3.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.register_family_name_lbl = QLabel(self.frame_9)
        self.register_family_name_lbl.setObjectName(u"register_family_name_lbl")
        self.register_family_name_lbl.setEnabled(True)
        sizePolicy.setHeightForWidth(self.register_family_name_lbl.sizePolicy().hasHeightForWidth())
        self.register_family_name_lbl.setSizePolicy(sizePolicy)
        self.register_family_name_lbl.setMinimumSize(QSize(0, 30))
        self.register_family_name_lbl.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_6.addWidget(self.register_family_name_lbl)

        self.register_family_name_txt = QPlainTextEdit(self.frame_9)
        self.register_family_name_txt.setObjectName(u"register_family_name_txt")
        self.register_family_name_txt.setEnabled(True)
        sizePolicy.setHeightForWidth(self.register_family_name_txt.sizePolicy().hasHeightForWidth())
        self.register_family_name_txt.setSizePolicy(sizePolicy)
        self.register_family_name_txt.setMinimumSize(QSize(0, 30))
        self.register_family_name_txt.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_6.addWidget(self.register_family_name_txt)


        self.verticalLayout_3.addWidget(self.frame_9)

        self.frame_3 = QFrame(self.frame_4)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.register_usr_lbl = QLabel(self.frame_3)
        self.register_usr_lbl.setObjectName(u"register_usr_lbl")
        self.register_usr_lbl.setEnabled(True)
        sizePolicy.setHeightForWidth(self.register_usr_lbl.sizePolicy().hasHeightForWidth())
        self.register_usr_lbl.setSizePolicy(sizePolicy)
        self.register_usr_lbl.setMinimumSize(QSize(0, 30))
        self.register_usr_lbl.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_2.addWidget(self.register_usr_lbl)

        self.register_usr_txt = QPlainTextEdit(self.frame_3)
        self.register_usr_txt.setObjectName(u"register_usr_txt")
        self.register_usr_txt.setEnabled(True)
        sizePolicy.setHeightForWidth(self.register_usr_txt.sizePolicy().hasHeightForWidth())
        self.register_usr_txt.setSizePolicy(sizePolicy)
        self.register_usr_txt.setMinimumSize(QSize(0, 30))
        self.register_usr_txt.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_2.addWidget(self.register_usr_txt)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.frame = QFrame(self.frame_4)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.register_pw_lbl = QLabel(self.frame)
        self.register_pw_lbl.setObjectName(u"register_pw_lbl")
        self.register_pw_lbl.setEnabled(True)
        sizePolicy.setHeightForWidth(self.register_pw_lbl.sizePolicy().hasHeightForWidth())
        self.register_pw_lbl.setSizePolicy(sizePolicy)
        self.register_pw_lbl.setMinimumSize(QSize(0, 30))
        self.register_pw_lbl.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout.addWidget(self.register_pw_lbl, 0, Qt.AlignTop)

        self.register_pw_txt = QPlainTextEdit(self.frame)
        self.register_pw_txt.setObjectName(u"register_pw_txt")
        self.register_pw_txt.setEnabled(True)
        sizePolicy.setHeightForWidth(self.register_pw_txt.sizePolicy().hasHeightForWidth())
        self.register_pw_txt.setSizePolicy(sizePolicy)
        self.register_pw_txt.setMinimumSize(QSize(0, 30))
        self.register_pw_txt.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout.addWidget(self.register_pw_txt)


        self.verticalLayout_3.addWidget(self.frame)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.register_rpw_lbl = QLabel(self.frame_6)
        self.register_rpw_lbl.setObjectName(u"register_rpw_lbl")
        self.register_rpw_lbl.setEnabled(True)
        sizePolicy.setHeightForWidth(self.register_rpw_lbl.sizePolicy().hasHeightForWidth())
        self.register_rpw_lbl.setSizePolicy(sizePolicy)
        self.register_rpw_lbl.setMinimumSize(QSize(0, 30))
        self.register_rpw_lbl.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_3.addWidget(self.register_rpw_lbl, 0, Qt.AlignTop)

        self.register_rpw_txt = QPlainTextEdit(self.frame_6)
        self.register_rpw_txt.setObjectName(u"register_rpw_txt")
        self.register_rpw_txt.setEnabled(True)
        sizePolicy.setHeightForWidth(self.register_rpw_txt.sizePolicy().hasHeightForWidth())
        self.register_rpw_txt.setSizePolicy(sizePolicy)
        self.register_rpw_txt.setMinimumSize(QSize(0, 30))
        self.register_rpw_txt.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_3.addWidget(self.register_rpw_txt)


        self.verticalLayout_3.addWidget(self.frame_6)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        self.frame_5.setMinimumSize(QSize(0, 130))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy1.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy1)
        self.frame_7.setMinimumSize(QSize(0, 100))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.assign_feedback_lbl = QLabel(self.frame_7)
        self.assign_feedback_lbl.setObjectName(u"assign_feedback_lbl")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.assign_feedback_lbl.sizePolicy().hasHeightForWidth())
        self.assign_feedback_lbl.setSizePolicy(sizePolicy2)
        self.assign_feedback_lbl.setMinimumSize(QSize(0, 100))
        self.assign_feedback_lbl.setMaximumSize(QSize(16777215, 30))
        self.assign_feedback_lbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_5.addWidget(self.assign_feedback_lbl, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_4.addWidget(self.frame_7, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.assign_btn = QPushButton(self.frame_5)
        self.assign_btn.setObjectName(u"assign_btn")
        sizePolicy.setHeightForWidth(self.assign_btn.sizePolicy().hasHeightForWidth())
        self.assign_btn.setSizePolicy(sizePolicy)
        self.assign_btn.setMinimumSize(QSize(0, 30))
        self.assign_btn.setMaximumSize(QSize(150, 30))

        self.verticalLayout_4.addWidget(self.assign_btn, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.verticalLayout_2.addWidget(self.frame_5, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(RegisterForm)

        QMetaObject.connectSlotsByName(RegisterForm)
    # setupUi

    def retranslateUi(self, RegisterForm):
        RegisterForm.setWindowTitle(QCoreApplication.translate("RegisterForm", u"Dialog", None))
        self.register_name_lbl.setText(QCoreApplication.translate("RegisterForm", u"Vorname", None))
        self.register_family_name_lbl.setText(QCoreApplication.translate("RegisterForm", u"Nachname", None))
        self.register_usr_lbl.setText(QCoreApplication.translate("RegisterForm", u"Benutzer", None))
        self.register_pw_lbl.setText(QCoreApplication.translate("RegisterForm", u"Passwort", None))
        self.register_rpw_lbl.setText(QCoreApplication.translate("RegisterForm", u"Passwort wiederholen", None))
        self.assign_feedback_lbl.setText("")
        self.assign_btn.setText(QCoreApplication.translate("RegisterForm", u"\u00dcbernehmen", None))
    # retranslateUi

