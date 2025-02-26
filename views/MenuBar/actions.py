from PySide6.QtGui import QIcon, QAction, QPixmap, QPainter
from PySide6.QtCore import Qt, Signal, QSize
import logging
from logging_config import setup_logging
from PySide6.QtGui import QIcon

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


class Open(QAction):
    def __init__(self, parent=None, text="&Open"):
        super().__init__(parent=parent, text=text)
        self.setIcon(action_icons[text])


class Save(QAction):
    def __init__(self, parent=None, text="&Save"):
        super().__init__(parent=parent, text=text)
        self.setIcon(action_icons[text])


class SaveAs(QAction):
    def __init__(self, parent=None, text="&Save as"):
        super().__init__(parent=parent, text=text)
        self.setIcon(action_icons[text])


class Copy(QAction):
    def __init__(self, parent=None, text="&Copy"):
        super().__init__(parent=parent, text=text)
        self.setIcon(action_icons[text])


class Cut(QAction):
    def __init__(self, parent=None, text="&Cut"):
        super().__init__(parent=parent, text=text)
        self.setIcon(action_icons[text])


class Paste(QAction):
    def __init__(self, parent=None, text="&Paste"):
        super().__init__(parent=parent, text=text)
        self.setIcon(action_icons[text])


class Delete(QAction):
    def __init__(self, parent=None, text="&Delete"):
        super().__init__(parent=parent, text=text)
        self.setIcon(action_icons[text])


class ToolWindows(QAction):
    def __init__(self, parent=None, text="&Tool Windows"):
        super().__init__(parent=parent, text=text)


class Appearance(QAction):
    def __init__(self, parent=None, text="&Appearance"):
        super().__init__(parent=parent, text=text)


class RecentFiles(QAction):
    def __init__(self, parent=None, text="&Recent Files"):
        super().__init__(parent=parent, text=text)


class Help(QAction):
    def __init__(self, parent=None, text="&Help"):
        super().__init__(parent=parent, text=text)
        self.setIcon(action_icons[text])


class About(QAction):

    def __init__(self, parent=None, text="&About"):
        super().__init__(parent=parent, text=text)
        self.setIcon(action_icons[text])

