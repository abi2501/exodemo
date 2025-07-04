from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout,
    QHBoxLayout, QSizePolicy
)
from PyQt6.QtGui import QPainter, QColor, QPen, QFont
from PyQt6.QtCore import Qt, QRectF


class LedCircle(QWidget):
    def __init__(self, text='', color='#444444', diameter=20, height=30):
        super().__init__()
        self.text = text
        self.color = QColor(color)
        self.diameter = diameter
        self.setFixedSize(diameter, height)

    def setText(self, text):
        self.text = text
        self.update()

    def setColor(self, color):
        self.color = QColor(color)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(self.color)
        painter.setPen(Qt.PenStyle.NoPen)

        x = (self.width() - self.diameter) // 2
        y = self.height() // 2 - self.diameter // 2
        painter.drawEllipse(x, y, self.diameter, self.diameter)

        if self.text:
            painter.setPen(Qt.GlobalColor.white)
            painter.setFont(QFont("Arial", 8))
            painter.drawText(self.rect(), Qt.AlignmentFlag.AlignCenter, self.text)




class StepBox(QWidget):
    def __init__(self, text='', color='#444444', width=30, height=24):
        super().__init__()
        self.text = text
        self.color = QColor(color)
        self.setFixedSize(width, height)

    def setText(self, text):
        self.text = text
        self.update()

    def setColor(self, color):
        self.color = QColor(color)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(self.color)
        painter.setPen(Qt.PenStyle.NoPen)

        painter.drawRoundedRect(self.rect(), 4, 4)

        if self.text:
            painter.setPen(Qt.GlobalColor.white)
            painter.setFont(QFont("Arial", 7))
            painter.drawText(self.rect(), Qt.AlignmentFlag.AlignCenter, self.text)


class ConnectorLine(QWidget):
    def __init__(self, color="#555555", thickness=3, length=20):
        super().__init__()
        self.color = QColor(color)
        self.thickness = thickness
        self.length = length
        self.setFixedSize(length, 24)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        pen = QPen(self.color)
        pen.setWidth(self.thickness)
        pen.setCapStyle(Qt.PenCapStyle.FlatCap)
        painter.setPen(pen)
        y = self.height() // 2
        painter.drawLine(0, y, self.width(), y)


class StepProgressBar(QWidget):
    def __init__(self, steps=10, percentage=15):
        super().__init__()
        self.steps = steps
        self.percentage = percentage

        # Two rows: progress bar + labels
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(4)

        self.progress_row = QHBoxLayout()
        self.progress_row.setSpacing(0)
        self.label_row = QHBoxLayout()
        self.label_row.setSpacing(0)

        self.main_layout.addLayout(self.progress_row)
        self.main_layout.addLayout(self.label_row)

        self.updateBar()

    def updateBar(self):
        self.clearLayout(self.progress_row)
        self.clearLayout(self.label_row)

        active_index = int((self.percentage / 100) * self.steps)

        # First step: Circle + Label
        circle_color = "#f97316" if 0 <= active_index else "#444444"
        circle = LedCircle(text=f"{self.percentage}%" if 0 <= active_index else '', color=circle_color)
        self.progress_row.addWidget(circle)
        self.label_row.addWidget(self._buildLabel("Start", circle))

        for i in range(1, self.steps):
            # Connecting line
            self.progress_row.addWidget(ConnectorLine(color="#f97316" if i <= active_index else "#444444"))
            self.label_row.addSpacing(20)  # same as connector length

            # Step box
            active = i <= active_index
            box = StepBox(
                text=f"{self.percentage}%" if active else '',
                color="#f97316" if active else "#444444"
            )
            self.progress_row.addWidget(box)
            self.label_row.addWidget(self._buildLabel(f"Step {i + 1}", box))

    def _buildLabel(self, text, widget_ref):
        label = QLabel(text)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("color: white; font-size: 9pt;")
        label.setFixedWidth(widget_ref.width())
        return label

    def clearLayout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.setParent(None)

    def setPercentage(self, percentage):
        self.percentage = percentage
        self.updateBar()
