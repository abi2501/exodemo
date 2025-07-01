import os

from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QWidget

from lib.controller.util.helper import resource_path
from lib.controller.views.custom.clickablewidget import ClickableWidget, ClickFilter
from lib.controller.views.ui.treadmill_ctl_ui import Ui_tread_ctl_widget_form

class TreadmillControlUI(QWidget):

    clicked = pyqtSignal()

    def __init__(self):

        super().__init__()
        self.ui = Ui_tread_ctl_widget_form()
        self.ui.setupUi(self)

        self.click_filter = ClickFilter(self.ui.play_widget)
        self.ui.play_widget.installEventFilter(self.click_filter)

        self.click_filter.clicked.connect(self.play_btn_click)
        self.ui.start_btn.clicked.connect(self.play_btn_click)

        self.init_settings()

        self.set_tread_controls_enabled(False)

    def play_btn_click(self, state):
        if self.ui.play_widget.isEnabled():
            print("Clicke engen ", state)
            self.click_filter.animate_click()
            self.set_tread_ui(state)

    def set_tread_ui(self, state):
        img = "play.png" if state else "pause_rect.png"
        img = ":images/" + img
        qIcon = QIcon()
        qIcon.addPixmap(QPixmap(img))

        if state:
            self.ui.play_widget.setStyleSheet("""background-color:#D82222""")
        else:
            self.ui.play_widget.setStyleSheet("""background-color:#85CC17""")

        self.ui.start_btn.setIcon(qIcon)

    def set_tread_controls_enabled(self, state):
        # self.setEnabled(state)
        self.ui.play_widget.setEnabled(state)
        # self.ui.start_btn

    def init_settings(self):

        styleFile = os.path.join(os.path.split(__file__)[0], resource_path("lib/assets/styles/tread_styles.qss"))

        with open(styleFile, 'r') as f:
            style = f.read()

        self.setStyleSheet(style)

    #
    # def set_slots(self):
    #     self.ui.play_widget.clicked.connect(self.play_btn_click)