from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel
from lib.controller.progressbar.led_circle import LedCircle, ConnectorLine
from lib.controller.progressbar.step_progress_bar import StepProgressBar
from lib.controller.views.ui.predict_gait_stack_one_ui import Ui_predictgait_stack_page_one

class PredictGaitStackPageOne(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_predictgait_stack_page_one()
        self.ui.setupUi(self)

        steps = [
            "Heel\nStrike", "Loading\nResponse", "Midstance", "Terminal\nStance",
            "Preswing", "Initial &\nMid-swing", "Terminal\nswing"
        ]
        percents = [15, 20, 10, 10, 15, 15, 15]
        current_step = 3  # 0-based index (Terminal Stance)

        self.progress = StepProgressBar(steps, percents, current_step)
        self.ui.pbar_container_wid.layout().addWidget(self.progress)


        strike_img_1 = ":images/strikes/strike_img_1.png"
        strike_img_2 = ":images/strikes/strike_img_2.png"
        strike_img_3 = ":images/strikes/strike_img_3.png"
        strike_img_33 = ":images/strikes/strike_image_3.png"
        strike_img_4 = ":images/strikes/strike_img_4.png"
        strike_img_5 = ":images/strikes/strike_img_5.png"
        strike_img_6 = ":images/strikes/strike_img_6.png"
        strike_img_7 = ":images/strikes/strike_img_7.png"

        pixmap = QPixmap(strike_img_1)
        self.ui.strike_image_1.setPixmap(pixmap)
        self.ui.strike_image_1.setScaledContents(True)
        self.ui.strike_image_1.setMaximumWidth(100)

        pixmap = QPixmap(strike_img_1)
        self.ui.strike_image_1.setPixmap(pixmap)
        self.ui.strike_image_1.setScaledContents(True)
        self.ui.strike_image_1.setMaximumWidth(100)

        pixmap = QPixmap(strike_img_2)
        self.ui.strike_image_2.setPixmap(pixmap)
        self.ui.strike_image_2.setScaledContents(True)
        self.ui.strike_image_2.setMaximumWidth(100)

        pixmap = QPixmap(strike_img_33)
        self.ui.strike_image_3.setPixmap(pixmap)
        self.ui.strike_image_3.setScaledContents(True)
        self.ui.strike_image_3.setMaximumWidth(100)

        pixmap = QPixmap(strike_img_4)
        self.ui.strike_image_4.setPixmap(pixmap)
        self.ui.strike_image_4.setScaledContents(True)
        self.ui.strike_image_4.setMaximumWidth(100)

        pixmap = QPixmap(strike_img_5)
        self.ui.strike_image_5.setPixmap(pixmap)
        self.ui.strike_image_5.setScaledContents(True)
        self.ui.strike_image_5.setMaximumWidth(100)

        pixmap = QPixmap(strike_img_6)
        self.ui.strike_image_6.setPixmap(pixmap)
        self.ui.strike_image_6.setScaledContents(True)
        self.ui.strike_image_6.setMaximumWidth(100)

        pixmap = QPixmap(strike_img_7)
        self.ui.strike_image_7.setPixmap(pixmap)
        self.ui.strike_image_7.setScaledContents(True)
        self.ui.strike_image_7.setMaximumWidth(100)

    def _buildLabel(self, text, widget_ref):
        label = QLabel(text)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("color: white; font-size: 9pt;")
        label.setFixedWidth(widget_ref.width())
        return label