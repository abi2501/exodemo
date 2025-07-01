# clickablewidget.py
import os

from PyQt5 import QtWidgets
from PyQt6 import QtGui, QtCore
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QSpacerItem, QSizePolicy, QToolButton, QGraphicsOpacityEffect
from PyQt6.QtCore import pyqtSignal, Qt, QRect, QPropertyAnimation, QEasingCurve, QObject, QEvent

from lib.controller.util.helper import resource_path


class ClickFilter(QObject):
    clicked = pyqtSignal(bool)
    isChecked = False

    def __init__(self, target_widget):
        super().__init__()
        self.target = target_widget

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.MouseButtonPress and event.button() == Qt.MouseButton.LeftButton:
            # print("Widget clicked!", self.isChecked)
            self.clicked.emit(not self.isChecked)
            self.isChecked = not self.isChecked
            return True  # Optional: consume event
        return False

    def animate_click(self):
        original = self.target.geometry()
        shrink = QRect(
            original.x() + 5,
            original.y() + 5,
            original.width() - 10,
            original.height() - 10,
        )

        self.anim_shrink = QPropertyAnimation(self.target, b"geometry")
        self.anim_shrink.setDuration(120)
        self.anim_shrink.setStartValue(original)
        self.anim_shrink.setEndValue(shrink)
        self.anim_shrink.setEasingCurve(QEasingCurve.Type.InOutQuad)

        self.anim_shrink.finished.connect(lambda: self.animate_expand(original))
        self.anim_shrink.start()

    def animate_expand(self, original):
        self.anim_expand = QPropertyAnimation(self.target, b"geometry")
        self.anim_expand.setDuration(180)
        self.anim_expand.setStartValue(self.target.geometry())
        self.anim_expand.setEndValue(original)
        self.anim_expand.setEasingCurve(QEasingCurve.Type.OutBounce)
        self.anim_expand.start()


class ClickableWidget(QWidget):
    clicked = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.vbox = QVBoxLayout()
        spacerItem2 = QSpacerItem(20, 98, QSizePolicy.Policy.Minimum,
                                           QSizePolicy.Policy.Expanding)
        self.vbox.addItem(spacerItem2)
        self.start_btn = QToolButton()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/play.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.start_btn.setIcon(icon)
        self.start_btn.setObjectName("start_btn")
        self.vbox.addWidget(self.start_btn, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.vbox.addItem(spacerItem2)
        self.setLayout(self.vbox)


    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit()

    def animate_click(self):
        original_rect = self.geometry()

        # Create a slightly smaller rectangle
        shrink_rect = QRect(
            original_rect.x() + 10,
            original_rect.y() + 5,
            original_rect.width() - 20,
            original_rect.height() - 10,
        )

        # Shrink animation
        self.shrink_anim = QPropertyAnimation(self, b"geometry")
        self.shrink_anim.setDuration(120)
        self.shrink_anim.setStartValue(original_rect)
        self.shrink_anim.setEndValue(shrink_rect)
        self.shrink_anim.setEasingCurve(QEasingCurve.Type.InOutQuad)

        # When shrink finishes, restore to original size
        self.shrink_anim.finished.connect(lambda: self.animate_expand(original_rect))
        self.shrink_anim.start()

    def animate_expand(self, original_rect):
        self.expand_anim = QPropertyAnimation(self, b"geometry")
        self.expand_anim.setDuration(180)
        self.expand_anim.setStartValue(self.geometry())
        self.expand_anim.setEndValue(original_rect)
        self.expand_anim.setEasingCurve(QEasingCurve.Type.OutBounce)
        self.expand_anim.start()

