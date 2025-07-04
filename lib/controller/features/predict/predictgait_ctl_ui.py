import os

from PyQt6.QtWidgets import QWidget

from lib.controller.features.predict.predictgait_stack_one import PredictGaitStackPageOne
from lib.controller.util.helper import resource_path
from lib.controller.views.ui.predictgait_ctl_ui import Ui_predict_ctl_wid
class PredictGaitControlUI(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_predict_ctl_wid()
        self.ui.setupUi(self)

        self.stack_page_one = PredictGaitStackPageOne()

        self.ui.page_one.layout().addWidget(self.stack_page_one)

        self.init_settings()

    def init_settings(self):

        styleFile = os.path.join(os.path.split(__file__)[0], resource_path("lib/assets/styles/predict_styles.qss"))

        with open(styleFile, 'r') as f:
            style = f.read()

        self.setStyleSheet(style)