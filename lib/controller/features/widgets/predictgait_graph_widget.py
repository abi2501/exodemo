from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPixmap, QPainter, QPainterPath
from PyQt6.QtWidgets import QWidget

from lib.controller.features.predictgait.predictgait_strike_ui import PredictGaitStrikeUI

from lib.controller.views.ui.predict_graph_ui import Ui_predict_gait_content


def rounded_pixmap(pixmap, radius):
    size = QSize(radius * 2, radius * 2)
    rounded = QPixmap(size)
    rounded.fill(Qt.GlobalColor.transparent)

    painter = QPainter(rounded)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing)
    path = QPainterPath()
    path.addEllipse(0, 0, size.width(), size.height())
    painter.setClipPath(path)
    scaled = pixmap.scaled(size, Qt.AspectRatioMode.KeepAspectRatioByExpanding, Qt.TransformationMode.SmoothTransformation)
    painter.drawPixmap(0, 0, scaled)
    painter.end()
    return rounded


class PredictGaitGraphUI(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_predict_gait_content()
        self.ui.setupUi(self)

        self.strike_images_ui = PredictGaitStrikeUI()

        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.strike_image_container.layout().addWidget(self.strike_images_ui)

        original_pixmap = QPixmap()  # Your image path
        self.ui.cpbar_1.setPixmap(rounded_pixmap(original_pixmap, 50))  # 50 radius = 100x100
        self.ui.cpbar_1.setFixedSize(100, 100)
        self.ui.cpbar_1.setStyleSheet("""background-color: #2ecc71;
    border-radius: 10px;
    color: white;""")