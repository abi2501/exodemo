
from PyQt6.QtGui import QPainter, QColor, QFont, QPen
from PyQt6.QtCore import Qt, QRectF
from PyQt6.QtWidgets import QWidget


class StepProgressBar(QWidget):
    def __init__(self, steps, percents, current_step, parent=None):
        super().__init__(parent)
        self.steps = steps
        self.percents = percents
        self.current_step = current_step  # 0-based index

        self.setMinimumHeight(120)
        self.setMinimumWidth(700)
        self.bg_color = QColor("#2c2c34")
        self.active_color = QColor("#ff6c1a")
        self.inactive_color = QColor("#444")
        self.text_active = QColor("#fff")
        self.text_inactive = QColor("#888")

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.fillRect(self.rect(), self.bg_color)

        n = len(self.steps)
        margin = 40
        spacing = (self.width() - 2 * margin) // (n - 1)
        y_center = 60
        circle_radius = 14

        # Draw lines between steps
        for i in range(n - 1):
            x1 = margin + i * spacing
            x2 = margin + (i + 1) * spacing
            color = self.active_color if i < self.current_step else self.inactive_color
            pen = QPen(color, 4)
            if i == self.current_step:
                pen.setStyle(Qt.PenStyle.DashLine)
            else:
                pen.setStyle(Qt.PenStyle.SolidLine)
            painter.setPen(pen)
            painter.drawLine(x1, y_center, x2, y_center)

        # Draw steps
        for i, (step, percent) in enumerate(zip(self.steps, self.percents)):
            x = margin + i * spacing
            # Draw circle
            color = self.active_color if i == self.current_step else self.inactive_color
            pen = QPen(color, 2)
            painter.setPen(pen)
            painter.setBrush(color)
            if i % 2 == 0:
                # Even index: draw circle
                painter.drawEllipse(x - circle_radius, y_center - circle_radius, 2 * circle_radius, 2 * circle_radius)
            else:
                # Odd index: draw rectangle
                painter.drawRect(x - circle_radius, y_center - circle_radius, 2 * circle_radius, 2 * circle_radius)

            # Draw percent inside the shape
            font = QFont("Arial", 8, QFont.Weight.Bold)
            painter.setFont(font)
            painter.setPen(self.text_active if i == self.current_step else self.text_inactive)
            percent_text = f"{percent}%"
            shape_rect = QRectF(x - circle_radius, y_center - circle_radius, 2 * circle_radius, 2 * circle_radius)
            painter.drawText(shape_rect, Qt.AlignmentFlag.AlignCenter, percent_text)

            # Draw label below
            font = QFont("Arial", 9)
            painter.setFont(font)
            painter.setPen(self.text_active if i == self.current_step else self.text_inactive)
            label_rect = QRectF(x - 40, y_center + 18, 80, 32)
            painter.drawText(label_rect, Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop, step)