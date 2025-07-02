from PyQt6.QtWidgets import QWidget
from lib.controller.views.ui.logger_ui import Ui_logger_widget_form

class LoggerUI(QWidget):
    def __init__(self):

        super().__init__()
        self.ui = Ui_logger_widget_form()
        self.ui.setupUi(self)

        self.ui.send_btn.clicked.connect(self.send_message)
        self.ui.logger_msg_edit.returnPressed.connect(self.send_message)

    def send_message(self):
        self.ui.plainTextEdit.appendPlainText(self.ui.logger_msg_edit.text())
        self.ui.logger_msg_edit.clear()