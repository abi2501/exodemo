import os

from PyQt6.QtWidgets import QWidget, QVBoxLayout

from lib.controller.util.helper import resource_path
from lib.controller.views.ui.exomusle_ctl_ui import Ui_exo_ctl_widget_form


class ExoMuscleControlUI(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_exo_ctl_widget_form()
        self.ui.setupUi(self)

        self.init_settings()

    def init_settings(self):

        self.setEnabled(False)


        styleFile = os.path.join(os.path.split(__file__)[0], resource_path("lib/assets/styles/exo_styles.qss"))

        with open(styleFile, 'r') as f:
            style = f.read()

        self.setStyleSheet(style)
        # self.ui.stackedWidgetPage1.setStyleSheet("""background-color: #35363F;""")
        # self.ui.tabWidget.tabBar().hide()

        # self.lout = QVBoxLayout()
        # self.lout.setContentsMargins(0,0,0,0)
        # self.ui.left_tab.setLayout(self.lout)
        # self.ui.left_tab.layout().setContentsMargins(0,0,0,0)

