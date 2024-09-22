# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'usrattrform.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_UsrAttrDialog(object):
    def setupUi(self, UsrAttrDialog):
        if not UsrAttrDialog.objectName():
            UsrAttrDialog.setObjectName(u"UsrAttrDialog")
        UsrAttrDialog.resize(500, 474)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(UsrAttrDialog.sizePolicy().hasHeightForWidth())
        UsrAttrDialog.setSizePolicy(sizePolicy)
        UsrAttrDialog.setWindowOpacity(1.000000000000000)
        self.verticalLayout_2 = QVBoxLayout(UsrAttrDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(UsrAttrDialog)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(0, 400))
        self.frame.setMaximumSize(QSize(16777215, 400))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 40))
        self.frame_5.setMaximumSize(QSize(16777215, 40))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.is_enabled_cbox = QCheckBox(self.frame_5)
        self.is_enabled_cbox.setObjectName(u"is_enabled_cbox")
        sizePolicy.setHeightForWidth(self.is_enabled_cbox.sizePolicy().hasHeightForWidth())
        self.is_enabled_cbox.setSizePolicy(sizePolicy)
        self.is_enabled_cbox.setMinimumSize(QSize(0, 35))
        self.is_enabled_cbox.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_5.addWidget(self.is_enabled_cbox)


        self.verticalLayout.addWidget(self.frame_5, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(0, 40))
        self.frame_2.setMaximumSize(QSize(16777215, 40))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.usrname_lbl = QLabel(self.frame_2)
        self.usrname_lbl.setObjectName(u"usrname_lbl")
        sizePolicy.setHeightForWidth(self.usrname_lbl.sizePolicy().hasHeightForWidth())
        self.usrname_lbl.setSizePolicy(sizePolicy)
        self.usrname_lbl.setMinimumSize(QSize(100, 35))
        self.usrname_lbl.setMaximumSize(QSize(100, 35))

        self.horizontalLayout.addWidget(self.usrname_lbl, 0, Qt.AlignLeft)

        self.usrname_txt = QLineEdit(self.frame_2)
        self.usrname_txt.setObjectName(u"usrname_txt")
        sizePolicy.setHeightForWidth(self.usrname_txt.sizePolicy().hasHeightForWidth())
        self.usrname_txt.setSizePolicy(sizePolicy)
        self.usrname_txt.setMinimumSize(QSize(300, 35))
        self.usrname_txt.setMaximumSize(QSize(300, 35))

        self.horizontalLayout.addWidget(self.usrname_txt, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.frame_2, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QSize(0, 40))
        self.frame_3.setMaximumSize(QSize(16777215, 40))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.name_lbl = QLabel(self.frame_3)
        self.name_lbl.setObjectName(u"name_lbl")
        sizePolicy.setHeightForWidth(self.name_lbl.sizePolicy().hasHeightForWidth())
        self.name_lbl.setSizePolicy(sizePolicy)
        self.name_lbl.setMinimumSize(QSize(100, 35))
        self.name_lbl.setMaximumSize(QSize(100, 35))

        self.horizontalLayout_2.addWidget(self.name_lbl, 0, Qt.AlignLeft)

        self.name_txt = QLineEdit(self.frame_3)
        self.name_txt.setObjectName(u"name_txt")
        sizePolicy.setHeightForWidth(self.name_txt.sizePolicy().hasHeightForWidth())
        self.name_txt.setSizePolicy(sizePolicy)
        self.name_txt.setMinimumSize(QSize(300, 35))
        self.name_txt.setMaximumSize(QSize(300, 35))

        self.horizontalLayout_2.addWidget(self.name_txt, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.frame_3, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QSize(0, 40))
        self.frame_4.setMaximumSize(QSize(16777215, 40))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.family_name_lbl = QLabel(self.frame_4)
        self.family_name_lbl.setObjectName(u"family_name_lbl")
        sizePolicy.setHeightForWidth(self.family_name_lbl.sizePolicy().hasHeightForWidth())
        self.family_name_lbl.setSizePolicy(sizePolicy)
        self.family_name_lbl.setMinimumSize(QSize(100, 35))
        self.family_name_lbl.setMaximumSize(QSize(100, 35))

        self.horizontalLayout_3.addWidget(self.family_name_lbl, 0, Qt.AlignLeft)

        self.family_name_txt = QLineEdit(self.frame_4)
        self.family_name_txt.setObjectName(u"family_name_txt")
        sizePolicy.setHeightForWidth(self.family_name_txt.sizePolicy().hasHeightForWidth())
        self.family_name_txt.setSizePolicy(sizePolicy)
        self.family_name_txt.setMinimumSize(QSize(300, 35))
        self.family_name_txt.setMaximumSize(QSize(300, 35))

        self.horizontalLayout_3.addWidget(self.family_name_txt, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.frame_4, 0, Qt.AlignLeft|Qt.AlignTop)

        self.roles_txt = QFrame(self.frame)
        self.roles_txt.setObjectName(u"roles_txt")
        sizePolicy.setHeightForWidth(self.roles_txt.sizePolicy().hasHeightForWidth())
        self.roles_txt.setSizePolicy(sizePolicy)
        self.roles_txt.setMinimumSize(QSize(0, 40))
        self.roles_txt.setMaximumSize(QSize(16777215, 40))
        self.roles_txt.setFrameShape(QFrame.StyledPanel)
        self.roles_txt.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.roles_txt)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.roles_lbl = QLabel(self.roles_txt)
        self.roles_lbl.setObjectName(u"roles_lbl")
        sizePolicy.setHeightForWidth(self.roles_lbl.sizePolicy().hasHeightForWidth())
        self.roles_lbl.setSizePolicy(sizePolicy)
        self.roles_lbl.setMinimumSize(QSize(100, 35))
        self.roles_lbl.setMaximumSize(QSize(100, 35))

        self.horizontalLayout_4.addWidget(self.roles_lbl, 0, Qt.AlignLeft)

        self.roles_comboBox = QComboBox(self.roles_txt)
        self.roles_comboBox.setObjectName(u"roles_comboBox")
        sizePolicy.setHeightForWidth(self.roles_comboBox.sizePolicy().hasHeightForWidth())
        self.roles_comboBox.setSizePolicy(sizePolicy)
        self.roles_comboBox.setMinimumSize(QSize(300, 35))
        self.roles_comboBox.setMaximumSize(QSize(300, 35))
        self.roles_comboBox.setSizeIncrement(QSize(0, 0))

        self.horizontalLayout_4.addWidget(self.roles_comboBox, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.roles_txt, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.buttonBox = QDialogButtonBox(UsrAttrDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox, 0, Qt.AlignLeft)

        QWidget.setTabOrder(self.is_enabled_cbox, self.usrname_txt)
        QWidget.setTabOrder(self.usrname_txt, self.name_txt)
        QWidget.setTabOrder(self.name_txt, self.family_name_txt)
        QWidget.setTabOrder(self.family_name_txt, self.roles_comboBox)

        self.retranslateUi(UsrAttrDialog)
        self.buttonBox.accepted.connect(UsrAttrDialog.accept)
        self.buttonBox.rejected.connect(UsrAttrDialog.reject)

        QMetaObject.connectSlotsByName(UsrAttrDialog)
    # setupUi

    def retranslateUi(self, UsrAttrDialog):
        UsrAttrDialog.setWindowTitle(QCoreApplication.translate("UsrAttrDialog", u"Dialog", None))
        self.is_enabled_cbox.setText(QCoreApplication.translate("UsrAttrDialog", u"aktiv", None))
        self.usrname_lbl.setText(QCoreApplication.translate("UsrAttrDialog", u"Username", None))
        self.name_lbl.setText(QCoreApplication.translate("UsrAttrDialog", u"Vorname", None))
        self.family_name_lbl.setText(QCoreApplication.translate("UsrAttrDialog", u"Nachname", None))
        self.roles_lbl.setText(QCoreApplication.translate("UsrAttrDialog", u"Rolle", None))
    # retranslateUi

