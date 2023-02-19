# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow - untitledwBpeSK.ui'
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
        MainWindow.resize(654, 431)
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
        font.setFamilies([u"Calibri"])
        font.setPointSize(14)
        self.create_task_btn.setFont(font)
        self.create_task_btn.setStyleSheet(u"QPushButton {\n"
"	background-repeat: none;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(215, 255, 255);\n"
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
        self.hide_btn.setMinimumSize(QSize(0, 25))
        self.hide_btn.setStyleSheet(u"QPushButton {\n"
"	background-repeat: none;\n"
"	border: none;\n"
"	background-color: rgb(215, 215, 215);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(215, 255, 255);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.hide_btn.setIcon(icon3)

        self.horizontalLayout_4.addWidget(self.hide_btn)

        self.expand_btn = QPushButton(self.actions_bar)
        self.expand_btn.setObjectName(u"expand_btn")
        self.expand_btn.setMinimumSize(QSize(0, 25))
        self.expand_btn.setStyleSheet(u"QPushButton {\n"
"	background-repeat: none;\n"
"	border: none;\n"
"	background-color: rgb(215, 215, 215);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(215, 255, 255);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/maximize-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.expand_btn.setIcon(icon4)

        self.horizontalLayout_4.addWidget(self.expand_btn)

        self.close_btn = QPushButton(self.actions_bar)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMinimumSize(QSize(0, 25))
        self.close_btn.setStyleSheet(u"QPushButton {\n"
"	background-repeat: none;\n"
"	border: none;\n"
"	background-color: rgb(215, 215, 215);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: red;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn.setIcon(icon5)

        self.horizontalLayout_4.addWidget(self.close_btn)


        self.horizontalLayout_3.addWidget(self.actions_bar)


        self.horizontalLayout.addWidget(self.top_bar)


        self.gridLayout.addWidget(self.main_header, 0, 0, 1, 2)

        self.main_body = QFrame(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.main_body)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(2)
        self.gridLayout_2.setContentsMargins(6, 6, 6, 6)
        self.start_menu = QFrame(self.main_body)
        self.start_menu.setObjectName(u"start_menu")
        self.start_menu.setFrameShape(QFrame.StyledPanel)
        self.start_menu.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.start_menu)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.start_menu)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setStyleSheet(u"QScrollArea{\n"
"	border: none\n"
"}")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 632, 316))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_4.addWidget(self.scrollArea_2, 2, 0, 1, 1)

        self.current_data_label = QLabel(self.start_menu)
        self.current_data_label.setObjectName(u"current_data_label")
        self.current_data_label.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Calibri"])
        font1.setPointSize(20)
        font1.setKerning(True)
        self.current_data_label.setFont(font1)
        self.current_data_label.setStyleSheet(u"QLabel{\n"
"	color: rgba(0, 0, 0, 90);\n"
"}")
        self.current_data_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.current_data_label, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.start_menu, 1, 3, 3, 1)

        self.calendar_menu = QFrame(self.main_body)
        self.calendar_menu.setObjectName(u"calendar_menu")
        self.calendar_menu.setMaximumSize(QSize(0, 0))
        self.calendar_menu.setFrameShape(QFrame.StyledPanel)
        self.calendar_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.calendar_menu)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.find_tasks_btn = QPushButton(self.calendar_menu)
        self.find_tasks_btn.setObjectName(u"find_tasks_btn")
        self.find_tasks_btn.setMinimumSize(QSize(0, 20))
        font2 = QFont()
        font2.setFamilies([u"Calibri"])
        font2.setPointSize(12)
        self.find_tasks_btn.setFont(font2)
        self.find_tasks_btn.setStyleSheet(u"QPushButton {\n"
"	background-repeat: none;\n"
"	border: none;\n"
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
        self.name_edit = QLineEdit(self.create_menu)
        self.name_edit.setObjectName(u"name_edit")
        self.name_edit.setMinimumSize(QSize(0, 30))
        self.name_edit.setFont(font2)
        self.name_edit.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid rgb(120,120,120);\n"
"	border-radius: 10px;\n"
"	background-color: rgb(235,235,235);\n"
"}")
        self.name_edit.setDragEnabled(False)

        self.gridLayout_3.addWidget(self.name_edit, 0, 0, 1, 1)

        self.timeEdit = QTimeEdit(self.create_menu)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setMinimumSize(QSize(0, 30))
        self.timeEdit.setMaximumSize(QSize(200, 16777215))
        self.timeEdit.setFont(font2)
        self.timeEdit.setStyleSheet(u"QTimeEdit{\n"
"	border: 2px solid rgb(120,120,120);\n"
"	border-radius: 10px;\n"
"	background-color: rgb(235,235,235);\n"
"}")

        self.gridLayout_3.addWidget(self.timeEdit, 3, 0, 1, 1)

        self.add_data_btn = QPushButton(self.create_menu)
        self.add_data_btn.setObjectName(u"add_data_btn")
        font3 = QFont()
        font3.setFamilies([u"Calibri"])
        font3.setPointSize(13)
        self.add_data_btn.setFont(font3)
        self.add_data_btn.setStyleSheet(u"QPushButton {\n"
"	background-repeat: none;\n"
"	background-color: rgb(215, 215, 215);\n"
"	border-radius: 10px;\n"
"	border: 1px solid #094065;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(215, 255, 255);\n"
"}")

        self.gridLayout_3.addWidget(self.add_data_btn, 5, 0, 1, 2)

        self.dateEdit = QDateEdit(self.create_menu)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setMinimumSize(QSize(0, 30))
        self.dateEdit.setMaximumSize(QSize(200, 16777215))
        self.dateEdit.setFont(font2)
        self.dateEdit.setStyleSheet(u"QDateEdit{\n"
"	border: 2px solid rgb(120,120,120);\n"
"	border-radius: 10px;\n"
"	background-color: rgb(235,235,235);\n"
"}")

        self.gridLayout_3.addWidget(self.dateEdit, 2, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(10, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 6, 0, 2, 2)


        self.gridLayout_2.addWidget(self.create_menu, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.main_body, 2, 1, 1, 1)

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
"}")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_btn.setIcon(icon8)
        self.settings_btn.setIconSize(QSize(24, 24))
        self.settings_btn.setFlat(False)

        self.verticalLayout.addWidget(self.settings_btn)


        self.gridLayout.addWidget(self.left_menu, 2, 0, 1, 1)

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

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.left_menu_btn.setText("")
        self.home_btn.setText("")
        self.create_task_btn.setText("")
        self.hide_btn.setText("")
        self.expand_btn.setText("")
        self.close_btn.setText("")
        self.current_data_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.find_tasks_btn.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438", None))
        self.name_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0437\u0434\u0435\u0441\u044c \u043d\u043e\u0432\u0443\u044e \u0437\u0430\u0434\u0430\u0447\u0443", None))
        self.add_data_btn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.calendar_btn.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043b\u0435\u043d\u0434\u0430\u0440\u044c", None))
        self.all_tasks_btn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435 \u0437\u0430\u0434\u0430\u0447\u0438", None))
        self.settings_btn.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
    # retranslateUi

