# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'manfacattrform.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_ManFacAttrDialog(object):
    def setupUi(self, ManFacAttrDialog):
        if not ManFacAttrDialog.objectName():
            ManFacAttrDialog.setObjectName(u"ManFacAttrDialog")
        ManFacAttrDialog.resize(555, 475)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ManFacAttrDialog.sizePolicy().hasHeightForWidth())
        ManFacAttrDialog.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(ManFacAttrDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ManfacDialog = QFrame(ManFacAttrDialog)
        self.ManfacDialog.setObjectName(u"ManfacDialog")
        sizePolicy.setHeightForWidth(self.ManfacDialog.sizePolicy().hasHeightForWidth())
        self.ManfacDialog.setSizePolicy(sizePolicy)
        self.ManfacDialog.setMinimumSize(QSize(0, 400))
        self.ManfacDialog.setMaximumSize(QSize(16777215, 400))
        self.ManfacDialog.setFrameShape(QFrame.StyledPanel)
        self.ManfacDialog.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.ManfacDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_5 = QFrame(self.ManfacDialog)
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
        self.is_enabled_cbox.setChecked(True)
        self.is_enabled_cbox.setAutoExclusive(False)
        self.is_enabled_cbox.setTristate(False)

        self.horizontalLayout_5.addWidget(self.is_enabled_cbox)


        self.verticalLayout.addWidget(self.frame_5)

        self.frame_2 = QFrame(self.ManfacDialog)
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
        self.manufacturer_name_lbl = QLabel(self.frame_2)
        self.manufacturer_name_lbl.setObjectName(u"manufacturer_name_lbl")
        sizePolicy.setHeightForWidth(self.manufacturer_name_lbl.sizePolicy().hasHeightForWidth())
        self.manufacturer_name_lbl.setSizePolicy(sizePolicy)
        self.manufacturer_name_lbl.setMinimumSize(QSize(100, 35))
        self.manufacturer_name_lbl.setMaximumSize(QSize(100, 35))

        self.horizontalLayout.addWidget(self.manufacturer_name_lbl, 0, Qt.AlignLeft)

        self.manufacturer_name_txt = QLineEdit(self.frame_2)
        self.manufacturer_name_txt.setObjectName(u"manufacturer_name_txt")
        sizePolicy.setHeightForWidth(self.manufacturer_name_txt.sizePolicy().hasHeightForWidth())
        self.manufacturer_name_txt.setSizePolicy(sizePolicy)
        self.manufacturer_name_txt.setMinimumSize(QSize(300, 35))
        self.manufacturer_name_txt.setMaximumSize(QSize(300, 35))

        self.horizontalLayout.addWidget(self.manufacturer_name_txt, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_4 = QFrame(self.ManfacDialog)
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
        self.address_line_1_lbl = QLabel(self.frame_4)
        self.address_line_1_lbl.setObjectName(u"address_line_1_lbl")
        sizePolicy.setHeightForWidth(self.address_line_1_lbl.sizePolicy().hasHeightForWidth())
        self.address_line_1_lbl.setSizePolicy(sizePolicy)
        self.address_line_1_lbl.setMinimumSize(QSize(100, 35))
        self.address_line_1_lbl.setMaximumSize(QSize(100, 35))

        self.horizontalLayout_3.addWidget(self.address_line_1_lbl, 0, Qt.AlignLeft)

        self.address_line_1_txt = QLineEdit(self.frame_4)
        self.address_line_1_txt.setObjectName(u"address_line_1_txt")
        sizePolicy.setHeightForWidth(self.address_line_1_txt.sizePolicy().hasHeightForWidth())
        self.address_line_1_txt.setSizePolicy(sizePolicy)
        self.address_line_1_txt.setMinimumSize(QSize(300, 35))
        self.address_line_1_txt.setMaximumSize(QSize(300, 35))

        self.horizontalLayout_3.addWidget(self.address_line_1_txt, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_8 = QFrame(self.ManfacDialog)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
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
        sizePolicy.setHeightForWidth(self.address_line_2_lbl.sizePolicy().hasHeightForWidth())
        self.address_line_2_lbl.setSizePolicy(sizePolicy)
        self.address_line_2_lbl.setMinimumSize(QSize(100, 35))
        self.address_line_2_lbl.setMaximumSize(QSize(100, 35))

        self.horizontalLayout_7.addWidget(self.address_line_2_lbl, 0, Qt.AlignLeft)

        self.address_line_2_txt = QLineEdit(self.frame_8)
        self.address_line_2_txt.setObjectName(u"address_line_2_txt")
        sizePolicy.setHeightForWidth(self.address_line_2_txt.sizePolicy().hasHeightForWidth())
        self.address_line_2_txt.setSizePolicy(sizePolicy)
        self.address_line_2_txt.setMinimumSize(QSize(300, 35))
        self.address_line_2_txt.setMaximumSize(QSize(300, 35))

        self.horizontalLayout_7.addWidget(self.address_line_2_txt, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.frame_8)

        self.frame_7 = QFrame(self.ManfacDialog)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setMinimumSize(QSize(0, 40))
        self.frame_7.setMaximumSize(QSize(16777215, 40))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.city_lbl = QLabel(self.frame_7)
        self.city_lbl.setObjectName(u"city_lbl")
        sizePolicy.setHeightForWidth(self.city_lbl.sizePolicy().hasHeightForWidth())
        self.city_lbl.setSizePolicy(sizePolicy)
        self.city_lbl.setMinimumSize(QSize(0, 35))
        self.city_lbl.setMaximumSize(QSize(50, 35))

        self.horizontalLayout_4.addWidget(self.city_lbl, 0, Qt.AlignLeft)

        self.city_txt = QLineEdit(self.frame_7)
        self.city_txt.setObjectName(u"city_txt")
        sizePolicy.setHeightForWidth(self.city_txt.sizePolicy().hasHeightForWidth())
        self.city_txt.setSizePolicy(sizePolicy)
        self.city_txt.setMinimumSize(QSize(250, 35))
        self.city_txt.setMaximumSize(QSize(250, 35))

        self.horizontalLayout_4.addWidget(self.city_txt, 0, Qt.AlignLeft)

        self.postal_code_lbl = QLabel(self.frame_7)
        self.postal_code_lbl.setObjectName(u"postal_code_lbl")
        sizePolicy.setHeightForWidth(self.postal_code_lbl.sizePolicy().hasHeightForWidth())
        self.postal_code_lbl.setSizePolicy(sizePolicy)
        self.postal_code_lbl.setMinimumSize(QSize(0, 35))
        self.postal_code_lbl.setMaximumSize(QSize(100, 35))

        self.horizontalLayout_4.addWidget(self.postal_code_lbl, 0, Qt.AlignLeft)

        self.postal_code_txt = QLineEdit(self.frame_7)
        self.postal_code_txt.setObjectName(u"postal_code_txt")
        sizePolicy.setHeightForWidth(self.postal_code_txt.sizePolicy().hasHeightForWidth())
        self.postal_code_txt.setSizePolicy(sizePolicy)
        self.postal_code_txt.setMinimumSize(QSize(100, 35))
        self.postal_code_txt.setMaximumSize(QSize(100, 35))

        self.horizontalLayout_4.addWidget(self.postal_code_txt, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.frame_7)

        self.frame_9 = QFrame(self.ManfacDialog)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setMinimumSize(QSize(0, 40))
        self.frame_9.setMaximumSize(QSize(16777215, 40))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.state_lbl = QLabel(self.frame_9)
        self.state_lbl.setObjectName(u"state_lbl")
        sizePolicy.setHeightForWidth(self.state_lbl.sizePolicy().hasHeightForWidth())
        self.state_lbl.setSizePolicy(sizePolicy)
        self.state_lbl.setMinimumSize(QSize(75, 35))
        self.state_lbl.setMaximumSize(QSize(100, 35))

        self.horizontalLayout_8.addWidget(self.state_lbl, 0, Qt.AlignLeft)

        self.state_txt = QLineEdit(self.frame_9)
        self.state_txt.setObjectName(u"state_txt")
        sizePolicy.setHeightForWidth(self.state_txt.sizePolicy().hasHeightForWidth())
        self.state_txt.setSizePolicy(sizePolicy)
        self.state_txt.setMinimumSize(QSize(150, 35))
        self.state_txt.setMaximumSize(QSize(150, 35))

        self.horizontalLayout_8.addWidget(self.state_txt, 0, Qt.AlignLeft)

        self.country_lbl = QLabel(self.frame_9)
        self.country_lbl.setObjectName(u"country_lbl")
        sizePolicy.setHeightForWidth(self.country_lbl.sizePolicy().hasHeightForWidth())
        self.country_lbl.setSizePolicy(sizePolicy)
        self.country_lbl.setMinimumSize(QSize(75, 35))
        self.country_lbl.setMaximumSize(QSize(100, 35))

        self.horizontalLayout_8.addWidget(self.country_lbl)

        self.country_txt = QLineEdit(self.frame_9)
        self.country_txt.setObjectName(u"country_txt")
        sizePolicy.setHeightForWidth(self.country_txt.sizePolicy().hasHeightForWidth())
        self.country_txt.setSizePolicy(sizePolicy)
        self.country_txt.setMinimumSize(QSize(150, 35))
        self.country_txt.setMaximumSize(QSize(150, 35))

        self.horizontalLayout_8.addWidget(self.country_txt)


        self.verticalLayout.addWidget(self.frame_9)

        self.frame_3 = QFrame(self.ManfacDialog)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.product_types_lbl = QLabel(self.frame_3)
        self.product_types_lbl.setObjectName(u"product_types_lbl")
        sizePolicy.setHeightForWidth(self.product_types_lbl.sizePolicy().hasHeightForWidth())
        self.product_types_lbl.setSizePolicy(sizePolicy)
        self.product_types_lbl.setMinimumSize(QSize(100, 35))
        self.product_types_lbl.setMaximumSize(QSize(100, 35))

        self.horizontalLayout_2.addWidget(self.product_types_lbl)

        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.produces_batteries_cbox = QCheckBox(self.frame)
        self.produces_batteries_cbox.setObjectName(u"produces_batteries_cbox")

        self.gridLayout.addWidget(self.produces_batteries_cbox, 0, 0, 1, 1)

        self.produces_modules_cbox = QCheckBox(self.frame)
        self.produces_modules_cbox.setObjectName(u"produces_modules_cbox")

        self.gridLayout.addWidget(self.produces_modules_cbox, 1, 0, 1, 1)

        self.produces_chg_points_cbox = QCheckBox(self.frame)
        self.produces_chg_points_cbox.setObjectName(u"produces_chg_points_cbox")

        self.gridLayout.addWidget(self.produces_chg_points_cbox, 0, 2, 1, 1)

        self.produces_com_cbox = QCheckBox(self.frame)
        self.produces_com_cbox.setObjectName(u"produces_com_cbox")

        self.gridLayout.addWidget(self.produces_com_cbox, 0, 1, 1, 1)

        self.produces_misc_cbox = QCheckBox(self.frame)
        self.produces_misc_cbox.setObjectName(u"produces_misc_cbox")

        self.gridLayout.addWidget(self.produces_misc_cbox, 1, 1, 1, 1)

        self.produces_inverters_cbox = QCheckBox(self.frame)
        self.produces_inverters_cbox.setObjectName(u"produces_inverters_cbox")

        self.gridLayout.addWidget(self.produces_inverters_cbox, 1, 2, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame)


        self.verticalLayout.addWidget(self.frame_3)


        self.verticalLayout_2.addWidget(self.ManfacDialog)

        self.buttonBox = QDialogButtonBox(ManFacAttrDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(ManFacAttrDialog)
        self.buttonBox.accepted.connect(ManFacAttrDialog.accept)
        self.buttonBox.rejected.connect(ManFacAttrDialog.reject)

        QMetaObject.connectSlotsByName(ManFacAttrDialog)
    # setupUi

    def retranslateUi(self, ManFacAttrDialog):
        ManFacAttrDialog.setWindowTitle(QCoreApplication.translate("ManFacAttrDialog", u"Dialog", None))
        self.is_enabled_cbox.setText(QCoreApplication.translate("ManFacAttrDialog", u"aktiv", None))
        self.manufacturer_name_lbl.setText(QCoreApplication.translate("ManFacAttrDialog", u"Firmenname", None))
        self.address_line_1_lbl.setText(QCoreApplication.translate("ManFacAttrDialog", u"Adressanschrift", None))
        self.address_line_2_lbl.setText(QCoreApplication.translate("ManFacAttrDialog", u"Stra\u00dfe und Nr.", None))
        self.city_lbl.setText(QCoreApplication.translate("ManFacAttrDialog", u"Ort", None))
        self.postal_code_lbl.setText(QCoreApplication.translate("ManFacAttrDialog", u"Postleitzahl", None))
        self.state_lbl.setText(QCoreApplication.translate("ManFacAttrDialog", u"Bundesland", None))
        self.country_lbl.setText(QCoreApplication.translate("ManFacAttrDialog", u"Land", None))
        self.product_types_lbl.setText(QCoreApplication.translate("ManFacAttrDialog", u"Produkttypen", None))
        self.produces_batteries_cbox.setText(QCoreApplication.translate("ManFacAttrDialog", u"Batterien", None))
        self.produces_modules_cbox.setText(QCoreApplication.translate("ManFacAttrDialog", u"Module", None))
        self.produces_chg_points_cbox.setText(QCoreApplication.translate("ManFacAttrDialog", u"Lades\u00e4ulen", None))
        self.produces_com_cbox.setText(QCoreApplication.translate("ManFacAttrDialog", u"Kommunikation", None))
        self.produces_misc_cbox.setText(QCoreApplication.translate("ManFacAttrDialog", u"Sonstige", None))
        self.produces_inverters_cbox.setText(QCoreApplication.translate("ManFacAttrDialog", u"Wechselrichter", None))
    # retranslateUi

