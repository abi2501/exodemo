from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtGui import QColor, QPainter, QPen, QBrush, QFont
from PyQt6.QtCore import Qt, QRectF

class ProgressBar(QWidget):
    def __init__(self, percentage=15, steps=10):
        super().__init__()
        self.percentage = percentage
        self.steps = steps
        self.setMinimumHeight(60)
        self.setStyleSheet("background-color: #2c2f3a;")  # Dark background

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        width = self.width()
        height = self.height()
        spacing = 10
        total_width = width - (self.steps - 1) * spacing - 20
        step_width = total_width / self.steps
        circle_radius = 6
        rect_width = 20
        rect_height = 20

        active_index = int((self.percentage / 100) * self.steps)

        # Draw connecting line
        painter.setPen(QPen(QColor("#555555"), 3))
        start_x = int(10 + circle_radius)
        end_x = int((self.steps - 1) * (step_width + spacing) + 10 + rect_width // 2)
        mid_y = int(height // 2)
        painter.drawLine(start_x, mid_y, end_x, mid_y)

        for i in range(self.steps):
            x = int(i * (step_width + spacing) + 10)
            y = int(height // 2 - rect_height // 2)

            if i == 0:
                # First circle
                painter.setBrush(QColor("#f97316") if i <= active_index else QColor("#444444"))
                painter.setPen(Qt.PenStyle.NoPen)
                painter.drawEllipse(x, int(height // 2 - circle_radius), circle_radius * 2, circle_radius * 2)

                # Draw percentage text next to the circle
                if i == active_index:
                    painter.setPen(Qt.GlobalColor.white)
                    painter.setFont(QFont("Arial", 8))
                    painter.drawText(x + 15, int(height // 2 + 4), f"{self.percentage}%")
            else:
                is_active = i <= active_index
                color = "#f97316" if is_active else "#444444"
                painter.setBrush(QColor(color))
                painter.setPen(Qt.PenStyle.NoPen)
                painter.drawRoundedRect(QRectF(x, y, rect_width, rect_height), 4, 4)

                if is_active:
                    # Draw percentage text inside the rectangle
                    painter.setPen(Qt.GlobalColor.white)
                    painter.setFont(QFont("Arial", 7))
                    text = f"{self.percentage}%"
                    text_rect = QRectF(x, y, rect_width, rect_height)
                    painter.drawText(text_rect, Qt.AlignmentFlag.AlignCenter, text)
def main():
    app = QApplication([])
    window = QWidget()
    layout = QVBoxLayout(window)

    progress = ProgressBar(percentage=15, steps=10)
    layout.addWidget(progress)

    window.setWindowTitle("Custom Progress with Connecting Line")
    window.resize(420, 80)
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
