from PySide6 import QtWidgets, QtCore
from utils.actions import (
    Open,
    SaveAs,
    Save,
    Copy,
    Cut,
    Paste,
    Delete,
    Appearance,
    ToolWindows,
    About,
    Help,
    RecentFiles
)
from utils.helpers import SANS_SERIF
from PySide6.QtWidgets import QMainWindow, QMenuBar
from utils.palette import create_cold_palette
import logging
from logging_config import setup_logging

setup_logging()
logger = logging.getLogger(__name__)


class FileMenu(QtWidgets.QMenu):

    def __init__(self, main_window: QMainWindow, parent: QMenuBar = None):
        super().__init__("File", parent=parent)
        self.main_window = main_window

        self.addAction(Open(parent, self))
        self.addAction(Save(main_window, self))
        self.addAction(SaveAs(main_window, self))


class EditMenu(QtWidgets.QMenu):
    def __init__(self, main_window: QMainWindow, parent: QMenuBar = None):
        super().__init__("Edit", parent)
        self.main_window = main_window
        self.addAction(Copy(main_window, parent=self))
        self.addAction(Cut(main_window, parent=self))
        self.addAction(Paste(main_window, parent=self))
        self.addAction(Delete(main_window, parent=self))


class ViewMenu(QtWidgets.QMenu):
    def __init__(self, main_window: QMainWindow, parent: QMenuBar = None):
        super().__init__("View", parent=parent)
        self.addAction(ToolWindows(main_window, parent=self))
        self.addAction(Appearance(main_window, parent=self))
        self.addAction(RecentFiles(main_window, parent=self))


class HelpMenu(QtWidgets.QMenu):
    def __init__(self, main_window: QMainWindow, parent: QMenuBar = None):
        super().__init__("Help", parent=parent)
        self.addAction(Help(main_window, parent=self))
        self.addAction(About(main_window, parent=self))


class MenuBar(QMenuBar):

    def __init__(self, parent: QMainWindow = None):
        super(MenuBar, self).__init__(parent=parent, nativeMenuBar=True)
        SANS_SERIF.setPixelSize(16)
        self.setFont(SANS_SERIF)

        self.addMenu(FileMenu(main_window=parent, parent=self))
        self.addMenu(EditMenu(main_window=parent, parent=self))
        self.addMenu(ViewMenu(main_window=parent, parent=self))
        self.addMenu(HelpMenu(main_window=parent, parent=self))

        self.setPalette(create_cold_palette())

        rect = QtCore.QRect(
            parent.geometry().topLeft().x(),
            parent.geometry().topLeft().y(),
            parent.geometry().width(),
            400)
