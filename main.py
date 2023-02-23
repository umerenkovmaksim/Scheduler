import datetime
from datetime import timedelta
from datetime import date as to_date
import sys
import time
from qt_material import apply_stylesheet

from PySide6 import QtCore
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QTimer
from PySide6.QtGui import QFont, QFontDatabase
from PySide6.QtWidgets import QApplication, QMainWindow, QSizeGrip, QLabel, QGraphicsBlurEffect
from CustomWidgets.CustomCalendar import *
from CustomWidgets.CustomDataEdit import *
from CustomWidgets.Switcher import *
from CustomWidgets.TaskWidget import *
from GUI.MainWindow import Ui_MainWindow


def clear_layout(layout):
    while layout.count():
        child = layout.takeAt(0)
        if child.widget() is not None:
            child.widget().deleteLater()
        elif child.layout() is not None:
            clear_layout(child.layout())


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.left_menu_btn.clicked.connect(lambda: self.slide_left_menu())
        QSizeGrip(self.size_grip)
        self.left_menu_enabled, self.create_menu_enabled, self.settings_menu_enabled, \
            self.calendar_menu_enabled, self.all_tasks_menu_enabled = False, False, False, False, False
        self.start_menu_enabled = True
        self.timeout = time.time()
        self.last_home_click = time.time()

        self.calendarWidget = CustomCalendar(self.calendar_menu)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setMaximumSize(QSize(999999, 99999))

        self.verticalLayout_6.insertWidget(0, self.calendarWidget)

        font2 = QFont()
        font2.setFamilies([u"Calibri"])
        font2.setPointSize(12)
        data_edit_style = self.dateEdit.styleSheet()
        self.dateEdit.setStyleSheet('')
        self.dateEdit = CustomDataEdit(self.create_menu)
        self.dateEdit.setStyleSheet(data_edit_style + self.dateEdit.styleSheet())
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setMinimumSize(QSize(0, 30))
        self.dateEdit.setMaximumSize(QSize(230, 16777215))
        self.gridLayout_3.addWidget(self.dateEdit, 2, 0, 1, 5)

        self.every_day_check = Switcher(self.create_menu, 40, 20, '#d7d7d7', 'white', '#4a9db5')
        self.every_day_check.setObjectName(u"every_day_check")
        self.every_day_check.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.every_day_check, 4, 3, 1, 1)

        self.close_btn.clicked.connect(self.close)
        self.add_data_btn.clicked.connect(self.add_data_to_db)
        self.find_tasks_btn.clicked.connect(self.find_tasks_to_day)
        self.home_btn.clicked.connect(lambda: self.return_to_home(self.left_menu_enabled,
                                                                  self.create_menu_enabled,
                                                                  self.calendar_menu_enabled,
                                                                  self.all_tasks_menu_enabled,
                                                                  self.settings_menu_enabled,
                                                                  False))
        self.settings_btn.clicked.connect(self.slide_settings_menu)
        self.all_tasks_btn.clicked.connect(self.slide_all_tasks_menu)
        self.calendar_btn.clicked.connect(self.slide_calendar_menu)
        self.create_task_btn.clicked.connect(self.slide_create_menu)
        self.previous_day_btn.clicked.connect(self.previous_day)
        self.next_day_btn.clicked.connect(self.next_day)
        self.every_day_check.stateChanged.connect(self.update_text_visible)
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

    def resizeEvent(self, event):
        self.create_menu.setMaximumSize(self.width(), self.height()) if self.create_menu_enabled else ''
        self.start_menu.setMaximumSize(self.width(), self.height()) if self.start_menu_enabled else ''
        self.calendar_menu.setMaximumSize(self.width(), self.height()) if self.calendar_menu_enabled else ''
        self.all_tasks_menu.setMaximumSize(self.width(), self.height()) if self.all_tasks_menu_enabled else ''
        self.settings_menu.setMaximumSize(self.width(), self.height()) if self.settings_menu_enabled else ''

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
        if not self.move_window_bar.underMouse() or not self.old_pos:
            return
        delta = event.pos() - self.old_pos
        self.move(self.pos() + delta)

    def previous_day(self):
        self.current_date = (to_date(*tuple(map(int, self.current_date.split('-')[::-1]))) + timedelta(
            days=-1)).strftime('%d-%m-%Y')
        self.load_day_tasks(self.current_date)

    def next_day(self):
        self.current_date = (to_date(*tuple(map(int, self.current_date.split('-')[::-1]))) + timedelta(
            days=1)).strftime('%d-%m-%Y')
        self.load_day_tasks(self.current_date)

    def main_menu_visible(self):
        now_open = [self.create_menu_enabled, self.settings_menu_enabled, self.calendar_menu_enabled,
                    self.all_tasks_menu_enabled]
        if any(now_open):
            self.lock_window()
            self.start_menu_enabled = False
            self.start_menu_animation_h.setStartValue(self.start_menu.height())
            self.start_menu_animation_h.setEndValue(0)
            self.start_menu_animation_h.start()
            self.start_menu_animation_w.setStartValue(self.start_menu.width())
            self.start_menu_animation_w.setEndValue(0)
            self.start_menu_animation_w.start()
        elif not self.start_menu_enabled:
            self.lock_window()
            self.start_menu_enabled = True
            self.load_day_tasks(self.current_date)
            self.start_menu_animation_h.setStartValue(0)
            self.start_menu_animation_h.setEndValue(self.height())
            self.start_menu_animation_h.start()
            self.start_menu_animation_w.setStartValue(0)
            self.start_menu_animation_w.setEndValue(self.width())
            self.start_menu_animation_w.start()

    def update_text_visible(self):
        if self.every_day_check.isChecked():
            self.again_label.setEnabled(True)
            self.again_box.setEnabled(True)
        else:
            self.again_label.setEnabled(False)
            self.again_box.setEnabled(False)

    def lock_window(self):
        self.setFixedSize(self.size())
        QTimer.singleShot(350, self.unlock_window)

    def unlock_window(self):
        self.setMinimumSize(0, 0)
        self.setMaximumSize(16777215, 16777215)

    def find_tasks_to_day(self):
        if self.calendarWidget.index != 1:
            self.load_day_tasks(self.calendarWidget.index.toString("dd-MM-yyyy"))
            self.return_to_home(0, self.create_menu_enabled, self.calendar_menu_enabled, self.all_tasks_menu_enabled,
                                False)
            self.calendarWidget.index = 1

    def load_day_tasks(self, date=datetime.today().strftime("%d-%m-%Y")):
        self.current_date = date
        self.current_data_label.setText(
            f'Сегодня ({self.current_date})' if self.current_date == datetime.today().strftime(
                "%d-%m-%Y") else self.current_date)
        con = sqlite3.connect('SchedulerApp.db')
        cur = con.cursor()
        data_from_db = sorted(sorted(cur.execute(f"""SELECT * from scheduler_data 
        WHERE date LIKE '%{date}%' OR repeat != ''""").fetchall(), key=lambda x: x[3]),
                              key=lambda x: x[2])

        clear_layout(self.verticalLayout_5)
        will_deleted = []
        for index, elem in enumerate(data_from_db):
            elem_date = to_date(*tuple(map(int, elem[2].split('-')[::-1])))
            today = to_date(*tuple(map(int, self.current_date.split('-')[::-1])))
            delta_days = elem_date - today
            if not elem[5] or elem[5] == 'Ежедневно' or (elem[5] == 'Еженедельно' and delta_days.days % 7 == 0) or (
                    elem[5] == 'Ежемесячно' and elem_date.day == today.day):
                continue
            will_deleted.append(index)
        for index in will_deleted[::-1]:
            data_from_db.pop(index)
        if len(data_from_db) == 0:
            label = QLabel()
            label.setMaximumSize(QSize(16777215, 16777215))
            font1 = QFont()
            font1.setPointSize(20)
            font1.setKerning(True)
            label.setFont(font1)
            label.setStyleSheet(u"QLabel{color: rgba(0, 0, 0, 90);}")
            label.setAlignment(Qt.AlignCenter)
            label.setText('Ничего не найдено')
            self.verticalLayout_5.addWidget(label)
            self.verticalLayout_5.addWidget(QLabel())
        else:
            for elem in data_from_db:
                self.verticalLayout_5.addWidget(TaskWidget(self, *elem))
        con.commit()
        con.close()

    def load_tasks(self):
        con = sqlite3.connect('SchedulerApp.db')
        cur = con.cursor()
        data_from_db = sorted(sorted(cur.execute("""SELECT * from scheduler_data""").fetchall(), key=lambda x: x[3]),
                              key=lambda x: x[2])
        clear_layout(self.verticalLayout_3)
        for elem in data_from_db:
            self.verticalLayout_3.addWidget(TaskWidget(self, *elem))
        self.name_edit.setText('')
        con.commit()
        con.close()

    def add_data_to_db(self):
        name = self.name_edit.text()
        data = self.dateEdit.date()
        time = self.timeEdit.time()
        repeat = ''
        if self.every_day_check.isChecked():
            repeat = self.again_box.currentText()

        con = sqlite3.connect('SchedulerApp.db')
        cur = con.cursor()
        out_data = [name, data.toString('dd-MM-yyyy'), time.toString('hh:mm'), repeat]
        cur.execute("""INSERT INTO scheduler_data(name, date, time, repeat) VALUES (?,?,?,?)""", out_data)
        con.commit()
        con.close()
        self.load_tasks()

    def return_to_home(self, left_menu, create_menu, calendar_menu, all_tasks_menu, settings_menu, change_date):
        if time.time() - self.timeout > 0.4:
            self.current_date = datetime.today().date().strftime('%d-%m-%Y') if change_date else self.current_date
            self.slide_left_menu() if left_menu else ''
            self.slide_create_menu() if create_menu else ''
            self.slide_calendar_menu() if calendar_menu else ''
            self.slide_all_tasks_menu() if all_tasks_menu else ''
            self.slide_settings_menu() if settings_menu else ''
            self.main_menu_visible()
            self.timeout = time.time()
        else:
            self.current_date = datetime.today().date().strftime('%d-%m-%Y')
            self.slide_left_menu() if left_menu else ''
            self.slide_create_menu() if create_menu else ''
            self.slide_calendar_menu() if calendar_menu else ''
            self.slide_all_tasks_menu() if all_tasks_menu else ''
            self.slide_settings_menu() if settings_menu else ''
            self.main_menu_visible()
            self.timeout = time.time()
            self.load_day_tasks(self.current_date)

    def load_animations(self):
        self.settings_menu_animation_w = QPropertyAnimation(self.settings_menu, b'maximumWidth')
        self.settings_menu_animation_w.setDuration(350)
        self.settings_menu_animation_w.setEasingCurve(QEasingCurve.InOutCubic)

        self.settings_menu_animation_h = QPropertyAnimation(self.settings_menu, b'maximumHeight')
        self.settings_menu_animation_h.setDuration(350)
        self.settings_menu_animation_h.setEasingCurve(QEasingCurve.InOutCubic)

        self.left_menu_animation = QPropertyAnimation(self.left_menu, b'maximumWidth')
        self.left_menu_animation.setDuration(350)
        self.left_menu_animation.setEasingCurve(QEasingCurve.InOutCubic)

        self.create_menu_animation_w = QPropertyAnimation(self.create_menu, b'maximumWidth')
        self.create_menu_animation_w.setDuration(350)
        self.create_menu_animation_w.setEasingCurve(QEasingCurve.InOutCubic)

        self.create_menu_animation_h = QPropertyAnimation(self.create_menu, b'maximumHeight')
        self.create_menu_animation_h.setDuration(350)
        self.create_menu_animation_h.setEasingCurve(QEasingCurve.InOutCubic)

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
            new_width = 140
        else:
            new_width = 0
        self.left_menu_animation.setStartValue(width)
        self.left_menu_animation.setEndValue(new_width)
        self.left_menu_animation.start()
        self.left_menu_enabled = not self.left_menu_enabled

    def slide_settings_menu(self, recursion=False):
        if time.time() - self.timeout > 0.4:
            width, height = self.settings_menu.width(), self.settings_menu.height()
            now_open = [self.create_menu_enabled, self.calendar_menu_enabled, self.all_tasks_menu_enabled]
            if any(now_open) and not self.settings_menu_enabled:
                self.slide_all_tasks_menu(True) if self.all_tasks_menu_enabled else ''
                self.slide_create_menu(True) if self.create_menu_enabled else ''
                self.slide_calendar_menu(True) if self.calendar_menu_enabled else ''
            if width == 0:
                new_width = self.width()
            else:
                new_width = 0
            self.settings_menu_enabled = not self.settings_menu_enabled
            self.main_menu_visible() if not recursion else ''
            self.settings_menu_animation_w.setStartValue(width)
            self.settings_menu_animation_w.setEndValue(new_width)
            self.settings_menu_animation_w.start()

            if height == 0:
                new_height = self.height()
            else:
                new_height = 0
            self.settings_menu_animation_h.setStartValue(height)
            self.settings_menu_animation_h.setEndValue(new_height)
            self.settings_menu_animation_h.start()
            self.timeout = time.time()

    def slide_create_menu(self, recursion=False, edit=False):
        if time.time() - self.timeout > 0.4:
            width, height = self.create_menu.width(), self.create_menu.height()
            if not edit:
                self.dateEdit.setDate(QDate(*tuple(map(int, self.current_date.split('-')[::-1]))))
                self.timeEdit.setTime(datetime.now().time())
            now_open = [self.create_menu_enabled, self.calendar_menu_enabled, self.all_tasks_menu_enabled,
                        self.settings_menu_enabled]
            if any(now_open) and not self.create_menu_enabled:
                self.slide_all_tasks_menu(True) if self.all_tasks_menu_enabled else ''
                self.slide_calendar_menu(True) if self.calendar_menu_enabled else ''
                self.slide_settings_menu(True) if self.settings_menu_enabled else ''
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

            self.create_menu_animation_h.setStartValue(height)
            self.create_menu_animation_h.setEndValue(new_height)
            self.create_menu_animation_h.start()
            self.timeout = time.time()

    def slide_calendar_menu(self, recursion=False):
        if time.time() - self.timeout > 0.4:
            width, height = self.calendar_menu.width(), self.calendar_menu.height()
            now_open = [self.create_menu_enabled, self.calendar_menu_enabled, self.all_tasks_menu_enabled,
                        self.settings_menu_enabled]
            if any(now_open) and not self.calendar_menu_enabled:
                self.slide_all_tasks_menu(True) if self.all_tasks_menu_enabled else ''
                self.slide_create_menu(True) if self.create_menu_enabled else ''
                self.slide_settings_menu(True) if self.settings_menu_enabled else ''
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
            self.timeout = time.time()

    def slide_all_tasks_menu(self, recursion=False):
        if time.time() - self.timeout > 0.4:
            width, height = self.all_tasks_menu.width(), self.all_tasks_menu.height()
            now_open = [self.create_menu_enabled, self.calendar_menu_enabled, self.all_tasks_menu_enabled,
                        self.settings_menu_enabled]
            if any(now_open) and not self.all_tasks_menu_enabled:
                self.slide_calendar_menu(True) if self.calendar_menu_enabled else ''
                self.slide_create_menu(True) if self.create_menu_enabled else ''
                self.slide_settings_menu(True) if self.settings_menu_enabled else ''
            if width == 0:
                new_width = self.width()
            else:
                new_width = 0
            self.all_tasks_menu_enabled = not self.all_tasks_menu_enabled
            self.main_menu_visible() if not recursion else ''
            self.all_tasks_menu_animation_w.setStartValue(width)
            self.all_tasks_menu_animation_w.setEndValue(new_width)
            self.all_tasks_menu_animation_w.start()
            self.load_tasks()
            self.timeout = time.time()

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
