from PySide6.QtGui import QColor
from PySide6.QtWidgets import QCalendarWidget


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