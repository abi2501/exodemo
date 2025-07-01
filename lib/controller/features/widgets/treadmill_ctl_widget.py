import os

from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtWidgets import QWidget

from lib.controller.util.helper import resource_path
from lib.controller.views.custom.clickablewidget import ClickableWidget, ClickFilter
from lib.controller.views.ui.treadmill_ctl_ui import Ui_tread_ctl_widget_form
#
# class ClickableWidget(QWidget):
#     clicked = pyqtSignal()
#
#
#     def mousePressEvent(self, event):
#         print("Click event custom")
#         if event.button() == Qt.MouseButton.LeftButton:
#             self.clicked.emit()
#
#

class TreadmillControlUI(QWidget):
    clicked = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_tread_ctl_widget_form()
        self.ui.setupUi(self)

        # placeholder = self.ui.play_widget  # QWidget placeholder from .ui
        # self.custom = ClickableWidget()
        self.click_filter = ClickFilter(self.ui.play_widget)
        self.ui.play_widget.installEventFilter(self.click_filter)
        self.click_filter.clicked.connect(self.play_btn_click)
        self.ui.start_btn.clicked.connect(self.play_btn_click)

        # self.ui.play_widget.layout().addWidget(self.custom)
        # self.custom.clicked.connect(self.play_btn_click)


        self.set_tread_controls_enabled(False)
        self.init_settings()
        # self.set_slots()


    def play_btn_click(self):
        print("Clicke engen")
        self.click_filter.animate_click()

    def set_tread_controls_enabled(self, state):
        self.setEnabled(state)
        self.ui.play_widget.setEnabled(True)

    def init_settings(self):

        styleFile = os.path.join(os.path.split(__file__)[0], resource_path("lib/assets/styles/tread_styles.qss"))

        with open(styleFile, 'r') as f:
            style = f.read()

        self.setStyleSheet(style)

    #
    # def set_slots(self):
    #     self.ui.play_widget.clicked.connect(self.play_btn_click)