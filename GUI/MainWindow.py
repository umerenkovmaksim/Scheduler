# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow - untitledMJZmgD.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(619, 410)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(9998798, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.main_header = QFrame(self.centralwidget)
        self.main_header.setObjectName(u"main_header")
        self.main_header.setMinimumSize(QSize(0, 35))
        self.main_header.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(215, 215, 215);\n"
"}")
        self.main_header.setFrameShape(QFrame.StyledPanel)
        self.main_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.main_header)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.main_header)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(150, 0))
        self.frame.setMaximumSize(QSize(75, 16777215))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.left_menu_btn = QPushButton(self.frame)
        self.left_menu_btn.setObjectName(u"left_menu_btn")
        self.left_menu_btn.setMinimumSize(QSize(0, 30))
        self.left_menu_btn.setStyleSheet(u"QPushButton {\n"
"	background-repeat: none;\n"
"	border: none;\n"
"	background-color: rgb(215, 215, 215);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(215, 255, 255);\n"
"border-radius: 5px;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/align-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.left_menu_btn.setIcon(icon)
        self.left_menu_btn.setIconSize(QSize(24, 24))
        self.left_menu_btn.setFlat(False)

        self.horizontalLayout_2.addWidget(self.left_menu_btn)

        self.home_btn = QPushButton(self.frame)
        self.home_btn.setObjectName(u"home_btn")
        self.home_btn.setMinimumSize(QSize(0, 30))
        self.home_btn.setStyleSheet(u"QPushButton {\n"
"	background-repeat: none;\n"
"	border: none;\n"
"	background-color: rgb(215, 215, 215);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(215, 255, 255);\n"
"	border-radius: 5px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.home_btn.setIcon(icon1)
        self.home_btn.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.home_btn)

        self.create_task_btn = QPushButton(self.frame)
        self.create_task_btn.setObjectName(u"create_task_btn")
        self.create_task_btn.setMinimumSize(QSize(0, 30))
        self.create_task_btn.setMaximumSize(QSize(300, 16777215))
        font = QFont()
        font.setPointSize(14)
        self.create_task_btn.setFont(font)
        self.create_task_btn.setStyleSheet(u"QPushButton {\n"
"	background-repeat: none;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(215, 255, 255);\n"
"	border-radius: 5px;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/plus-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.create_task_btn.setIcon(icon2)
        self.create_task_btn.setIconSize(QSize(24, 24))
        self.create_task_btn.setFlat(False)

        self.horizontalLayout_2.addWidget(self.create_task_btn)


        self.horizontalLayout.addWidget(self.frame)

        self.top_bar = QFrame(self.main_header)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setFrameShape(QFrame.StyledPanel)
        self.top_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.top_bar)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.move_window_bar = QFrame(self.top_bar)
        self.move_window_bar.setObjectName(u"move_window_bar")
        self.move_window_bar.setFrameShape(QFrame.StyledPanel)
        self.move_window_bar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.move_window_bar)

        self.actions_bar = QFrame(self.top_bar)
        self.actions_bar.setObjectName(u"actions_bar")
        self.actions_bar.setMaximumSize(QSize(150, 16777215))
        self.actions_bar.setFrameShape(QFrame.StyledPanel)
        self.actions_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.actions_bar)
        self.horizontalLayout_4.setSpacing(8)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.hide_btn = QPushButton(self.actions_bar)
        self.hide_btn.setObjectName(u"hide_btn")
        self.hide_btn.setMinimumSize(QSize(0, 30))
        self.hide_btn.setStyleSheet(u"QPushButton {\n"
"	background-repeat: none;\n"
"	border: none;\n"
"	background-color: rgb(215, 215, 215);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(215, 255, 255);\n"
"	border-radius: 5px;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.hide_btn.setIcon(icon3)

        self.horizontalLayout_4.addWidget(self.hide_btn)

        self.expand_btn = QPushButton(self.actions_bar)
        self.expand_btn.setObjectName(u"expand_btn")
        self.expand_btn.setMinimumSize(QSize(0, 30))
        self.expand_btn.setStyleSheet(u"QPushButton {\n"
"	background-repeat: none;\n"
"	border: none;\n"
"	background-color: rgb(215, 215, 215);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(215, 255, 255);\n"
"	border-radius: 5px;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/maximize-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.expand_btn.setIcon(icon4)

        self.horizontalLayout_4.addWidget(self.expand_btn)

        self.close_btn = QPushButton(self.actions_bar)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMinimumSize(QSize(0, 30))
        self.close_btn.setStyleSheet(u"QPushButton {\n"
"	background-repeat: none;\n"
"	border: none;\n"
"	background-color: rgb(215, 215, 215);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(215, 255, 255);\n"
"	border-radius: 5px;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn.setIcon(icon5)

        self.horizontalLayout_4.addWidget(self.close_btn)


        self.horizontalLayout_3.addWidget(self.actions_bar)


        self.horizontalLayout.addWidget(self.top_bar)


        self.gridLayout.addWidget(self.main_header, 0, 0, 1, 2)

        self.bottom_bar = QFrame(self.centralwidget)
        self.bottom_bar.setObjectName(u"bottom_bar")
        self.bottom_bar.setMinimumSize(QSize(0, 25))
        self.bottom_bar.setMaximumSize(QSize(16777215, 16777215))
        self.bottom_bar.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(215, 215, 215);\n"
"}")
        self.bottom_bar.setFrameShape(QFrame.StyledPanel)
        self.bottom_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.bottom_bar)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.status_bar = QFrame(self.bottom_bar)
        self.status_bar.setObjectName(u"status_bar")
        self.status_bar.setFrameShape(QFrame.StyledPanel)
        self.status_bar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.status_bar)

        self.size_grip = QFrame(self.bottom_bar)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMaximumSize(QSize(20, 16777215))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.size_grip)


        self.gridLayout.addWidget(self.bottom_bar, 3, 0, 1, 2)

        self.left_menu = QFrame(self.centralwidget)
        self.left_menu.setObjectName(u"left_menu")
        self.left_menu.setMinimumSize(QSize(0, 0))
        self.left_menu.setMaximumSize(QSize(0, 16777215))
        self.left_menu.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(215, 215, 215);\n"
