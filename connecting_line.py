from PyQt6.QtWidgets import QLabel, QApplication
from PyQt6.QtGui import QPixmap, QPainter, QPainterPath
from PyQt6.QtCore import Qt, QSize
import sys
import res
def rounded_pixmap(pixmap, radius):
    size = QSize(radius * 2, radius * 2)
    rounded = QPixmap(size)
    rounded.fill(Qt.GlobalColor.transparent)

    painter = QPainter(rounded)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing)
    path = QPainterPath()
    path.addEllipse(0, 0, size.width(), size.height())
    painter.setClipPath(path)
    scaled = pixmap.scaled(size, Qt.AspectRatioMode.KeepAspectRatioByExpanding, Qt.TransformationMode.SmoothTransformation)
    painter.drawPixmap(0, 0, scaled)
    painter.end()
    return rounded

app = QApplication(sys.argv)
label = QLabel()
original_pixmap = QPixmap(":images/hand.png")  # Your image path
label.setPixmap(rounded_pixmap(original_pixmap, 50))  # 50 radius = 100x100
label.setFixedSize(100, 100)
label.setStyleSheet("background: transparent;")
label.show()
sys.exit(app.exec())
