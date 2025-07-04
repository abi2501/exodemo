import os

from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import QWidget, QVBoxLayout

from lib.controller.util.helper import resource_path
from lib.controller.views.custom.clickablewidget import ClickFilter
from lib.controller.views.ui.exomusle_ctl_ui import Ui_exo_ctl_widget_form


class ExoMuscleControlUI(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_exo_ctl_widget_form()
        self.ui.setupUi(self)

        self.play_btn = ClickFilter(self.ui.play_widget)
        self.ui.play_widget.installEventFilter(self.play_btn)

        self.play_btn.clicked.connect(self.play_btn_click)

        self.ui.exo_left_btn.clicked.connect(lambda : self.set_stack_widget(0))
        self.ui.exo_right_btn.clicked.connect(lambda : self.set_stack_widget(1))

        self.init_settings()
        self.set_exo_controls_enabled(False)

    def play_btn_click(self, state):
        if self.ui.play_widget.isEnabled():
            # self.play_btn.animate_click()
            self.set_exo_ui(state)

    def set_stack_widget(self, idx):

        if idx == 0:
            self.ui.exo_left_btn.setEnabled(False)
            self.ui.exo_right_btn.setEnabled(True)
        elif idx == 1:
            self.ui.exo_left_btn.setEnabled(True)
            self.ui.exo_right_btn.setEnabled(False)

        self.ui.stackedWidget.setCurrentIndex(idx)

    def set_exo_ui(self, state):

        if state:
            # Set play mode
            self.ui.play_widget.setStyleSheet("""background-color:#D82222""")
            img = ":images/" + "pause_rect.png"
            increImg = ":images/" + "carbon_add-filled_active.png"
            decreImg = ":images/" + "lsicon_minus_active-filled.png"

        else:
            # Set pause mode
            self.ui.play_widget.setStyleSheet("""background-color:#85CC17""")
            img = ":images/" + "play.png"
            increImg = ":images/" + "carbon_add-filled.png"
            decreImg = ":images/" + "lsicon_minus-filled.png"

        self.ui.start_btn.setPixmap(QPixmap(img))

        qIconIncrement = QIcon()
        qIconDecrement = QIcon()
        qIconIncrement.addPixmap(QPixmap(increImg))
        qIconDecrement.addPixmap(QPixmap(decreImg))

        self.ui.left_pressure_increment_btn.setIcon(qIconIncrement)
        self.ui.left_pressure_decrement_btn.setIcon(qIconDecrement)
        self.ui.left_activeph_increment_btn.setIcon(qIconIncrement)
        self.ui.left_activeph_decrement_btn.setIcon(qIconDecrement)
        self.ui.left_activedur_increment_btn.setIcon(qIconIncrement)
        self.ui.left_activedur_decrement_btn.setIcon(qIconDecrement)
        self.ui.left_maxdur_increment_btn.setIcon(qIconIncrement)
        self.ui.left_maxdur_decrement_btn.setIcon(qIconDecrement)

        self.ui.right_pressure_increment_btn.setIcon(qIconIncrement)
        self.ui.right_pressure_decrement_btn.setIcon(qIconDecrement)
        self.ui.right_activeph_increment_btn.setIcon(qIconIncrement)
        self.ui.right_activeph_decrement_btn.setIcon(qIconDecrement)
        self.ui.right_activedur_increment_btn.setIcon(qIconIncrement)
        self.ui.right_activedur_decrement_btn.setIcon(qIconDecrement)
        self.ui.right_maxdur_increment_btn.setIcon(qIconIncrement)
        self.ui.right_maxdur_decrement_btn.setIcon(qIconDecrement)


    def set_exo_controls_enabled(self, state):

        self.ui.play_widget.setEnabled(state)

    def init_settings(self):

        styleFile = os.path.join(os.path.split(__file__)[0], resource_path("lib/assets/styles/exo_styles.qss"))

        with open(styleFile, 'r') as f:
            style = f.read()

        self.setStyleSheet(style)

