import sqlite3
from datetime import datetime
from datetime import date as to_date

from PySide6.QtCore import Qt, QDate, QTime
from PySide6.QtWidgets import QWidget
from GUI.UiTaskWidget import Ui_Form


class TaskWidget(QWidget, Ui_Form):
    def __init__(self, parent, id, name, date, time, accept, repeat):
        super().__init__()
        self.setupUi(self)
        self.name_label.setText(name)
        self.editing = False
        self.parent, self.name, self.id, self.date, self.time, self.accept = parent, name, id, date, time, accept
        self.repeat = repeat
        task_date = to_date(*tuple(map(int, self.date.split('-')[::-1])))
        if self.repeat == 'Ежедневно' and self.date != datetime.today().date().strftime('%d-%m-%Y'):
            print(1)
            self.date = datetime.today().date().strftime('%d-%m-%Y')
            self.accept = False
            self.save()
        elif self.repeat == 'Еженедельно' and abs((datetime.today().date() - task_date).days) > 0 and (
                datetime.today().date() - task_date).days % 7 == 0:
            self.date = datetime.today().date().strftime('%d-%m-%Y')
            self.accept = False
            self.save()
        elif self.repeat == 'Ежемесячно' and abs((datetime.today().date() - task_date).days) > 0 and (
                datetime.today().date().day == task_date.day):
            self.date = datetime.today().date().strftime('%d-%m-%Y')
            self.accept = False
            self.save()
        self.data_and_time.setText(f'{date} {time}' if self.parent.all_tasks_menu_enabled else f'{time}')
        if self.date != datetime.today().date().strftime('%d-%m-%Y') or (
                self.parent.current_date != self.date) or self.parent.all_tasks_menu_enabled:
            self.accept_btn.hide()

        self.setMaximumHeight(100)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.repeat_label.setMaximumWidth(0) if not self.repeat else ''

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
        self.edit_btn.clicked.connect(self.edit_task)
        self.parent.add_data_btn.clicked.connect(self.save_edited_task)
        self.parent.create_task_btn.clicked.connect(self.cancel_edited_task)
        self.parent.calendar_btn.clicked.connect(lambda: self.cancel_edited_task(True))
        self.parent.all_tasks_btn.clicked.connect(lambda: self.cancel_edited_task(True))

    # def change_theme(self, theme):
    #
    def edit_task(self):
        self.parent.add_data_btn.setText('Сохранить')
        self.parent.dateEdit.setDate(QDate(*tuple(map(int, self.date.split('-')[::-1]))))
        self.parent.timeEdit.setTime(QTime(*tuple(map(int, self.time.split(':')))))
        self.parent.every_day_check.setChecked(True if self.repeat else False)
        self.parent.again_box.setCurrentText(self.repeat) if self.repeat else ''
        self.parent.slide_create_menu(edit=True)
        self.parent.name_edit.setText(self.name)
        self.editing = True

    def save(self):
        con = sqlite3.connect('SchedulerApp.db')
        cur = con.cursor()
        cur.execute(f"""UPDATE scheduler_data SET name='{self.name}', date='{self.date}', 
                    time='{self.time}', accept={self.accept} WHERE id={self.id}""")
        con.commit()
        con.close()

    def cancel_edited_task(self, missclick=False):
        if self.editing:
            self.parent.load_tasks()
            self.parent.return_to_home(self.parent.left_menu_enabled,
                                       self.parent.create_menu_enabled,
                                       self.parent.calendar_menu_enabled,
                                       self.parent.all_tasks_menu_enabled,
                                       False) if not missclick else ''
            self.editing = False
            self.parent.load_tasks()
            self.parent.load_day_tasks(self.parent.current_date)

            self.parent.every_day_check.setChecked(False)
            self.parent.add_data_btn.setText('Добавить')
            self.parent.name_edit.setText('')

    def save_edited_task(self):
        if self.editing:
            self.name = self.parent.name_edit.text()
            self.date = self.parent.dateEdit.date().toString('dd-MM-yyyy')
            self.time = self.parent.timeEdit.time().toString()

            con = sqlite3.connect('SchedulerApp.db')
            cur = con.cursor()
            cur.execute(f"""UPDATE scheduler_data 
            SET name='{self.name}', date='{self.date}', 
            time='{self.time}' WHERE id={self.id}""")
            cur.execute(f"""DELETE FROM scheduler_data WHERE id={self.id}""")
            con.commit()
            con.close()
            self.parent.load_tasks()
            self.parent.return_to_home(self.parent.left_menu_enabled,
                                       self.parent.create_menu_enabled,
                                       self.parent.calendar_menu_enabled,
                                       self.parent.all_tasks_menu_enabled,
                                       self.parent.settings_menu_enabled,
                                       False)
            self.editing = False
            self.parent.load_tasks()
            self.parent.load_day_tasks(self.parent.current_date)

            self.parent.every_day_check.setChecked(False)
            self.parent.add_data_btn.setText('Добавить')
            self.parent.name_edit.setText('')
            self.parent.load_tasks_notification()

    def delete_task(self):
        con = sqlite3.connect('SchedulerApp.db')
        cur = con.cursor()
        cur.execute(f"""DELETE FROM scheduler_data WHERE id={self.id}""")
        con.commit()
        con.close()
        self.parent.load_tasks()
        self.parent.load_day_tasks(self.parent.current_date)
        self.parent.load_tasks_notification()

    def accept_task(self):
        self.accept = not self.accept
        con = sqlite3.connect('SchedulerApp.db')
        cur = con.cursor()
        cur.execute(f"""UPDATE scheduler_data SET accept={self.accept} WHERE id={self.id}""")
        con.commit()
        con.close()
        self.parent.load_tasks()
        self.parent.load_day_tasks(self.parent.current_date)
        self.parent.load_tasks_notification()