"}")
        self.left_menu.setFrameShape(QFrame.StyledPanel)
        self.left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.left_menu)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 5, 0, 5)
        self.calendar_btn = QPushButton(self.left_menu)
        self.calendar_btn.setObjectName(u"calendar_btn")
        self.calendar_btn.setMinimumSize(QSize(0, 30))
        self.calendar_btn.setFont(font)
        self.calendar_btn.setStyleSheet(u"QPushButton {\n"
"	background-repeat: none;\n"
"	border: none;\n"
"	background-color: rgb(215, 215, 215);\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(215, 255, 255);\n"
"	border-radius: 5px;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/calendar.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.calendar_btn.setIcon(icon6)
        self.calendar_btn.setIconSize(QSize(24, 24))
        self.calendar_btn.setFlat(False)

        self.verticalLayout.addWidget(self.calendar_btn)

        self.all_tasks_btn = QPushButton(self.left_menu)
        self.all_tasks_btn.setObjectName(u"all_tasks_btn")
        self.all_tasks_btn.setMinimumSize(QSize(0, 30))
        self.all_tasks_btn.setFont(font)
        self.all_tasks_btn.setStyleSheet(u"QPushButton {\n"
"	background-repeat: none;\n"
"	border: none;\n"
"	background-color: rgb(215, 215, 215);\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(215, 255, 255);\n"
"	border-radius: 5px;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/clipboard.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.all_tasks_btn.setIcon(icon7)
        self.all_tasks_btn.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.all_tasks_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.settings_btn = QPushButton(self.left_menu)
        self.settings_btn.setObjectName(u"settings_btn")
        self.settings_btn.setMinimumSize(QSize(0, 30))
        self.settings_btn.setFont(font)
        self.settings_btn.setStyleSheet(u"QPushButton {\n"
"	background-repeat: none;\n"
"	border: none;\n"
"	background-color: rgb(215, 215, 215);\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(215, 255, 255);\n"
"	border-radius: 5px;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_btn.setIcon(icon8)
        self.settings_btn.setIconSize(QSize(24, 24))
        self.settings_btn.setFlat(False)

        self.verticalLayout.addWidget(self.settings_btn)


        self.gridLayout.addWidget(self.left_menu, 2, 0, 1, 1)

        self.main_body = QFrame(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.main_body)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setContentsMargins(6, 6, 6, 6)
        self.create_menu = QFrame(self.main_body)
        self.create_menu.setObjectName(u"create_menu")
        self.create_menu.setMinimumSize(QSize(0, 0))
        self.create_menu.setMaximumSize(QSize(0, 0))
        self.create_menu.setFrameShape(QFrame.StyledPanel)
        self.create_menu.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.create_menu)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.add_data_btn = QPushButton(self.create_menu)
        self.add_data_btn.setObjectName(u"add_data_btn")
        font1 = QFont()
        font1.setBold(True)
        self.add_data_btn.setFont(font1)
        self.add_data_btn.setStyleSheet(u"QPushButton {\n"
"    min-width: 80px;\n"
"    min-height: 20px;\n"
"    padding: 6px 12px;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    color: #333;\n"
"    background-color:rgb(230,230,230);\n"
"    border: 2px solid rgb(120, 120, 120);\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(215, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(180, 225, 225);\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    border: 2px solid #06c;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #eee;\n"
"    border-color: #ccc;\n"
"    color: #999;\n"
"}\n"
"\n"
"QPushButton::menu-indicator {\n"
"    width: 0;\n"
"    height: 0;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"}\n"
"\n"
"QPushButton::menu-indicator:subcontrol {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: right center;\n"
"}\n"
"\n"
"")

        self.gridLayout_3.addWidget(self.add_data_btn, 5, 0, 1, 5)

        self.timeEdit = QTimeEdit(self.create_menu)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setMinimumSize(QSize(0, 30))
        self.timeEdit.setMaximumSize(QSize(230, 16777215))
        font2 = QFont()
        self.timeEdit.setFont(font2)
        self.timeEdit.setStyleSheet(u"QTimeEdit{\n"
"	border: 2px solid rgb(120,120,120);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(230,230,230);\n"
"}\n"
"QTimeEdit {\n"
"    border: 2px solid rgb(120,120,120);\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-size: 15px;\n"
"    color: #333;\n"
"}\n"
"\n"
"QTimeEdit:focus {\n"
"    border-color: #06c;\n"
"}\n"
"\n"
"QTimeEdit:disabled {\n"
"    background-color: #eee;\n"
"    color: #999;\n"
"}\n"
"QTimeEdit::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"    image: url(:/icons/icons/chevron-up.svg);\n"
"    width: 24px;\n"
"    height: 24px;\n"
"    padding: -2 -2px;\n"
"}\n"
"\n"
"QTimeEdit::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right;\n"
"    image: url(:/icons/icons/chevron-down.svg);\n"
"    width: 24px;\n"
"    height: 24px;\n"
"    padding: -2 -2px;\n"
"}\n"
"\n"
"")

        self.gridLayout_3.addWidget(self.timeEdit, 3, 0, 1, 5)

        self.name_edit = QLineEdit(self.create_menu)
        self.name_edit.setObjectName(u"name_edit")
        self.name_edit.setMinimumSize(QSize(0, 30))
        self.name_edit.setFont(font2)
        self.name_edit.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid rgb(120,120,120);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(230,230,230);\n"
"}\n"
"QLineEdit {\n"
"    border: 2px solid rgb(120,120,120);\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-size: 15px;\n"
"    color: #333;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: #06c;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color:  rgb(215,215,215);\n"
"    color: #999;\n"
"}\n"
"")
        self.name_edit.setDragEnabled(False)

        self.gridLayout_3.addWidget(self.name_edit, 0, 0, 1, 5)

        self.label = QLabel(self.create_menu)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(60, 0))
        self.label.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_3.addWidget(self.label, 4, 3, 1, 1)

        self.again_box = QComboBox(self.create_menu)
        self.again_box.addItem("")
        self.again_box.addItem("")
        self.again_box.addItem("")
        self.again_box.setObjectName(u"again_box")
        self.again_box.setEnabled(False)
        self.again_box.setMaximumSize(QSize(140, 16777215))
        self.again_box.setFont(font2)
        self.again_box.setStyleSheet(u"QComboBox {\n"
"    min-width: 6em;\n"
"    background-color: #FFFFFF;\n"
"    selection-background-color: #E5E5E5;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-size: 15px;\n"
"    color: #333;\n"
"    border: 2px solid rgb(120,120,120);\n"
"    border-radius: 5px;\n"
"    background-color: rgb(230,230,230);\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background-color: #FFFFFF;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    width: 0;\n"
"    border: none;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #999999;\n"
"    border-radius: 6px;\n"
"    color: #333333;\n"
"    background-color: #FFFFFF;\n"
"    selection-background-color: #7cc5e5;\n"
"    outline: none;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    padding: 2px 5px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    background-color: #7cc5e5;\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"    color: #999999;\n"
"    border-c"
                        "olor: #999999;\n"
"    background-color: #F0F0F0;\n"
"}\n"
"\n"
"QComboBox:disabled QAbstractItemView {\n"
"    color: rgb(50,50,50);\n"
"    background-color: rgb(230,230,230);\n"
"    border-color: #999999;\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.again_box, 4, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(10, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 6, 0, 2, 5)

        self.again_label = QLabel(self.create_menu)
        self.again_label.setObjectName(u"again_label")
        self.again_label.setEnabled(False)
        self.again_label.setMinimumSize(QSize(80, 0))
        self.again_label.setMaximumSize(QSize(80, 16777215))
        font3 = QFont()
        font3.setPointSize(11)
        self.again_label.setFont(font3)

        self.gridLayout_3.addWidget(self.again_label, 4, 0, 1, 1)

        self.label_2 = QLabel(self.create_menu)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(10, 0))
        self.label_2.setMaximumSize(QSize(10, 16777215))

        self.gridLayout_3.addWidget(self.label_2, 4, 2, 1, 1)

        self.dateEdit = QDateEdit(self.create_menu)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setMinimumSize(QSize(0, 30))
        self.dateEdit.setMaximumSize(QSize(230, 16777215))
        self.dateEdit.setFont(font2)
        self.dateEdit.setStyleSheet(u"QDateEdit{\n"
"	border: 2px solid rgb(120,120,120);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(230,230,230);\n"
"}\n"
"QDateEdit {\n"
"    border: 2px solid rgb(120,120,120);\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-size: 15px;\n"
"    color: #333;\n"
"}\n"
"\n"
"QDateEdit:focus {\n"
"    border-color: #06c;\n"
"}\n"
"\n"
"QDateEdit:disabled {\n"
"    background-color: #eee;\n"
"    color: #999;\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.dateEdit, 2, 0, 1, 4)


        self.gridLayout_2.addWidget(self.create_menu, 1, 0, 1, 1)

        self.calendar_menu = QFrame(self.main_body)
        self.calendar_menu.setObjectName(u"calendar_menu")
        self.calendar_menu.setMinimumSize(QSize(0, 0))
        self.calendar_menu.setMaximumSize(QSize(0, 0))
        self.calendar_menu.setFrameShape(QFrame.StyledPanel)
        self.calendar_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.calendar_menu)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.find_tasks_btn = QPushButton(self.calendar_menu)
        self.find_tasks_btn.setObjectName(u"find_tasks_btn")
        self.find_tasks_btn.setMinimumSize(QSize(0, 25))
        font4 = QFont()
        font4.setPointSize(13)
        self.find_tasks_btn.setFont(font4)
        self.find_tasks_btn.setStyleSheet(u"QPushButton {\n"
"	background-repeat: none;\n"
"	border: 2px solid rgb(120, 120, 120);\n"
"	border-radius: 10px;\n"
"	background-color: rgb(215, 215, 215);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(215, 255, 255);\n"
"}")

        self.verticalLayout_6.addWidget(self.find_tasks_btn)


        self.gridLayout_2.addWidget(self.calendar_menu, 1, 2, 1, 1)

        self.all_tasks_menu = QFrame(self.main_body)
        self.all_tasks_menu.setObjectName(u"all_tasks_menu")
        self.all_tasks_menu.setMinimumSize(QSize(0, 0))
        self.all_tasks_menu.setMaximumSize(QSize(0, 0))
        self.all_tasks_menu.setFrameShape(QFrame.StyledPanel)
        self.all_tasks_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.all_tasks_menu)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea = QScrollArea(self.all_tasks_menu)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollArea{\n"
"	border: none;\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 18, 18))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.gridLayout_2.addWidget(self.all_tasks_menu, 1, 4, 1, 1)

        self.start_menu = QFrame(self.main_body)
        self.start_menu.setObjectName(u"start_menu")
        self.start_menu.setFrameShape(QFrame.StyledPanel)
        self.start_menu.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.start_menu)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.previous_day_btn = QPushButton(self.start_menu)
        self.previous_day_btn.setObjectName(u"previous_day_btn")
        self.previous_day_btn.setMaximumSize(QSize(30, 16777215))
        self.previous_day_btn.setStyleSheet(u"QPushButton {\n"
"	background-repeat: none;\n"
"	border: none;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(210, 210, 210);\n"
"	border-radius: 10px;\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/chevron-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.previous_day_btn.setIcon(icon9)
        self.previous_day_btn.setIconSize(QSize(32, 32))

        self.gridLayout_4.addWidget(self.previous_day_btn, 0, 0, 1, 1)

        self.current_data_label = QLabel(self.start_menu)
        self.current_data_label.setObjectName(u"current_data_label")
        self.current_data_label.setMaximumSize(QSize(16777215, 40))
        font5 = QFont()
        font5.setPointSize(20)
        font5.setKerning(True)
        self.current_data_label.setFont(font5)
        self.current_data_label.setStyleSheet(u"QLabel{\n"
"	color: rgba(0, 0, 0, 90);\n"
"}")
        self.current_data_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.current_data_label, 0, 1, 1, 1)

        self.next_day_btn = QPushButton(self.start_menu)
        self.next_day_btn.setObjectName(u"next_day_btn")
        self.next_day_btn.setMaximumSize(QSize(30, 16777215))
        self.next_day_btn.setStyleSheet(u"QPushButton {\n"
"	background-repeat: none;\n"
"	border: none;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(210, 210, 210);\n"
"border-radius: 10px;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/chevron-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.next_day_btn.setIcon(icon10)
        self.next_day_btn.setIconSize(QSize(32, 32))

        self.gridLayout_4.addWidget(self.next_day_btn, 0, 2, 1, 1)

        self.scrollArea_2 = QScrollArea(self.start_menu)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setStyleSheet(u"QScrollArea{\n"
"	border: none\n"
"}")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 603, 291))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_4.addWidget(self.scrollArea_2, 2, 0, 1, 3)


        self.gridLayout_2.addWidget(self.start_menu, 1, 3, 3, 1)

        self.settings_menu = QFrame(self.main_body)
        self.settings_menu.setObjectName(u"settings_menu")
        self.settings_menu.setMinimumSize(QSize(0, 0))
        self.settings_menu.setMaximumSize(QSize(0, 0))
        self.settings_menu.setFrameShape(QFrame.StyledPanel)
        self.settings_menu.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.settings_menu)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(-1, -1, -1, 0)
        self.label_3 = QLabel(self.settings_menu)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setEnabled(False)
        self.label_3.setMaximumSize(QSize(110, 16777215))
        self.label_3.setFont(font4)

        self.gridLayout_5.addWidget(self.label_3, 4, 0, 1, 1)

        self.auto_delete_check = QCheckBox(self.settings_menu)
        self.auto_delete_check.setObjectName(u"auto_delete_check")
        self.auto_delete_check.setMinimumSize(QSize(0, 30))
        self.auto_delete_check.setFont(font4)
        self.auto_delete_check.setStyleSheet(u"QCheckBox::indicator {\n"
"                width: 15px;\n"
"                height: 15px;\n"
"            }\n"
"            QCheckBox::indicator:unchecked {\n"
"                border: 2px solid #C4C4C4;\n"
"                border-radius: 5px;\n"
"            }\n"
"            QCheckBox::indicator:checked {\n"
"                background-color: #00BFFF;\n"
"                border: none;\n"
"				border-radius: 5px;\n"
"            }\n"
"            QCheckBox::indicator:hover {\n"
"                border: 2px solid #1E90FF;\n"
"            }\n"
"            QCheckBox::indicator:checked:hover {\n"
"                background-color: #1E90FF;\n"
"            }\n"
"            QCheckBox::indicator:checked:disabled {\n"
"                background-color: #B0C4DE;\n"
"            }\n"
"            QCheckBox::indicator:unchecked:disabled {\n"
"                border: 2px solid #B0C4DE;\n"
"                border-radius: 5px;\n"
"            }\n"
"            QCheckBox::indicator:indeterminate {\n"
"                back"
                        "ground-color: #C4C4C4;\n"
"            }")

        self.gridLayout_5.addWidget(self.auto_delete_check, 0, 0, 1, 5)

        self.notification_timer = QSpinBox(self.settings_menu)
        self.notification_timer.setObjectName(u"notification_timer")
        self.notification_timer.setEnabled(False)
        self.notification_timer.setMaximumSize(QSize(40, 16777215))
        self.notification_timer.setStyleSheet(u"QSpinBox {\n"
"                border: 2px solid #C4C4C4;\n"
"				\n"
"	background-color: rgb(235, 235, 235);\n"
"                border-radius: 5px;\n"
"                padding: 2px 5px 2px 5px;\n"
"            }\n"
"            QSpinBox::up-button,\n"
"            QSpinBox::down-button {\n"
"                width: 0;\n"
"                height: 0;\n"
"                border: none;\n"
"                background-color: transparent;\n"
"            }	")

        self.gridLayout_5.addWidget(self.notification_timer, 4, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_3, 5, 2, 1, 1)

        self.frame_2 = QFrame(self.settings_menu)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 40))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.apply_btn = QPushButton(self.frame_2)
        self.apply_btn.setObjectName(u"apply_btn")
        self.apply_btn.setFont(font1)
        self.apply_btn.setStyleSheet(u"QPushButton {\n"
"    min-width: 80px;\n"
"    min-height: 15px;\n"
"    padding: 6px 12px;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    color: #333;\n"
"    background-color:rgb(230,230,230);\n"
"    border: 2px solid rgb(120, 120, 120);\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(215, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(180, 225, 225);\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    border: 2px solid #06c;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #eee;\n"
"    border-color: #ccc;\n"
"    color: #999;\n"
"}\n"
"\n"
"QPushButton::menu-indicator {\n"
"    width: 0;\n"
"    height: 0;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"}\n"
"\n"
"QPushButton::menu-indicator:subcontrol {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: right center;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_5.addWidget(self.apply_btn)

        self.cancel_btn = QPushButton(self.frame_2)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setFont(font1)
        self.cancel_btn.setStyleSheet(u"QPushButton {\n"
"    min-width: 80px;\n"
"    min-height: 15px;\n"
"    padding: 6px 12px;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    color: #333;\n"
"    background-color:rgb(230,230,230);\n"
"    border: 2px solid rgb(120, 120, 120);\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(215, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(180, 225, 225);\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    border: 2px solid #06c;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #eee;\n"
"    border-color: #ccc;\n"
"    color: #999;\n"
"}\n"
"\n"
"QPushButton::menu-indicator {\n"
"    width: 0;\n"
"    height: 0;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"}\n"
"\n"
"QPushButton::menu-indicator:subcontrol {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: right center;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_5.addWidget(self.cancel_btn)


        self.gridLayout_5.addWidget(self.frame_2, 6, 0, 1, 5)

        self.notification_check = QCheckBox(self.settings_menu)
        self.notification_check.setObjectName(u"notification_check")
        self.notification_check.setFont(font4)
        self.notification_check.setStyleSheet(u"QCheckBox::indicator {\n"
"                width: 15px;\n"
"                height: 15px;\n"
"            }\n"
"            QCheckBox::indicator:unchecked {\n"
"                border: 2px solid #C4C4C4;\n"
"                border-radius: 5px;\n"
"            }\n"
"            QCheckBox::indicator:checked {\n"
"                background-color: #00BFFF;\n"
"                border: none;\n"
"				border-radius: 5px;\n"
"            }\n"
"            QCheckBox::indicator:hover {\n"
"                border: 2px solid #1E90FF;\n"
"            }\n"
"            QCheckBox::indicator:checked:hover {\n"
"                background-color: #1E90FF;\n"
"            }\n"
"            QCheckBox::indicator:checked:disabled {\n"
"                background-color: #B0C4DE;\n"
"            }\n"
"            QCheckBox::indicator:unchecked:disabled {\n"
"                border: 2px solid #B0C4DE;\n"
"                border-radius: 5px;\n"
"            }\n"
"            QCheckBox::indicator:indeterminate {\n"
"                back"
                        "ground-color: #C4C4C4;\n"
"            }")

        self.gridLayout_5.addWidget(self.notification_check, 2, 0, 1, 4)

        self.label_4 = QLabel(self.settings_menu)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setEnabled(False)
        self.label_4.setMinimumSize(QSize(0, 0))
        self.label_4.setMaximumSize(QSize(50, 16777215))
        self.label_4.setFont(font4)

        self.gridLayout_5.addWidget(self.label_4, 4, 2, 1, 3)

        self.autorun_box = QCheckBox(self.settings_menu)
        self.autorun_box.setObjectName(u"autorun_box")
        self.autorun_box.setFont(font4)
        self.autorun_box.setStyleSheet(u"QCheckBox::indicator {\n"
"                width: 15px;\n"
"                height: 15px;\n"
"            }\n"
"            QCheckBox::indicator:unchecked {\n"
"                border: 2px solid #C4C4C4;\n"
"                border-radius: 5px;\n"
"            }\n"
"            QCheckBox::indicator:checked {\n"
"                background-color: #00BFFF;\n"
"                border: none;\n"
"				border-radius: 5px;\n"
"            }\n"
"            QCheckBox::indicator:hover {\n"
"                border: 2px solid #1E90FF;\n"
"            }\n"
"            QCheckBox::indicator:checked:hover {\n"
"                background-color: #1E90FF;\n"
"            }\n"
"            QCheckBox::indicator:checked:disabled {\n"
"                background-color: #B0C4DE;\n"
"            }\n"
"            QCheckBox::indicator:unchecked:disabled {\n"
"                border: 2px solid #B0C4DE;\n"
"                border-radius: 5px;\n"
"            }\n"
"            QCheckBox::indicator:indeterminate {\n"
"                back"
                        "ground-color: #C4C4C4;\n"
"            }")

        self.gridLayout_5.addWidget(self.autorun_box, 1, 0, 1, 5)


        self.gridLayout_2.addWidget(self.settings_menu, 2, 1, 2, 1)


        self.gridLayout.addWidget(self.main_body, 2, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0449\u0438\u043a \u0437\u0430\u0434\u0430\u0447", None))
        self.left_menu_btn.setText("")
#if QT_CONFIG(shortcut)
        self.left_menu_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+M", None))
#endif // QT_CONFIG(shortcut)
        self.home_btn.setText("")
#if QT_CONFIG(shortcut)
        self.home_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+H", None))
#endif // QT_CONFIG(shortcut)
        self.create_task_btn.setText("")
#if QT_CONFIG(shortcut)
        self.create_task_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.hide_btn.setText("")
        self.expand_btn.setText("")
        self.close_btn.setText("")
        self.calendar_btn.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043b\u0435\u043d\u0434\u0430\u0440\u044c ", None))
#if QT_CONFIG(shortcut)
        self.calendar_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+K", None))
#endif // QT_CONFIG(shortcut)
        self.all_tasks_btn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435 \u0437\u0430\u0434\u0430\u0447\u0438 ", None))
#if QT_CONFIG(shortcut)
        self.all_tasks_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+T", None))
#endif // QT_CONFIG(shortcut)
        self.settings_btn.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 ", None))
#if QT_CONFIG(shortcut)
        self.settings_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+I", None))
#endif // QT_CONFIG(shortcut)
        self.add_data_btn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.name_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0437\u0434\u0435\u0441\u044c \u043d\u043e\u0432\u0443\u044e \u0437\u0430\u0434\u0430\u0447\u0443", None))
        self.label.setText("")
        self.again_box.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0415\u0436\u0435\u0434\u043d\u0435\u0432\u043d\u043e", None))
        self.again_box.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0415\u0436\u0435\u043d\u0435\u0434\u0435\u043b\u044c\u043d\u043e", None))
        self.again_box.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0415\u0436\u0435\u043c\u0435\u0441\u044f\u0447\u043d\u043e", None))

        self.again_label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0432\u0442\u043e\u0440\u044f\u0442\u044c", None))
        self.label_2.setText("")
        self.find_tasks_btn.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438", None))
        self.previous_day_btn.setText("")
        self.current_data_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.next_day_btn.setText("")
#if QT_CONFIG(shortcut)
        self.next_day_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u043e\u0432\u0435\u0449\u0430\u0442\u044c \u0437\u0430", None))
        self.auto_delete_check.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u043f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c \u0437\u0430\u0434\u0430\u0447\u0438 \u043f\u043e \u0438\u0441\u0442\u0435\u0447\u0435\u043d\u0438\u044e \u0438\u0445 \u0441\u0440\u043e\u043a\u0430 ", None))
        self.apply_btn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.cancel_btn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.notification_check.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0432\u0435\u0434\u043e\u043c\u043b\u0435\u043d\u0438\u044f \u043e \u0437\u0430\u0434\u0430\u0447\u0430\u0445", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u043c\u0438\u043d\u0443\u0442", None))
        self.autorun_box.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u043a\u0430\u0442\u044c \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u0432\u043c\u0435\u0441\u0442\u0435 \u0441 Windows", None))
    # retranslateUi

