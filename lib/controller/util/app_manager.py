

import qdarktheme
from PyQt6.QtWidgets import QApplication


# Singleton App Manager
class AppManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.theme = 'dark'
        return cls._instance

    def apply_theme(self):
        if self.theme == 'dark':
            qdarktheme.setup_theme("dark")
        else:
            qdarktheme.setup_theme("light")

    def toggle_theme(self):
        self.theme = 'light' if self.theme == 'dark' else 'dark'
        self.apply_theme()
