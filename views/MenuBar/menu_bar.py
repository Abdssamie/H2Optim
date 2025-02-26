from PySide6 import QtWidgets, QtCore
from views.MenuBar.actions import (
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
import logging
from logging_config import setup_logging

setup_logging()
logger = logging.getLogger(__name__)


class FileMenu(QtWidgets.QMenu):

    def __init__(self):
        super().__init__("File",)
        self.addAction(Open(self))
        self.addAction(Save(self))
        self.addAction(SaveAs(self))

    def mouseMoveEvent(self, event):
        action = self.actionAt(event.pos())
        if action:
            if action.menu():
                pass

            action_text = action.text()
            logger.info(f'Action name: {action_text}')

            action.setIcon(hover_action_icons[action_text])
            logger.info("Changed Icon = Success")


class EditMenu(QtWidgets.QMenu):
    def __init__(self):
        super().__init__("Edit")
        self.addAction(Copy(self))
        self.addAction(Cut(self))
        self.addAction(Paste(self))
        self.addAction(Delete(self))


class ViewMenu(QtWidgets.QMenu):
    def __init__(self):
        super().__init__("View")
        self.addAction(ToolWindows(self))
        self.addAction(Appearance(self))
        self.addAction(RecentFiles(self))


class HelpMenu(QtWidgets.QMenu):
    def __init__(self):
        super().__init__("View")
        self.addAction(Help(self))
        self.addAction(About(self))


class MenuBar(QtWidgets.QMenuBar):

    def __init__(self, parent: QtWidgets.QMainWindow):
        super(MenuBar, self).__init__(parent=parent, nativeMenuBar=True)
        self.addMenu(FileMenu())
        self.addMenu(EditMenu())
        self.addMenu(ViewMenu())
        self.addMenu(HelpMenu())

        rect = QtCore.QRect(
                        parent.geometry().topLeft().x(),
                        parent.geometry().topLeft().y(),
                        parent.geometry().width(),
                        400)
