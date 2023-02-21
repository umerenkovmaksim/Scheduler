from PySide6.QtCore import Qt, QRect, QPropertyAnimation, QEasingCurve, Property
from PySide6.QtGui import QPainter, QColor
from PySide6.QtWidgets import QCheckBox


class Switcher(QCheckBox):
    def __init__(self, parent=None, width=45, height=20, bg_color="#777", circle_color="DDD", active_color="#00bcff"):
        QCheckBox.__init__(self, parent)

        self.parent = parent
        self.setFixedSize(width, height)
        self.setCursor(Qt.PointingHandCursor)

        self.current_pos = 2

        self.animation = QPropertyAnimation(self, b'circle_position', self)
        self.animation.setEasingCurve(QEasingCurve.InOutCubic)
        self.animation.setDuration(400)

        self.stateChanged.connect(self.start_animation)

        self.bg_color, self.circle_color, self.active_color = bg_color, circle_color, active_color

    @Property(float)
    def circle_position(self):
        return self.current_pos

    @circle_position.setter
    def circle_position(self, pos):
        self.current_pos = pos
        self.update()

    def start_animation(self, value):
        self.animation.stop()
        if value:
            self.animation.setEndValue(self.width() - self.height() + 2)
        else:
            self.animation.setEndValue(3)
        self.animation.start()

    def hitButton(self, pos):
        return self.contentsRect().contains(pos)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)

        rect = QRect(0, 0, self.width(), self.height())

        if not self.isChecked():
            painter.setBrush(QColor(self.bg_color))
            painter.drawRoundedRect(0, 0, rect.width(), self.height(), self.height() / 2, self.height() / 2)

            painter.setBrush(QColor(self.circle_color))
            painter.drawEllipse(self.current_pos, 2, self.height() - 4, self.height() - 4)
        else:
            painter.setBrush(QColor(self.active_color))
            painter.drawRoundedRect(0, 0, rect.width(), self.height(), self.height() / 2, self.height() / 2)

            painter.setBrush(QColor(self.circle_color))
            painter.drawEllipse(self.current_pos, 2, self.height() - 4, self.height() - 4)

        painter.end()
