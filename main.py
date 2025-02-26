from PySide6 import QtCore, QtWidgets
from PySide6. QtCore import Slot
import sys
import random
from views.MenuBar.menu_bar import MenuBar
from logging_config import setup_logging
import logging

setup_logging()
logger = logging.getLogger(__name__)

logger.info("Started logging process Successfully")


class IoTApplication(QtWidgets.QApplication):
    def __init__(self):
        super().__init__()
        with open("styles/style.qss", "r") as f:
            _style = f.read()
            self.setStyleSheet(_style)

        self.main_window = QtWidgets.QMainWindow()

        self.widget = MyWidget()
        self.main_window.resize(1000, 700)

        self.menu_bar_widget = MenuBar(self.main_window)

        self.main_window.setMenuBar(self.menu_bar_widget)
        self.main_window.setCentralWidget(self.widget)

        self.main_window.show()


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Abdessamie", "Hei Abdessamie", "Hola Abdessamie", "Привет Абдессами"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello Abdessamie", alignment=QtCore.Qt.AlignmentFlag.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))
        logger.info("Hello Abdessamie")


if __name__ == "__main__":
    app = IoTApplication()
    sys.exit(app.exec())

