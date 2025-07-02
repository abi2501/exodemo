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

        self.play_btn = ClickFilter(self.ui.play_widget)
        self.ui.play_widget.installEventFilter(self.play_btn)

        self.play_btn.clicked.connect(self.play_btn_click)

        self.init_settings()

        self.set_tread_controls_enabled(False)

    def play_btn_click(self, state):

        if self.ui.play_widget.isEnabled():
            self.play_btn.animate_click()

        self.set_tread_ui(state)

    def set_tread_ui(self, state):

        if state:
            # Set play mode
            self.ui.play_widget.setStyleSheet("""background-color:#D82222""")
            self.ui.emergent_stp_wid.setStyleSheet("""background-color:#D82222""")
            img = ":images/" + "pause_rect.png"
        else:
            # Set pause mode
            self.ui.play_widget.setStyleSheet("""background-color:#85CC17""")
            self.ui.emergent_stp_wid.setStyleSheet("""background-color:#2C2D33""")
            img = ":images/" + "play.png"

        self.ui.start_btn.setPixmap(QPixmap(img))

    def set_tread_controls_enabled(self, state):
        self.ui.play_widget.setEnabled(state)

    def init_settings(self):

        styleFile = os.path.join(os.path.split(__file__)[0], resource_path("lib/assets/styles/tread_styles.qss"))

        with open(styleFile, 'r') as f:
            style = f.read()

        self.setStyleSheet(style)

    #
    # def set_slots(self):
    #     self.ui.play_widget.clicked.connect(self.play_btn_click)