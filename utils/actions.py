from PySide6.QtGui import QIcon, QAction, QKeySequence, QFont
from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtCore import Slot
import logging
from logging_config import setup_logging
from utils.helpers import get_data_file, validate_file, SANS_SERIF


setup_logging()
logger = logging.getLogger(__name__)

action_icons = {
    "&Open": QIcon.fromTheme(QIcon.ThemeIcon.DocumentOpen),
    "&Save": QIcon.fromTheme(QIcon.ThemeIcon.DocumentSave),
    "&Save as": QIcon.fromTheme(QIcon.ThemeIcon.DocumentSaveAs),
    "&Copy": QIcon.fromTheme(QIcon.ThemeIcon.EditCopy),
    "&Cut": QIcon.fromTheme(QIcon.ThemeIcon.EditCut),
    "&Paste": QIcon.fromTheme(QIcon.ThemeIcon.EditPaste),
    "&Delete": QIcon.fromTheme(QIcon.ThemeIcon.EditDelete),
    "&Tool Windows": None,  # No icon for this action
    "&Appearance": None,  # No icon for this action
    "&Recent Files": None,  # No icon for this action
    "&Help": QIcon("Icons/help_center.svg"),  # Custom icon
    "&About": QIcon.fromTheme(QIcon.ThemeIcon.HelpAbout),
}


class BaseAction(QAction):
    def __init__(self, main_window: QMainWindow, parent=None, text="", shortcut=None):
        super().__init__(parent=parent, text=text)
        self.main_window = main_window

        action_icon = action_icons.get(text)
        if action_icon:
            self.setIcon(action_icon)

        SANS_SERIF.setPixelSize(13)
        self.setFont(SANS_SERIF)

        if shortcut:
            self.setShortcut(QKeySequence(shortcut))

    @Slot()
    def action_triggered(self):
        pass


class Open(BaseAction):
    def __init__(self, main_window: QMainWindow = None, parent=None, text="&Open"):
        super().__init__(main_window=main_window, parent=parent, text=text, shortcut="Ctrl+O")

    @Slot()
    def open_file(self):
        file_path = get_data_file()
        file_is_valid = False

        if file_path:
            logger.debug(f"file_path is {file_path}")
            file_is_valid = validate_file(file_path)

        if file_is_valid:
            with open(file_path, "r") as file:
                content = file.read()
                logging.info(f"The content of the file is: {content}")
        else:
            self.show_error_message("Invalid file type", "Please select a valid table-like data file")

    def show_error_message(self, title, message):
        msg_box = QMessageBox(self.main_window)
        msg_box.setIcon(QMessageBox.Icon.Warning)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec()


class Save(BaseAction):
    def __init__(self, main_window: QMainWindow = None, parent=None, text="&Save"):
        super().__init__(main_window=main_window, parent=parent, text=text, shortcut="Ctrl+S")


class SaveAs(BaseAction):
    def __init__(self, main_window: QMainWindow = None, parent=None, text="&Save as"):
        super().__init__(main_window=main_window, parent=parent, text=text, shortcut="Ctrl+Shift+S")


class Copy(BaseAction):
    def __init__(self, main_window: QMainWindow = None, parent=None, text="&Copy"):
        super().__init__(main_window=main_window, parent=parent, text=text, shortcut="Ctrl+C")


class Cut(BaseAction):
    def __init__(self, main_window: QMainWindow = None, parent=None, text="&Cut"):
        super().__init__(main_window=main_window, parent=parent, text=text, shortcut="Ctrl+X")


class Paste(BaseAction):
    def __init__(self, main_window: QMainWindow = None, parent=None, text="&Paste"):
        super().__init__(main_window=main_window, parent=parent, text=text, shortcut="Ctrl+V")


class Delete(BaseAction):
    def __init__(self, main_window: QMainWindow = None, parent=None, text="&Delete"):
        super().__init__(main_window=main_window, parent=parent, text=text)


class ToolWindows(BaseAction):
    def __init__(self, main_window: QMainWindow = None, parent=None, text="&Tool Windows"):
        super().__init__(main_window=main_window, parent=parent, text=text)


class Appearance(BaseAction):
    def __init__(self, main_window: QMainWindow = None, parent=None, text="&Appearance"):
        super().__init__(main_window=main_window, parent=parent, text=text)


class RecentFiles(BaseAction):
    def __init__(self, main_window: QMainWindow = None, parent=None, text="&Recent Files"):
        super().__init__(main_window=main_window, parent=parent, text=text)


class Help(BaseAction):
    def __init__(self, main_window: QMainWindow = None, parent=None, text="&Help"):
        super().__init__(main_window=main_window, parent=parent, text=text)


class About(BaseAction):
    def __init__(self, main_window: QMainWindow = None, parent=None, text="&About"):
        super().__init__(main_window=main_window, parent=parent, text=text)
