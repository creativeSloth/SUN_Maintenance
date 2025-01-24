# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'projectattrform.ui'
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
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_ProjectAttrDialog(object):
    def setupUi(self, ProjectAttrDialog):
        if not ProjectAttrDialog.objectName():
            ProjectAttrDialog.setObjectName(u"ProjectAttrDialog")
        ProjectAttrDialog.resize(834, 673)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ProjectAttrDialog.sizePolicy().hasHeightForWidth())
        ProjectAttrDialog.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(ProjectAttrDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ProjectAttr = QFrame(ProjectAttrDialog)
        self.ProjectAttr.setObjectName(u"ProjectAttr")
        sizePolicy.setHeightForWidth(self.ProjectAttr.sizePolicy().hasHeightForWidth())
        self.ProjectAttr.setSizePolicy(sizePolicy)
        self.ProjectAttr.setMinimumSize(QSize(0, 400))
        self.ProjectAttr.setMaximumSize(QSize(16777215, 16777215))
        self.ProjectAttr.setFrameShape(QFrame.StyledPanel)
        self.ProjectAttr.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.ProjectAttr)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.ProjectAttr)
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
        self.project_no_lbl = QLabel(self.frame_2)
        self.project_no_lbl.setObjectName(u"project_no_lbl")
        sizePolicy.setHeightForWidth(self.project_no_lbl.sizePolicy().hasHeightForWidth())
        self.project_no_lbl.setSizePolicy(sizePolicy)
        self.project_no_lbl.setMinimumSize(QSize(150, 35))
        self.project_no_lbl.setMaximumSize(QSize(150, 35))

        self.horizontalLayout.addWidget(self.project_no_lbl, 0, Qt.AlignRight)

        self.project_no_txt = QLineEdit(self.frame_2)
        self.project_no_txt.setObjectName(u"project_no_txt")
        sizePolicy.setHeightForWidth(self.project_no_txt.sizePolicy().hasHeightForWidth())
        self.project_no_txt.setSizePolicy(sizePolicy)
        self.project_no_txt.setMinimumSize(QSize(300, 35))
        self.project_no_txt.setMaximumSize(QSize(300, 35))

        self.horizontalLayout.addWidget(self.project_no_txt, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.frame_2, 0, Qt.AlignHCenter)

        self.frame_4 = QFrame(self.ProjectAttr)
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
        self.project_name_lbl = QLabel(self.frame_4)
        self.project_name_lbl.setObjectName(u"project_name_lbl")
        sizePolicy.setHeightForWidth(self.project_name_lbl.sizePolicy().hasHeightForWidth())
        self.project_name_lbl.setSizePolicy(sizePolicy)
        self.project_name_lbl.setMinimumSize(QSize(150, 35))
        self.project_name_lbl.setMaximumSize(QSize(150, 35))

        self.horizontalLayout_3.addWidget(self.project_name_lbl, 0, Qt.AlignRight)

        self.project_name_txt = QLineEdit(self.frame_4)
        self.project_name_txt.setObjectName(u"project_name_txt")
        sizePolicy.setHeightForWidth(self.project_name_txt.sizePolicy().hasHeightForWidth())
        self.project_name_txt.setSizePolicy(sizePolicy)
        self.project_name_txt.setMinimumSize(QSize(300, 35))
        self.project_name_txt.setMaximumSize(QSize(300, 35))

        self.horizontalLayout_3.addWidget(self.project_name_txt, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.frame_4, 0, Qt.AlignHCenter)

        self.frame_8 = QFrame(self.ProjectAttr)
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
        self.sys_perf_lbl = QLabel(self.frame_8)
        self.sys_perf_lbl.setObjectName(u"sys_perf_lbl")
        sizePolicy.setHeightForWidth(self.sys_perf_lbl.sizePolicy().hasHeightForWidth())
        self.sys_perf_lbl.setSizePolicy(sizePolicy)
        self.sys_perf_lbl.setMinimumSize(QSize(150, 35))
        self.sys_perf_lbl.setMaximumSize(QSize(150, 35))

        self.horizontalLayout_7.addWidget(self.sys_perf_lbl, 0, Qt.AlignRight)

        self.sys_perf_txt = QLineEdit(self.frame_8)
        self.sys_perf_txt.setObjectName(u"sys_perf_txt")
        sizePolicy.setHeightForWidth(self.sys_perf_txt.sizePolicy().hasHeightForWidth())
        self.sys_perf_txt.setSizePolicy(sizePolicy)
        self.sys_perf_txt.setMinimumSize(QSize(300, 35))
        self.sys_perf_txt.setMaximumSize(QSize(300, 35))

        self.horizontalLayout_7.addWidget(self.sys_perf_txt, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.frame_8, 0, Qt.AlignHCenter)

        self.frame_7 = QFrame(self.ProjectAttr)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setMinimumSize(QSize(0, 40))
        self.frame_7.setMaximumSize(QSize(16777215, 40))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.comission_date_lbl = QLabel(self.frame_7)
        self.comission_date_lbl.setObjectName(u"comission_date_lbl")
        sizePolicy.setHeightForWidth(self.comission_date_lbl.sizePolicy().hasHeightForWidth())
        self.comission_date_lbl.setSizePolicy(sizePolicy)
        self.comission_date_lbl.setMinimumSize(QSize(150, 35))
        self.comission_date_lbl.setMaximumSize(QSize(150, 35))

        self.horizontalLayout_4.addWidget(self.comission_date_lbl, 0, Qt.AlignRight)

        self.comission_date_txt = QLineEdit(self.frame_7)
        self.comission_date_txt.setObjectName(u"comission_date_txt")
        sizePolicy.setHeightForWidth(self.comission_date_txt.sizePolicy().hasHeightForWidth())
        self.comission_date_txt.setSizePolicy(sizePolicy)
        self.comission_date_txt.setMinimumSize(QSize(300, 35))
        self.comission_date_txt.setMaximumSize(QSize(300, 35))

        self.horizontalLayout_4.addWidget(self.comission_date_txt, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.frame_7, 0, Qt.AlignHCenter)

        self.frame_10 = QFrame(self.ProjectAttr)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setMinimumSize(QSize(0, 40))
        self.frame_10.setMaximumSize(QSize(16777215, 40))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.customer_address_lbl = QLabel(self.frame_10)
        self.customer_address_lbl.setObjectName(u"customer_address_lbl")
        sizePolicy.setHeightForWidth(self.customer_address_lbl.sizePolicy().hasHeightForWidth())
        self.customer_address_lbl.setSizePolicy(sizePolicy)
        self.customer_address_lbl.setMinimumSize(QSize(150, 35))
        self.customer_address_lbl.setMaximumSize(QSize(150, 35))

        self.horizontalLayout_6.addWidget(self.customer_address_lbl, 0, Qt.AlignRight)

        self.customer_address_txt = QLineEdit(self.frame_10)
        self.customer_address_txt.setObjectName(u"customer_address_txt")
        self.customer_address_txt.setEnabled(False)
        sizePolicy.setHeightForWidth(self.customer_address_txt.sizePolicy().hasHeightForWidth())
        self.customer_address_txt.setSizePolicy(sizePolicy)
        self.customer_address_txt.setMinimumSize(QSize(300, 35))
        self.customer_address_txt.setMaximumSize(QSize(300, 35))
        self.customer_address_txt.setClearButtonEnabled(False)

        self.horizontalLayout_6.addWidget(self.customer_address_txt, 0, Qt.AlignLeft)

        self.change_customer_adress_btn = QPushButton(self.frame_10)
        self.change_customer_adress_btn.setObjectName(u"change_customer_adress_btn")
        sizePolicy.setHeightForWidth(self.change_customer_adress_btn.sizePolicy().hasHeightForWidth())
        self.change_customer_adress_btn.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.change_customer_adress_btn)


        self.verticalLayout.addWidget(self.frame_10, 0, Qt.AlignHCenter)

        self.frame_9 = QFrame(self.ProjectAttr)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setMinimumSize(QSize(0, 40))
        self.frame_9.setMaximumSize(QSize(16777215, 40))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.loc_address_lbl = QLabel(self.frame_9)
        self.loc_address_lbl.setObjectName(u"loc_address_lbl")
        sizePolicy.setHeightForWidth(self.loc_address_lbl.sizePolicy().hasHeightForWidth())
        self.loc_address_lbl.setSizePolicy(sizePolicy)
        self.loc_address_lbl.setMinimumSize(QSize(150, 35))
        self.loc_address_lbl.setMaximumSize(QSize(150, 35))

        self.horizontalLayout_2.addWidget(self.loc_address_lbl)

        self.loc_address_txt = QLineEdit(self.frame_9)
        self.loc_address_txt.setObjectName(u"loc_address_txt")
        self.loc_address_txt.setEnabled(False)
        sizePolicy.setHeightForWidth(self.loc_address_txt.sizePolicy().hasHeightForWidth())
        self.loc_address_txt.setSizePolicy(sizePolicy)
        self.loc_address_txt.setMinimumSize(QSize(300, 35))
        self.loc_address_txt.setMaximumSize(QSize(300, 35))

        self.horizontalLayout_2.addWidget(self.loc_address_txt)

        self.change_loc_adress_btn = QPushButton(self.frame_9)
        self.change_loc_adress_btn.setObjectName(u"change_loc_adress_btn")
        sizePolicy.setHeightForWidth(self.change_loc_adress_btn.sizePolicy().hasHeightForWidth())
        self.change_loc_adress_btn.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.change_loc_adress_btn)


        self.verticalLayout.addWidget(self.frame_9, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.ProjectAttr)

        self.buttonBox = QDialogButtonBox(ProjectAttrDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(ProjectAttrDialog)
        self.buttonBox.accepted.connect(ProjectAttrDialog.accept)
        self.buttonBox.rejected.connect(ProjectAttrDialog.reject)

        QMetaObject.connectSlotsByName(ProjectAttrDialog)
    # setupUi

    def retranslateUi(self, ProjectAttrDialog):
        ProjectAttrDialog.setWindowTitle(QCoreApplication.translate("ProjectAttrDialog", u"Dialog", None))
        self.project_no_lbl.setText(QCoreApplication.translate("ProjectAttrDialog", u"Projektnummer", None))
        self.project_name_lbl.setText(QCoreApplication.translate("ProjectAttrDialog", u"Projektname", None))
        self.sys_perf_lbl.setText(QCoreApplication.translate("ProjectAttrDialog", u"Anlagenleistung", None))
        self.comission_date_lbl.setText(QCoreApplication.translate("ProjectAttrDialog", u"Inbetriebnahmedatum", None))
        self.customer_address_lbl.setText(QCoreApplication.translate("ProjectAttrDialog", u"Betreiber", None))
        self.change_customer_adress_btn.setText(QCoreApplication.translate("ProjectAttrDialog", u"<--", None))
        self.loc_address_lbl.setText(QCoreApplication.translate("ProjectAttrDialog", u"Standort", None))
        self.change_loc_adress_btn.setText(QCoreApplication.translate("ProjectAttrDialog", u"<--", None))
    # retranslateUi

