from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget

from lib.controller.views.ui.predict_image_stream_ui import Ui_strike_image_container
import res
class PredictGaitStrikeUI(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_strike_image_container()
        self.ui.setupUi(self)

        strike_img_1 = ":images/strikes/strike_img_1.png"
        strike_img_2 = ":images/strikes/strike_img_2.png"
        strike_img_3 = ":images/strikes/strike_img_3.png"
        strike_img_4 = ":images/strikes/strike_img_4.png"
        strike_img_5 = ":images/strikes/strike_img_5.png"
        strike_img_6 = ":images/strikes/strike_img_6.png"
        strike_img_7 = ":images/strikes/strike_img_7.png"

        pixmap = QPixmap(strike_img_1)
        self.ui.strike_image_1.setPixmap(pixmap)
        self.ui.strike_image_1.setScaledContents(True)
        self.ui.strike_image_1.setMaximumWidth(100)

        pixmap = QPixmap(strike_img_2)
        self.ui.strike_image_2.setPixmap(pixmap)
        self.ui.strike_image_2.setScaledContents(True)
        self.ui.strike_image_2.setMaximumWidth(100)

        pixmap = QPixmap(strike_img_3)
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