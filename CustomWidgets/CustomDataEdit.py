from PySide6.QtCore import QSize, QDate
from PySide6.QtGui import QTextCharFormat, QColor, Qt, QIcon
from PySide6.QtWidgets import QDateEdit, QWidget, QSpinBox, QToolButton


class CustomDataEdit(QDateEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        style_main_color = 808080
        self.setCalendarPopup(True)
        self.setStyleSheet(
            "QDateEdit{border: 2px solid rgb(120,120,120);border-radius: 5px;background-color: rgb(235,235,235);}"
            f"QDateEdit::drop-down{{border:none;}}"
            f"QDateEdit::down-arrow{{image: url(:/icons/icons/chevron-down.svg);border: none;}}color: white;")

        format = QTextCharFormat()

        format.setForeground(QColor(Qt.black))
        dateEditCalendarWidget = self.calendarWidget()
        dateEditCalendarWidget.setWeekdayTextFormat(Qt.Saturday, format)
        dateEditCalendarWidget.setWeekdayTextFormat(Qt.Sunday, format)
        dateEditCalendarWidget.setFixedSize(300, 190)
        dateEditCalendarWidget.findChildren(QWidget)[0].setCursor(Qt.PointingHandCursor)
        dateEditCalendarWidget.findChildren(QSpinBox)[0].setAlignment(Qt.AlignCenter)
        dateEditCalendarWidget.findChildren(QSpinBox)[0].setButtonSymbols(QSpinBox.NoButtons)
        toolbtn_list = self.calendarWidget().findChildren(QToolButton)
        for toolbtn in toolbtn_list:
            toolbtn.setCursor(Qt.PointingHandCursor)

        s = QSize(32, 32)
        toolbtn = self.calendarWidget().findChild(QToolButton, "qt_calendar_prevmonth")
        toolbtn.setIcon(QIcon(':/icons/icons/arrow-left.svg'))
        toolbtn.setIconSize(s)
        toolbtn = self.calendarWidget().findChild(QToolButton, "qt_calendar_nextmonth")
        toolbtn.setIcon(QIcon(':/icons/icons/arrow-right.svg'))
        toolbtn.setIconSize(s)

        self.calendarWidget().setStyleSheet(
            f"QCalendarWidget{{background-color:#FFFFFF;border: 1px solid #{style_main_color};}}"
            f"QCalendarWidget QAbstractItemView:enabled{{color:#000000;"
            f"background-color:#ffffff;"
            f"selection-color: white;"
            f"selection-background-color:#{style_main_color};}}"
            f"QCalendarWidget QSpinBox#qt_calendar_yearedit{{background:#ffffff;height:34px;width:125px;selection-background-color:#{style_main_color};}}"
            f"QCalendarWidget QToolButton{{background-color:#FFFFFF;height:34px;width:125px;color:#000000;}}"
            f"QCalendarWidget QToolButton:hover{{border: 1px solid #{style_main_color};}}"
            f"QCalendarWidget QToolButton::menu-indicator#qt_calendar_monthbutton{{subcontrol-position: right center;subcontrol-origin: padding;}}"
            f"QCalendarWidget QToolButton QMenu{{background-color:#FFFFFF;width:125px;border:1px solid #{style_main_color};}}"
            f"QCalendarWidget QToolButton QMenu::item:selected{{color:#FFFFFF;background:#{style_main_color};}}")
        self.setDate(QDate.currentDate())
        self.setDisplayFormat("dd-MM-yyyy")
