import os

import qdarktheme
from PyQt6.QtGui import QShortcut, QKeySequence, QIcon, QPixmap
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QWidget

from lib.controller.features.predict.predictgait_ctl_ui import PredictGaitControlUI
from lib.controller.features.widgets.exomuscle_ctl_widget import ExoMuscleControlUI
from lib.controller.features.widgets.logger_widget import LoggerUI
from lib.controller.features.widgets.predictgait_graph_widget import PredictGaitGraphUI
from lib.controller.features.widgets.treadmill_ctl_widget import TreadmillControlUI
from lib.controller.util.app_manager import AppManager
from lib.controller.util.helper import resource_path
from lib.controller.views.main_screen import Ui_MainWindow

import res

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.manager = AppManager()

        # UI Component Widgets
        self.treadmill_ctl_widget = TreadmillControlUI()
        self.exomuscle_ctl_widget = ExoMuscleControlUI()
        self.logger_widget = LoggerUI()

        # self.predict_gait_widget = PredictGaitGraphUI()
        self.predict_gait_widget = PredictGaitControlUI()

        self.init_app_settings()
        self.set_slots()

        self.setWindowTitle("MM Treadmill system")


    def init_app_settings(self):

        # Set dark theme
        self.manager.apply_theme()

        styleFile = os.path.join(os.path.split(__file__)[0], resource_path("lib/assets/styles/style.qss"))

        with open(styleFile, 'r') as f:
            style = f.read()

        self.setStyleSheet(style)

        self.ui.treadmillctl_container.layout().addWidget(self.treadmill_ctl_widget)
        self.ui.exomusle_container.layout().addWidget(self.exomuscle_ctl_widget)
        self.ui.log_settings_container.layout().addWidget(self.logger_widget)
        self.ui.predict_gait_wid.layout().addWidget(self.predict_gait_widget)

    def set_slots(self):

        self.ui.connect_btn.clicked.connect(lambda : self.connect_port(self.ui.connect_btn.isChecked()))
        # self.ui.disconnect_btn.clicked.connect(self.disconnect_port)

        # Set Shortcut for close window on ctrl + c
        self.short_cut = QShortcut(QKeySequence("Ctrl+C"), self)
        self.short_cut.activated.connect(self.close)

    def connect_port(self, state):
        if state:
            connection_status = self.get_serial_connection()

            if connection_status:
                self.set_active_mode()
            else:
                self.showDialog("Error", "Unable to make serial connection")
                self.set_deactivate_mode()

            self.set_connection_btn(connection_status)
        else:
            self.set_connection_btn(state)
            self.set_deactivate_mode()

    def set_active_mode(self):
        self.treadmill_ctl_widget.set_tread_controls_enabled(True)
        self.exomuscle_ctl_widget.set_exo_controls_enabled(True)
        self.exomuscle_ctl_widget.setEnabled(True)

    def set_deactivate_mode(self):

        self.treadmill_ctl_widget.set_tread_controls_enabled(False)
        self.exomuscle_ctl_widget.set_exo_controls_enabled(False)



    def set_connection_btn(self, state):
        img = "unlink_active.png" if state else "weui_link-filled.png"
        img = ":images/" + img
        qIcon = QIcon()
        qIcon.addPixmap(QPixmap(img))
        self.ui.connect_btn.setIcon(qIcon)

    def get_serial_connection(self):
        return True

    def showDialog(self, title, description):
        msgBox = QMessageBox()
        msgBox.setText(description)
        msgBox.setWindowTitle(title)
        msgBox.exec()
        return msgBox


    # # def make_connection(self):
    # #
    # #     if self.ui.connect_btn.isChecked():
    # #         self.ui.connect_btn.setEnabled(False)
    # #         self.ui.disconnect_btn.setEnabled(False)
    # #         self.exomuscle_ctl_widget.setEnabled(True)
    # #
    # #     if self.ui.disconnect_btn.isChecked():
    # #         self.ui.connect_btn.setEnabled(True)
    # #
    # #         self.ui.disconnect_btn.setEnabled(False)
    # #         self.exomuscle_ctl_widget.setEnabled(False)
    #
    # def connect_port(self):
    #     print(self.ui.connect_btn.isEnabled())
    #     self.ui.connect_btn.setEnabled(False)
    #     self.ui.disconnect_btn.setEnabled(True)
    #     self.exomuscle_ctl_widget.setEnabled(True)
    # def disconnect_port(self):
    #     self.ui.disconnect_btn.setEnabled(False)
    #     self.ui.connect_btn.setEnabled(True)
    #     self.exomuscle_ctl_widget.setEnabled(False)