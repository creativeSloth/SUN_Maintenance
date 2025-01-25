# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addressattrform.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_AddressAttrDialog(object):
    def setupUi(self, AddressAttrDialog):
        if not AddressAttrDialog.objectName():
            AddressAttrDialog.setObjectName(u"AddressAttrDialog")
        AddressAttrDialog.resize(1017, 764)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AddressAttrDialog.sizePolicy().hasHeightForWidth())
        AddressAttrDialog.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(AddressAttrDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(AddressAttrDialog)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.search_frame = QFrame(self.frame)
        self.search_frame.setObjectName(u"search_frame")
        sizePolicy1.setHeightForWidth(self.search_frame.sizePolicy().hasHeightForWidth())
        self.search_frame.setSizePolicy(sizePolicy1)
        self.search_frame.setMinimumSize(QSize(0, 0))
        self.search_frame.setFrameShape(QFrame.StyledPanel)
        self.search_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.search_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.addresses_dlg_overview_tbl = QTableWidget(self.search_frame)
        self.addresses_dlg_overview_tbl.setObjectName(u"addresses_dlg_overview_tbl")
        sizePolicy1.setHeightForWidth(self.addresses_dlg_overview_tbl.sizePolicy().hasHeightForWidth())
        self.addresses_dlg_overview_tbl.setSizePolicy(sizePolicy1)
        self.addresses_dlg_overview_tbl.horizontalHeader().setProperty("showSortIndicator", True)
        self.addresses_dlg_overview_tbl.verticalHeader().setVisible(False)
        self.addresses_dlg_overview_tbl.verticalHeader().setHighlightSections(False)

        self.verticalLayout.addWidget(self.addresses_dlg_overview_tbl)


        self.verticalLayout_3.addWidget(self.search_frame)

        self.AdressAttr = QFrame(self.frame)
        self.AdressAttr.setObjectName(u"AdressAttr")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.AdressAttr.sizePolicy().hasHeightForWidth())
        self.AdressAttr.setSizePolicy(sizePolicy2)
        self.AdressAttr.setMinimumSize(QSize(0, 0))
        self.AdressAttr.setMaximumSize(QSize(16777215, 16777215))
        self.AdressAttr.setFrameShape(QFrame.StyledPanel)
        self.AdressAttr.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.AdressAttr)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_3 = QFrame(self.AdressAttr)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setMinimumSize(QSize(0, 40))
        self.frame_2.setMaximumSize(QSize(16777215, 40))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.address_line_1_lbl = QLabel(self.frame_2)
        self.address_line_1_lbl.setObjectName(u"address_line_1_lbl")
        sizePolicy1.setHeightForWidth(self.address_line_1_lbl.sizePolicy().hasHeightForWidth())
        self.address_line_1_lbl.setSizePolicy(sizePolicy1)
        self.address_line_1_lbl.setMinimumSize(QSize(150, 35))
        self.address_line_1_lbl.setMaximumSize(QSize(150, 35))

        self.horizontalLayout.addWidget(self.address_line_1_lbl, 0, Qt.AlignRight)

        self.address_line_1_txt = QLineEdit(self.frame_2)
        self.address_line_1_txt.setObjectName(u"address_line_1_txt")
        sizePolicy1.setHeightForWidth(self.address_line_1_txt.sizePolicy().hasHeightForWidth())
        self.address_line_1_txt.setSizePolicy(sizePolicy1)
        self.address_line_1_txt.setMinimumSize(QSize(300, 35))
        self.address_line_1_txt.setMaximumSize(QSize(300, 35))

        self.horizontalLayout.addWidget(self.address_line_1_txt, 0, Qt.AlignLeft)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy1.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy1)
        self.frame_8.setMinimumSize(QSize(0, 40))
        self.frame_8.setMaximumSize(QSize(16777215, 40))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.address_line_2_lbl = QLabel(self.frame_8)
        self.address_line_2_lbl.setObjectName(u"address_line_2_lbl")
        sizePolicy1.setHeightForWidth(self.address_line_2_lbl.sizePolicy().hasHeightForWidth())
        self.address_line_2_lbl.setSizePolicy(sizePolicy1)
        self.address_line_2_lbl.setMinimumSize(QSize(150, 35))
        self.address_line_2_lbl.setMaximumSize(QSize(150, 35))

        self.horizontalLayout_7.addWidget(self.address_line_2_lbl, 0, Qt.AlignRight)

        self.address_line_2_txt = QLineEdit(self.frame_8)
        self.address_line_2_txt.setObjectName(u"address_line_2_txt")
        sizePolicy1.setHeightForWidth(self.address_line_2_txt.sizePolicy().hasHeightForWidth())
        self.address_line_2_txt.setSizePolicy(sizePolicy1)
        self.address_line_2_txt.setMinimumSize(QSize(300, 35))
        self.address_line_2_txt.setMaximumSize(QSize(300, 35))

        self.horizontalLayout_7.addWidget(self.address_line_2_txt, 0, Qt.AlignLeft)


        self.verticalLayout_4.addWidget(self.frame_8)

        self.frame_10 = QFrame(self.frame_3)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy1.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy1)
        self.frame_10.setMinimumSize(QSize(0, 40))
        self.frame_10.setMaximumSize(QSize(16777215, 40))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.postal_code_lbl = QLabel(self.frame_10)
        self.postal_code_lbl.setObjectName(u"postal_code_lbl")
        sizePolicy1.setHeightForWidth(self.postal_code_lbl.sizePolicy().hasHeightForWidth())
        self.postal_code_lbl.setSizePolicy(sizePolicy1)
        self.postal_code_lbl.setMinimumSize(QSize(150, 35))
        self.postal_code_lbl.setMaximumSize(QSize(150, 35))

        self.horizontalLayout_6.addWidget(self.postal_code_lbl, 0, Qt.AlignRight)

        self.postal_code_txt = QLineEdit(self.frame_10)
        self.postal_code_txt.setObjectName(u"postal_code_txt")
        sizePolicy1.setHeightForWidth(self.postal_code_txt.sizePolicy().hasHeightForWidth())
        self.postal_code_txt.setSizePolicy(sizePolicy1)
        self.postal_code_txt.setMinimumSize(QSize(300, 35))
        self.postal_code_txt.setMaximumSize(QSize(300, 35))

        self.horizontalLayout_6.addWidget(self.postal_code_txt, 0, Qt.AlignLeft)


        self.verticalLayout_4.addWidget(self.frame_10)


        self.horizontalLayout_3.addWidget(self.frame_3, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_4 = QFrame(self.AdressAttr)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy1.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy1)
        self.frame_7.setMinimumSize(QSize(0, 40))
        self.frame_7.setMaximumSize(QSize(16777215, 40))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.city_lbl = QLabel(self.frame_7)
        self.city_lbl.setObjectName(u"city_lbl")
        sizePolicy1.setHeightForWidth(self.city_lbl.sizePolicy().hasHeightForWidth())
        self.city_lbl.setSizePolicy(sizePolicy1)
        self.city_lbl.setMinimumSize(QSize(150, 35))
        self.city_lbl.setMaximumSize(QSize(150, 35))

        self.horizontalLayout_2.addWidget(self.city_lbl, 0, Qt.AlignRight)

        self.city_txt = QLineEdit(self.frame_7)
        self.city_txt.setObjectName(u"city_txt")
        sizePolicy1.setHeightForWidth(self.city_txt.sizePolicy().hasHeightForWidth())
        self.city_txt.setSizePolicy(sizePolicy1)
        self.city_txt.setMinimumSize(QSize(300, 35))
        self.city_txt.setMaximumSize(QSize(300, 35))

        self.horizontalLayout_2.addWidget(self.city_txt, 0, Qt.AlignLeft)


        self.verticalLayout_5.addWidget(self.frame_7)

        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy1.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy1)
        self.frame_9.setMinimumSize(QSize(0, 40))
        self.frame_9.setMaximumSize(QSize(16777215, 40))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.state_lbl = QLabel(self.frame_9)
        self.state_lbl.setObjectName(u"state_lbl")
        sizePolicy1.setHeightForWidth(self.state_lbl.sizePolicy().hasHeightForWidth())
        self.state_lbl.setSizePolicy(sizePolicy1)
        self.state_lbl.setMinimumSize(QSize(150, 35))
        self.state_lbl.setMaximumSize(QSize(150, 35))

        self.horizontalLayout_8.addWidget(self.state_lbl, 0, Qt.AlignRight)

        self.state_txt = QLineEdit(self.frame_9)
        self.state_txt.setObjectName(u"state_txt")
        sizePolicy1.setHeightForWidth(self.state_txt.sizePolicy().hasHeightForWidth())
        self.state_txt.setSizePolicy(sizePolicy1)
        self.state_txt.setMinimumSize(QSize(300, 35))
        self.state_txt.setMaximumSize(QSize(300, 35))

        self.horizontalLayout_8.addWidget(self.state_txt, 0, Qt.AlignLeft)


        self.verticalLayout_5.addWidget(self.frame_9)

        self.frame_11 = QFrame(self.frame_4)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy1.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy1)
        self.frame_11.setMinimumSize(QSize(0, 40))
        self.frame_11.setMaximumSize(QSize(16777215, 40))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.country_lbl = QLabel(self.frame_11)
        self.country_lbl.setObjectName(u"country_lbl")
        sizePolicy1.setHeightForWidth(self.country_lbl.sizePolicy().hasHeightForWidth())
        self.country_lbl.setSizePolicy(sizePolicy1)
        self.country_lbl.setMinimumSize(QSize(150, 35))
        self.country_lbl.setMaximumSize(QSize(150, 35))

        self.horizontalLayout_9.addWidget(self.country_lbl, 0, Qt.AlignRight)

        self.country_txt = QLineEdit(self.frame_11)
        self.country_txt.setObjectName(u"country_txt")
        sizePolicy1.setHeightForWidth(self.country_txt.sizePolicy().hasHeightForWidth())
        self.country_txt.setSizePolicy(sizePolicy1)
        self.country_txt.setMinimumSize(QSize(300, 35))
        self.country_txt.setMaximumSize(QSize(300, 35))

        self.horizontalLayout_9.addWidget(self.country_txt, 0, Qt.AlignLeft)


        self.verticalLayout_5.addWidget(self.frame_11)


        self.horizontalLayout_3.addWidget(self.frame_4)


        self.verticalLayout_3.addWidget(self.AdressAttr, 0, Qt.AlignBottom)


        self.verticalLayout_2.addWidget(self.frame)

        self.buttonBox = QDialogButtonBox(AddressAttrDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(AddressAttrDialog)
        self.buttonBox.accepted.connect(AddressAttrDialog.accept)
        self.buttonBox.rejected.connect(AddressAttrDialog.reject)

        QMetaObject.connectSlotsByName(AddressAttrDialog)
    # setupUi

    def retranslateUi(self, AddressAttrDialog):
        AddressAttrDialog.setWindowTitle(QCoreApplication.translate("AddressAttrDialog", u"Dialog", None))
        self.address_line_1_lbl.setText(QCoreApplication.translate("AddressAttrDialog", u"Name", None))
        self.address_line_2_lbl.setText(QCoreApplication.translate("AddressAttrDialog", u"Stra\u00dfe und Nr.", None))
        self.postal_code_lbl.setText(QCoreApplication.translate("AddressAttrDialog", u"Postleitzahl", None))
        self.city_lbl.setText(QCoreApplication.translate("AddressAttrDialog", u"Ort", None))
        self.state_lbl.setText(QCoreApplication.translate("AddressAttrDialog", u"Bundesland", None))
        self.country_lbl.setText(QCoreApplication.translate("AddressAttrDialog", u"Land", None))
    # retranslateUi

