from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel
from PyQt6.QtCore import pyqtSignal, Qt, QPropertyAnimation, QRect, QEasingCurve

class ClickableAnimatedWidget(QWidget):
    clicked = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: #AED6F1; border-radius: 10px;")
        self.setFixedSize(200, 100)

        layout = QVBoxLayout(self)
        label = QLabel("Click Me", self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.animate_click()
            self.clicked.emit()

    def animate_click(self):
        original = self.geometry()
        shrink = QRect(
            original.x() + 10,
            original.y() + 5,
            original.width() - 20,
            original.height() - 10,
        )

        self.anim_shrink = QPropertyAnimation(self, b"geometry")
        self.anim_shrink.setDuration(120)
        self.anim_shrink.setStartValue(original)
        self.anim_shrink.setEndValue(shrink)
        self.anim_shrink.setEasingCurve(QEasingCurve.Type.InOutQuad)
        self.anim_shrink.finished.connect(lambda: self.animate_expand(original))
        self.anim_shrink.start()

    def animate_expand(self, original):
        self.anim_expand = QPropertyAnimation(self, b"geometry")
        self.anim_expand.setDuration(180)
        self.anim_expand.setStartValue(self.geometry())
        self.anim_expand.setEndValue(original)
        self.anim_expand.setEasingCurve(QEasingCurve.Type.OutBounce)
        self.anim_expand.start()