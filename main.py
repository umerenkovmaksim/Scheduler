import sqlite3
import sys
import time
from datetime import datetime

import PySide6
from PySide6 import QtCore
from PySide6.QtGui import QColor, QTextCharFormat, QFont
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect, QSizeGrip, QWidget, QCalendarWidget, \
    QSpinBox, QToolButton, QDateEdit
from PySide6.QtCore import QFile, QPropertyAnimation, QEasingCurve, Qt, QSize, QDate
from GUI.MainWindow import Ui_MainWindow
from GUI.UiTaskWidget import Ui_Form


def clear_layout(layout):
    while layout.count():
        child = layout.takeAt(0)
        if child.widget() is not None:
            child.widget().deleteLater()
        elif child.layout() is not None:
            clear_layout(child.layout())


class CustomDataEdit(QDateEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        style_main_color = 808080
        self.setCalendarPopup(True)
        self.setStyleSheet(
            "QDateEdit{border: 2px solid rgb(120,120,120);border-radius: 10px;background-color: rgb(235,235,235);}"
        )

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
        toolbtn.setIconSize(s)
        toolbtn = self.calendarWidget().findChild(QToolButton, "qt_calendar_nextmonth")
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


class TaskWidget(QWidget, Ui_Form):
    def __init__(self, parent, id, name, date, time, accept):
        super().__init__()
        self.setupUi(self)
        self.name_label.setText(name)
        self.parent, self.name, self.id, self.date, self.time, self.accept = parent, name, id, date, time, accept
        self.data_and_time.setText(f'{date} {time}')
        self.setMaximumHeight(100)
        self.setAttribute(Qt.WA_StyledBackground, True)

        self.name_label.setStyleSheet("QLabel{"
                                      "border: none;"
                                      "}")
        self.data_and_time.setStyleSheet("QLabel{"
                                         "border: none;"
                                         "}")

        if self.accept:
            self.setStyleSheet("QWidget {"
                               "background-color: rgb(215, 215, 215);"
                               "border-radius: 10px;border: 2px solid green;"
                               "}")
            self.edit_btn.hide()
        else:
            self.setStyleSheet("QWidget {"
                               "background-color: rgb(215, 215, 215);"
                               "border-radius: 10px;"
                               "}")
            self.edit_btn.show()
        self.delete_btn.clicked.connect(self.delete_task)
        self.accept_btn.clicked.connect(self.accept_task)

    def delete_task(self):
        con = sqlite3.connect('SchedulerApp.db')
        cur = con.cursor()
        cur.execute(f"""DELETE FROM scheduler_data WHERE id={self.id}""")
        con.commit()
        con.close()
        self.parent.load_tasks()
        self.parent.load_day_tasks(self.parent.current_date)

    def accept_task(self):
        self.accept = not self.accept
        con = sqlite3.connect('SchedulerApp.db')
        cur = con.cursor()
        cur.execute(f"""UPDATE scheduler_data SET accept={self.accept} WHERE id={self.id}""")
        con.commit()
        con.close()
        self.parent.load_tasks()
        self.parent.load_day_tasks(self.parent.current_date)


class CustomCalendar(QCalendarWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.clicked.connect(self.click)

    def paintCell(self, painter, rect, date):
        QCalendarWidget.paintCell(self, painter, rect, date)
        if date == date.currentDate():
            painter.setBrush(QColor(0, 200, 200, 50))
            painter.setPen(QColor(0, 0, 0, 0))
            painter.drawRect(rect)

    def click(self, index):
        self.index = index


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.left_menu_btn.clicked.connect(lambda: self.slide_left_menu())
        QSizeGrip(self.size_grip)
        self.left_menu_enabled, self.create_menu_enabled, \
            self.calendar_menu_enabled, self.all_tasks_menu_enabled = False, False, False, False

        self.calendarWidget = CustomCalendar(self.calendar_menu)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setMaximumSize(QSize(999999, 99999))

        self.verticalLayout_6.insertWidget(0, self.calendarWidget)

        font2 = QFont()
        font2.setFamilies([u"Calibri"])
        font2.setPointSize(12)
        self.dateEdit = CustomDataEdit(self.create_menu)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setMinimumSize(QSize(0, 30))
        self.dateEdit.setMaximumSize(QSize(200, 16777215))
        self.dateEdit.setFont(font2)

        self.gridLayout_3.addWidget(self.dateEdit, 2, 0, 1, 1)

        self.close_btn.clicked.connect(self.close)
        self.add_data_btn.clicked.connect(self.add_data_to_db)
        self.find_tasks_btn.clicked.connect(self.find_tasks_to_day)
        self.home_btn.clicked.connect(lambda: self.return_to_home(self.left_menu_enabled,
                                                                  self.create_menu_enabled,
                                                                  self.calendar_menu_enabled,
                                                                  self.all_tasks_menu_enabled))
        self.all_tasks_btn.clicked.connect(self.slide_all_tasks_menu)
        self.calendar_btn.clicked.connect(self.slide_calendar_menu)
        self.create_task_btn.clicked.connect(self.slide_create_menu)
        self.expand_btn.clicked.connect(lambda: self.expand_action())
        self.hide_btn.clicked.connect(self.showMinimized)

        self.current_date = datetime.today().strftime("%d-%m-%Y")
        self.current_data_label.setText(f'Сегодня ({self.current_date})')
        self.load_day_tasks()
        self.dateEdit.setDate(datetime.today())
        self.timeEdit.setTime(datetime.now().time())
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.load_tasks()
        self.load_animations()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_F11:
            self.expand_action()

    def mousePressEvent(self, event):
        if self.move_window_bar.underMouse() and event.button() == Qt.LeftButton:
            self.old_pos = event.pos()

    def mouseReleaseEvent(self, event):
        if self.move_window_bar.underMouse() and event.button() == Qt.LeftButton:
            self.old_pos = None

    def mouseMoveEvent(self, event):
        if not self.old_pos or not self.move_window_bar.underMouse():
            return
        delta = event.pos() - self.old_pos
        self.move(self.pos() + delta)

    def main_menu_visible(self):
        now_open = [self.create_menu_enabled, self.calendar_menu_enabled, self.all_tasks_menu_enabled]
        if any(now_open):
            self.start_menu.setMaximumWidth(0)
            self.start_menu.setMaximumHeight(0)
        else:
            self.load_day_tasks(self.current_date)
            self.start_menu_animation_h.setStartValue(0)
            self.start_menu_animation_h.setEndValue(self.height())
            self.start_menu_animation_h.start()
            self.start_menu_animation_w.setStartValue(0)
            self.start_menu_animation_w.setEndValue(self.width())
            self.start_menu_animation_w.start()

    def find_tasks_to_day(self):
        if self.calendarWidget.index != 1:
            self.load_day_tasks(self.calendarWidget.index.toString("dd-MM-yyyy"))
            self.return_to_home(0, self.create_menu_enabled, self.calendar_menu_enabled, self.all_tasks_menu_enabled)
            self.calendarWidget.index = 1

    def load_day_tasks(self, date=datetime.today().strftime("%d-%m-%Y")):
        self.current_date = date
        self.current_data_label.setText(
            f'Сегодня ({self.current_date})' if self.current_date == datetime.today().strftime(
                "%d-%m-%Y") else self.current_date)
        con = sqlite3.connect('SchedulerApp.db')
        cur = con.cursor()
        data_from_db = sorted(sorted(cur.execute(f"""SELECT * from scheduler_data 
        WHERE date LIKE '%{date}%'""").fetchall(), key=lambda x: x[3]),
                              key=lambda x: x[2])
        clear_layout(self.verticalLayout_5)
        for elem in data_from_db:
            self.verticalLayout_5.addWidget(TaskWidget(self, elem[0], elem[1], elem[2], elem[3], elem[4]))
        con.commit()
        con.close()

    def load_tasks(self):
        con = sqlite3.connect('SchedulerApp.db')
        cur = con.cursor()
        data_from_db = sorted(sorted(cur.execute("""SELECT * from scheduler_data""").fetchall(), key=lambda x: x[3]),
                              key=lambda x: x[2])
        clear_layout(self.verticalLayout_3)
        for elem in data_from_db:
            self.verticalLayout_3.addWidget(TaskWidget(self, elem[0], elem[1], elem[2], elem[3], elem[4]))
        con.commit()
        con.close()

    def add_data_to_db(self):
        name = self.name_edit.text()
        data = self.dateEdit.date()
        time = self.timeEdit.time()

        con = sqlite3.connect('SchedulerApp.db')
        cur = con.cursor()
        out_data = [name, data.toString('dd-MM-yyyy'), time.toString()]
        cur.execute("""INSERT INTO scheduler_data(name, date, time) VALUES (?,?,?)""", out_data)
        con.commit()
        con.close()
        self.load_tasks()

    def return_to_home(self, left_menu, create_menu, calendar_menu, all_tasks_menu):
        self.slide_left_menu() if left_menu else ''
        self.slide_create_menu() if create_menu else ''
        self.slide_calendar_menu() if calendar_menu else ''
        self.slide_all_tasks_menu() if all_tasks_menu else ''
        self.main_menu_visible()

    def load_animations(self):
        self.left_menu_animation = QPropertyAnimation(self.left_menu, b'maximumWidth')
        self.left_menu_animation.setDuration(350)
        self.left_menu_animation.setEasingCurve(QEasingCurve.InOutCubic)

        self.create_menu_animation_w = QPropertyAnimation(self.create_menu, b'maximumWidth')
        self.create_menu_animation_w.setDuration(350)
        self.create_menu_animation_w.setEasingCurve(QEasingCurve.InOutCubic)

        self.left_menu_animation_h = QPropertyAnimation(self.create_menu, b'maximumHeight')
        self.left_menu_animation_h.setDuration(350)
        self.left_menu_animation_h.setEasingCurve(QEasingCurve.InOutCubic)

        self.calendar_menu_animation_w = QPropertyAnimation(self.calendar_menu, b'maximumWidth')
        self.calendar_menu_animation_w.setDuration(350)
        self.calendar_menu_animation_w.setEasingCurve(QEasingCurve.InOutCubic)

        self.calendar_menu_animation_h = QPropertyAnimation(self.calendar_menu, b'maximumHeight')
        self.calendar_menu_animation_h.setDuration(350)
        self.calendar_menu_animation_h.setEasingCurve(QEasingCurve.InOutCubic)

        self.all_tasks_menu_animation_w = QPropertyAnimation(self.all_tasks_menu, b'maximumWidth')
        self.all_tasks_menu_animation_w.setDuration(350)
        self.all_tasks_menu_animation_w.setEasingCurve(QEasingCurve.InOutCubic)

        self.all_tasks_menu_animation_h = QPropertyAnimation(self.all_tasks_menu, b'maximumHeight')
        self.all_tasks_menu_animation_h.setDuration(350)
        self.all_tasks_menu_animation_h.setEasingCurve(QEasingCurve.InOutCubic)

        self.start_menu_animation_w = QPropertyAnimation(self.start_menu, b'maximumWidth')
        self.start_menu_animation_w.setDuration(350)
        self.start_menu_animation_w.setEasingCurve(QEasingCurve.InOutCubic)

        self.start_menu_animation_h = QPropertyAnimation(self.start_menu, b'maximumHeight')
        self.start_menu_animation_h.setDuration(350)
        self.start_menu_animation_h.setEasingCurve(QEasingCurve.InOutCubic)

    def slide_left_menu(self):
        width = self.left_menu.width()
        if width == 0:
            new_width = 120
        else:
            new_width = 0
        self.left_menu_animation.setStartValue(width)
        self.left_menu_animation.setEndValue(new_width)
        self.left_menu_animation.start()
        self.left_menu_enabled = not self.left_menu_enabled

    def slide_create_menu(self, recursion=False):
        width, height = self.create_menu.width(), self.create_menu.height()
        self.dateEdit.setDate(QDate(*tuple(map(int, self.current_date.split('-')[::-1]))))
        self.timeEdit.setTime(datetime.now().time())
        now_open = [self.create_menu_enabled, self.calendar_menu_enabled, self.all_tasks_menu_enabled]
        if any(now_open) and not self.create_menu_enabled:
            self.slide_all_tasks_menu(True) if self.all_tasks_menu_enabled else ''
            self.slide_calendar_menu(True) if self.calendar_menu_enabled else ''
        if width == 0:
            new_width = self.width()
        else:
            new_width = 0

        self.create_menu_enabled = not self.create_menu_enabled
        self.main_menu_visible() if not recursion else ''
        self.create_menu_animation_w.setStartValue(width)
        self.create_menu_animation_w.setEndValue(new_width)
        self.create_menu_animation_w.start()

        if height == 0:
            new_height = self.height()
        else:
            new_height = 0

        self.left_menu_animation_h.setStartValue(height)
        self.left_menu_animation_h.setEndValue(new_height)
        self.left_menu_animation_h.start()

    def slide_calendar_menu(self, recursion=False):
        width, height = self.calendar_menu.width(), self.calendar_menu.height()
        now_open = [self.create_menu_enabled, self.calendar_menu_enabled, self.all_tasks_menu_enabled]
        if any(now_open) and not self.calendar_menu_enabled:
            self.slide_all_tasks_menu(True) if self.all_tasks_menu_enabled else ''
            self.slide_create_menu(True) if self.create_menu_enabled else ''
        if width == 0:
            new_width = self.width()
        else:
            new_width = 0
        self.calendar_menu_enabled = not self.calendar_menu_enabled
        self.main_menu_visible() if not recursion else ''
        self.calendar_menu_animation_w.setStartValue(width)
        self.calendar_menu_animation_w.setEndValue(new_width)
        self.calendar_menu_animation_w.start()

        if height == 0:
            new_height = self.height()
        else:
            new_height = 0
        self.calendar_menu_animation_h.setStartValue(height)
        self.calendar_menu_animation_h.setEndValue(new_height)
        self.calendar_menu_animation_h.start()

    def slide_all_tasks_menu(self, recursion=False):
        width, height = self.all_tasks_menu.width(), self.all_tasks_menu.height()
        now_open = [self.create_menu_enabled, self.calendar_menu_enabled, self.all_tasks_menu_enabled]
        if any(now_open) and not self.all_tasks_menu_enabled:
            self.slide_calendar_menu(True) if self.calendar_menu_enabled else ''
            self.slide_create_menu(True) if self.create_menu_enabled else ''
        if width == 0:
            new_width = self.width()
        else:
            new_width = 0
        self.all_tasks_menu_enabled = not self.all_tasks_menu_enabled
        self.main_menu_visible() if not recursion else ''
        self.all_tasks_menu_animation_w.setStartValue(width)
        self.all_tasks_menu_animation_w.setEndValue(new_width)
        self.all_tasks_menu_animation_w.start()

        if height == 0:
            new_height = self.height()
        else:
            new_height = 0
        self.all_tasks_menu_animation_h.setStartValue(height)
        self.all_tasks_menu_animation_h.setEndValue(new_height)
        self.all_tasks_menu_animation_h.start()

    def expand_action(self):
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
