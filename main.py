from PySide6.QtWidgets import (
    QLabel, QTabWidget, QStackedWidget, QVBoxLayout, QMainWindow, QPushButton, QWidget, QApplication
)
from PySide6.QtCore import Qt
import sys
from views.main_window import MainWindow

from utils.palette import create_cold_palette
from utils.helpers import CONSOLAS, CONSOLAS_BOLD, SANS_SERIF, SANS_SERIF_BOLD

import logging
from logging_config import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

logger.info("Started logging process Successfully")


class IoTApplication(QApplication):
    def __init__(self):
        super().__init__()

        with open("styles/menu.qss", "r") as f:
            _style = f.read()
            self.setStyleSheet(_style)

        self.setApplicationName("HYDRA App")

        cold_scheme_palette = create_cold_palette()
        self.setPalette(cold_scheme_palette)
        self.setFont(SANS_SERIF)

        self.main_window = MainWindow()

        self.main_window.showMaximized()


if __name__ == "__main__":
    app = IoTApplication()
    sys.exit(app.exec())
