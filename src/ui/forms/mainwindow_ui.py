# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(960, 744)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"AirbusMCDUb"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        MainWindow.setFont(font)
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header_frame = QFrame(self.centralwidget)
        self.header_frame.setObjectName(u"header_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.header_frame.sizePolicy().hasHeightForWidth())
        self.header_frame.setSizePolicy(sizePolicy1)
        self.header_frame.setMinimumSize(QSize(0, 40))
        self.header_frame.setMaximumSize(QSize(16777215, 55))
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_2 = QFrame(self.header_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.dashboard_btn = QPushButton(self.frame_2)
        self.dashboard_btn.setObjectName(u"dashboard_btn")
        self.dashboard_btn.setMinimumSize(QSize(0, 30))
        self.dashboard_btn.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_3.addWidget(self.dashboard_btn)


        self.horizontalLayout_4.addWidget(self.frame_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.frame_7 = QFrame(self.header_frame)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy2)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_7)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.curr_usr_info_btn = QPushButton(self.frame_7)
        self.curr_usr_info_btn.setObjectName(u"curr_usr_info_btn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.curr_usr_info_btn.sizePolicy().hasHeightForWidth())
        self.curr_usr_info_btn.setSizePolicy(sizePolicy3)
        self.curr_usr_info_btn.setMinimumSize(QSize(0, 30))
        self.curr_usr_info_btn.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout.addWidget(self.curr_usr_info_btn)

        self.exit_btn = QPushButton(self.frame_7)
        self.exit_btn.setObjectName(u"exit_btn")
        sizePolicy3.setHeightForWidth(self.exit_btn.sizePolicy().hasHeightForWidth())
        self.exit_btn.setSizePolicy(sizePolicy3)
        self.exit_btn.setMinimumSize(QSize(0, 30))
        self.exit_btn.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout.addWidget(self.exit_btn)


        self.horizontalLayout_4.addWidget(self.frame_7)


        self.verticalLayout.addWidget(self.header_frame)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy4)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.menu_frame_2 = QFrame(self.frame_4)
        self.menu_frame_2.setObjectName(u"menu_frame_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.menu_frame_2.sizePolicy().hasHeightForWidth())
        self.menu_frame_2.setSizePolicy(sizePolicy5)
        self.menu_frame_2.setFrameShape(QFrame.StyledPanel)
        self.menu_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.menu_frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 5, 5, 5)
        self.frame_8 = QFrame(self.menu_frame_2)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy5.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy5)
        self.frame_8.setMinimumSize(QSize(150, 0))
        self.frame_8.setMaximumSize(QSize(16777215, 16777215))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_8)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(9, 5, 9, 5)
        self.menu_service_btn = QPushButton(self.frame_8)
        self.menu_service_btn.setObjectName(u"menu_service_btn")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.menu_service_btn.sizePolicy().hasHeightForWidth())
        self.menu_service_btn.setSizePolicy(sizePolicy6)
        self.menu_service_btn.setMinimumSize(QSize(150, 35))
        self.menu_service_btn.setMaximumSize(QSize(150, 35))

        self.verticalLayout_12.addWidget(self.menu_service_btn, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.service_dropdown = QFrame(self.frame_8)
        self.service_dropdown.setObjectName(u"service_dropdown")
        sizePolicy5.setHeightForWidth(self.service_dropdown.sizePolicy().hasHeightForWidth())
        self.service_dropdown.setSizePolicy(sizePolicy5)
        self.service_dropdown.setFrameShape(QFrame.StyledPanel)
        self.service_dropdown.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.service_dropdown)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 6, 0, 6)
        self.menu_service_maint_btn = QPushButton(self.service_dropdown)
        self.menu_service_maint_btn.setObjectName(u"menu_service_maint_btn")
        self.menu_service_maint_btn.setMinimumSize(QSize(120, 30))
        self.menu_service_maint_btn.setMaximumSize(QSize(120, 30))

        self.verticalLayout_5.addWidget(self.menu_service_maint_btn, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.menu_service_analysis_btn = QPushButton(self.service_dropdown)
        self.menu_service_analysis_btn.setObjectName(u"menu_service_analysis_btn")
        self.menu_service_analysis_btn.setMinimumSize(QSize(120, 30))
        self.menu_service_analysis_btn.setMaximumSize(QSize(120, 30))

        self.verticalLayout_5.addWidget(self.menu_service_analysis_btn, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_12.addWidget(self.service_dropdown, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_3.addWidget(self.frame_8, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_5 = QFrame(self.menu_frame_2)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy7)
        self.frame_5.setMinimumSize(QSize(150, 0))
        self.frame_5.setMaximumSize(QSize(16777215, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, 5, -1, 5)
        self.menu_ref_dat_btn = QPushButton(self.frame_5)
        self.menu_ref_dat_btn.setObjectName(u"menu_ref_dat_btn")
        sizePolicy6.setHeightForWidth(self.menu_ref_dat_btn.sizePolicy().hasHeightForWidth())
        self.menu_ref_dat_btn.setSizePolicy(sizePolicy6)
        self.menu_ref_dat_btn.setMinimumSize(QSize(150, 35))
        self.menu_ref_dat_btn.setMaximumSize(QSize(150, 35))

        self.verticalLayout_10.addWidget(self.menu_ref_dat_btn, 0, Qt.AlignHCenter)

        self.ref_dat_dropdown = QFrame(self.frame_5)
        self.ref_dat_dropdown.setObjectName(u"ref_dat_dropdown")
        sizePolicy5.setHeightForWidth(self.ref_dat_dropdown.sizePolicy().hasHeightForWidth())
        self.ref_dat_dropdown.setSizePolicy(sizePolicy5)
        self.ref_dat_dropdown.setFrameShape(QFrame.StyledPanel)
        self.ref_dat_dropdown.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.ref_dat_dropdown)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 6, 0, 6)
        self.menu_ref_dat_mod_lib_btn = QPushButton(self.ref_dat_dropdown)
        self.menu_ref_dat_mod_lib_btn.setObjectName(u"menu_ref_dat_mod_lib_btn")
        self.menu_ref_dat_mod_lib_btn.setMinimumSize(QSize(120, 30))
        self.menu_ref_dat_mod_lib_btn.setMaximumSize(QSize(120, 30))

        self.verticalLayout_6.addWidget(self.menu_ref_dat_mod_lib_btn, 0, Qt.AlignHCenter)

        self.menu_ref_dat_pv_facs_btn = QPushButton(self.ref_dat_dropdown)
        self.menu_ref_dat_pv_facs_btn.setObjectName(u"menu_ref_dat_pv_facs_btn")
        self.menu_ref_dat_pv_facs_btn.setMinimumSize(QSize(120, 30))
        self.menu_ref_dat_pv_facs_btn.setMaximumSize(QSize(120, 30))

        self.verticalLayout_6.addWidget(self.menu_ref_dat_pv_facs_btn, 0, Qt.AlignHCenter)


        self.verticalLayout_10.addWidget(self.ref_dat_dropdown, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_3.addWidget(self.frame_5, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_3 = QFrame(self.menu_frame_2)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy5.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy5)
        self.frame_3.setMinimumSize(QSize(150, 0))
        self.frame_3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, 5, -1, 5)
        self.menu_usr_btn = QPushButton(self.frame_3)
        self.menu_usr_btn.setObjectName(u"menu_usr_btn")
        sizePolicy6.setHeightForWidth(self.menu_usr_btn.sizePolicy().hasHeightForWidth())
        self.menu_usr_btn.setSizePolicy(sizePolicy6)
        self.menu_usr_btn.setMinimumSize(QSize(150, 35))
        self.menu_usr_btn.setMaximumSize(QSize(150, 35))

        self.verticalLayout_8.addWidget(self.menu_usr_btn, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.usr_dropdown = QFrame(self.frame_3)
        self.usr_dropdown.setObjectName(u"usr_dropdown")
        sizePolicy5.setHeightForWidth(self.usr_dropdown.sizePolicy().hasHeightForWidth())
        self.usr_dropdown.setSizePolicy(sizePolicy5)
        self.usr_dropdown.setFrameShape(QFrame.StyledPanel)
        self.usr_dropdown.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.usr_dropdown)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 6, 0, 6)
        self.menu_usr_overview_btn = QPushButton(self.usr_dropdown)
        self.menu_usr_overview_btn.setObjectName(u"menu_usr_overview_btn")
        self.menu_usr_overview_btn.setMinimumSize(QSize(120, 30))
        self.menu_usr_overview_btn.setMaximumSize(QSize(120, 30))

        self.verticalLayout_4.addWidget(self.menu_usr_overview_btn, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.menu_usr_roles_btn = QPushButton(self.usr_dropdown)
        self.menu_usr_roles_btn.setObjectName(u"menu_usr_roles_btn")
        self.menu_usr_roles_btn.setMinimumSize(QSize(120, 30))
        self.menu_usr_roles_btn.setMaximumSize(QSize(120, 30))

        self.verticalLayout_4.addWidget(self.menu_usr_roles_btn, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.menu_usr_permissions_btn = QPushButton(self.usr_dropdown)
        self.menu_usr_permissions_btn.setObjectName(u"menu_usr_permissions_btn")
        self.menu_usr_permissions_btn.setMinimumSize(QSize(120, 30))
        self.menu_usr_permissions_btn.setMaximumSize(QSize(120, 30))

        self.verticalLayout_4.addWidget(self.menu_usr_permissions_btn, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_8.addWidget(self.usr_dropdown, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_3.addWidget(self.frame_3, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.side_menu_frame = QFrame(self.menu_frame_2)
        self.side_menu_frame.setObjectName(u"side_menu_frame")
        self.side_menu_frame.setFrameShape(QFrame.StyledPanel)
        self.side_menu_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.side_menu_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.side_menu_frame, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_9.addWidget(self.menu_frame_2, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.frame_4)

        self.main_body_frame = QFrame(self.frame)
        self.main_body_frame.setObjectName(u"main_body_frame")
        sizePolicy.setHeightForWidth(self.main_body_frame.sizePolicy().hasHeightForWidth())
        self.main_body_frame.setSizePolicy(sizePolicy)
        self.main_body_frame.setFrameShape(QFrame.StyledPanel)
        self.main_body_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.main_body_frame)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.main_body_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.dashboard = QWidget()
        self.dashboard.setObjectName(u"dashboard")
        self.stackedWidget.addWidget(self.dashboard)
        self.usr_overview_page = QWidget()
        self.usr_overview_page.setObjectName(u"usr_overview_page")
        self.verticalLayout_11 = QVBoxLayout(self.usr_overview_page)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_6 = QFrame(self.usr_overview_page)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_6)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.usr_overview_tbl = QTableWidget(self.frame_6)
        self.usr_overview_tbl.setObjectName(u"usr_overview_tbl")
        self.usr_overview_tbl.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.usr_overview_tbl.setSortingEnabled(True)
        self.usr_overview_tbl.verticalHeader().setVisible(False)

        self.verticalLayout_13.addWidget(self.usr_overview_tbl)


        self.verticalLayout_11.addWidget(self.frame_6)

        self.stackedWidget.addWidget(self.usr_overview_page)
        self.usr_roles_page = QWidget()
        self.usr_roles_page.setObjectName(u"usr_roles_page")
        self.stackedWidget.addWidget(self.usr_roles_page)
        self.usr_permissions_page = QWidget()
        self.usr_permissions_page.setObjectName(u"usr_permissions_page")
        self.stackedWidget.addWidget(self.usr_permissions_page)
        self.ref_dat_mod_lib_page = QWidget()
        self.ref_dat_mod_lib_page.setObjectName(u"ref_dat_mod_lib_page")
        self.stackedWidget.addWidget(self.ref_dat_mod_lib_page)
        self.ref_dat_pv_facs_page = QWidget()
        self.ref_dat_pv_facs_page.setObjectName(u"ref_dat_pv_facs_page")
        self.stackedWidget.addWidget(self.ref_dat_pv_facs_page)
        self.service_maint_page = QWidget()
        self.service_maint_page.setObjectName(u"service_maint_page")
        self.stackedWidget.addWidget(self.service_maint_page)
        self.service_analysis_page = QWidget()
        self.service_analysis_page.setObjectName(u"service_analysis_page")
        self.stackedWidget.addWidget(self.service_analysis_page)

        self.verticalLayout_7.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.main_body_frame)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.dashboard_btn.setText(QCoreApplication.translate("MainWindow", u"DASHBOARD", None))
        self.curr_usr_info_btn.setText(QCoreApplication.translate("MainWindow", u"PROFIL", None))
        self.exit_btn.setText(QCoreApplication.translate("MainWindow", u"EXIT", None))
        self.menu_service_btn.setText(QCoreApplication.translate("MainWindow", u"Service", None))
        self.menu_service_maint_btn.setText(QCoreApplication.translate("MainWindow", u"Wartungen", None))
        self.menu_service_analysis_btn.setText(QCoreApplication.translate("MainWindow", u"Analyse", None))
        self.menu_ref_dat_btn.setText(QCoreApplication.translate("MainWindow", u"Stammdaten", None))
        self.menu_ref_dat_mod_lib_btn.setText(QCoreApplication.translate("MainWindow", u"Module", None))
        self.menu_ref_dat_pv_facs_btn.setText(QCoreApplication.translate("MainWindow", u"Anlagen", None))
        self.menu_usr_btn.setText(QCoreApplication.translate("MainWindow", u"Benutzer", None))
        self.menu_usr_overview_btn.setText(QCoreApplication.translate("MainWindow", u"\u00dcbersicht", None))
        self.menu_usr_roles_btn.setText(QCoreApplication.translate("MainWindow", u"Rollen", None))
        self.menu_usr_permissions_btn.setText(QCoreApplication.translate("MainWindow", u"Rechte", None))
    # retranslateUi

