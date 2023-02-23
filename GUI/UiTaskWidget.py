# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledMNTVBi.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(388, 76)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet(u"")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.delete_btn = QPushButton(Form)
        self.delete_btn.setObjectName(u"delete_btn")
        self.delete_btn.setMinimumSize(QSize(0, 35))
        self.delete_btn.setMaximumSize(QSize(40, 16777215))
        self.delete_btn.setStyleSheet(u"QPushButton {\n"
"	background-repeat: none;\n"
"	border: none;\n"
"	background-color: rgb(215, 215, 215);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgba(255,0,0, 120);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/slash.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_btn.setIcon(icon)
        self.delete_btn.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.delete_btn, 0, 3, 2, 1)

        self.edit_btn = QPushButton(Form)
        self.edit_btn.setObjectName(u"edit_btn")
        self.edit_btn.setMinimumSize(QSize(0, 35))
        self.edit_btn.setMaximumSize(QSize(40, 16777215))
        self.edit_btn.setStyleSheet(u"QPushButton {\n"
"	background-repeat: none;\n"
"	border: none;\n"
"	background-color: rgb(215, 215, 215);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgba(255,255,0, 120);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/edit-3.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.edit_btn.setIcon(icon1)
        self.edit_btn.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.edit_btn, 0, 4, 2, 1)

        self.data_and_time = QLabel(Form)
        self.data_and_time.setObjectName(u"data_and_time")
        font = QFont()
        font.setPointSize(11)
        self.data_and_time.setFont(font)
        self.data_and_time.setStyleSheet(u"")

        self.gridLayout.addWidget(self.data_and_time, 1, 1, 1, 1)

        self.accept_btn = QPushButton(Form)
        self.accept_btn.setObjectName(u"accept_btn")
        self.accept_btn.setMinimumSize(QSize(0, 35))
        self.accept_btn.setMaximumSize(QSize(40, 16777215))
        self.accept_btn.setStyleSheet(u"QPushButton {\n"
"	background-repeat: none;\n"
"	border: none;\n"
"	background-color: rgb(215, 215, 215);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgba(0,255,0, 120);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/check.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.accept_btn.setIcon(icon2)
        self.accept_btn.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.accept_btn, 0, 5, 2, 1)

        self.repeat_label = QLabel(Form)
        self.repeat_label.setObjectName(u"repeat_label")
        self.repeat_label.setMaximumSize(QSize(30, 16777215))
        self.repeat_label.setStyleSheet(u"border: none;")
        self.repeat_label.setPixmap(QPixmap(u":/icons/icons/repeat.svg"))
        self.repeat_label.setScaledContents(False)

        self.gridLayout.addWidget(self.repeat_label, 1, 0, 1, 1)

        self.name_label = QLabel(Form)
        self.name_label.setObjectName(u"name_label")
        font1 = QFont()
        font1.setPointSize(16)
        self.name_label.setFont(font1)

        self.gridLayout.addWidget(self.name_label, 0, 0, 1, 3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.delete_btn.setText("")
        self.edit_btn.setText("")
        self.data_and_time.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.accept_btn.setText("")
        self.repeat_label.setText("")
        self.name_label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

