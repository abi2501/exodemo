

from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QColor, QPen, QFont
from PyQt6.QtCore import Qt, QRectF

class LedCircle(QWidget):
    def __init__(self, text='', color='#444444', diameter=20):
        super().__init__()
        self.text = text
        self.color = QColor(color)
        self.diameter = diameter
        self.setFixedSize(diameter, 24)  # Remove extra text width

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
    def __init__(self, text='', color='#444444', size=QRectF(0, 0, 30, 20)):
        super().__init__()
        self.text = text
        self.color = QColor(color)
        self.size = size
        self.setFixedSize(int(size.width()), int(size.height()))

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
    def __init__(self, color="#f97316", thickness=3, length=20):
        super().__init__()
        self.color = QColor(color)
        self.thickness = thickness
        self.length = length
        self.setFixedSize(length, 24)  # Match StepBox height

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        pen = QPen(self.color)
        pen.setWidth(self.thickness)
        pen.setCapStyle(Qt.PenCapStyle.FlatCap)
        painter.setPen(pen)
        y = self.height() // 2
        painter.drawLine(0, y, self.width(), y)


from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout

class StepProgressBar(QWidget):
    def __init__(self, steps=10, percentage=15):
        super().__init__()
        self.steps = steps
        self.percentage = percentage
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.updateBar()

    def updateBar(self):
        self.clearLayout()

        active_index = int((self.percentage / 100) * self.steps)

        # First step: circle
        circle = LedCircle(text=f"{self.percentage}%", color="#f97316" if 0 <= active_index else "#444444")
        self.layout.addWidget(circle)

        for i in range(1, self.steps):
            self.layout.addWidget(ConnectorLine())

            active = i <= active_index
            box = StepBox(
                text=f"{self.percentage}%" if active else "",
                color="#f97316" if active else "#444444"
            )
            self.layout.addWidget(box)

    def clearLayout(self):
        while self.layout.count():
            item = self.layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.setParent(None)

    def setPercentage(self, percentage):
        self.percentage = percentage
        self.updateBar()



def main():
    app = QApplication([])
    window = QWidget()
    layout = QHBoxLayout(window)
    layout.setContentsMargins(0,0,0,0)
    layout.setSpacing(0)
    progress = StepProgressBar(steps=10, percentage=15)
    layout.addWidget(progress)

    window.setWindowTitle("Modular Progress Bar")
    window.resize(600, 80)
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
