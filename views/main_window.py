from PySide6.QtWidgets import (QMainWindow, QApplication, QPushButton, QVBoxLayout, QLabel,
                               QWidget, QStackedWidget, QButtonGroup, QToolBar, QStatusBar)
from views.dock_widget import Sidebar
from views.Pages.Dashboard.dashboard import TabbedWidget
from views.Menubar.menu_bar import MenuBar

from utils.colors import JORDY_BLUE
from utils.actions import Open

from PySide6.QtCore import Qt, QTimer, QTime
from PySide6.QtCore import Slot


from logging_config import setup_logging
import logging

setup_logging()
logger = logging.getLogger(__name__)


class MainWindow(QMainWindow):
    def __init__(self, parent: QApplication = None):
        super().__init__(parent=parent)

        self.main_widget = MainWidget(self)

        self.menu_bar = MenuBar(self)

        self.setMenuBar(self.menu_bar)
        self.setCentralWidget(self.main_widget)

        self.setMinimumSize(800, 450)

        toolbar = QToolBar("Main Toolbar", self)
        toolbar.addAction(Open(self))
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, toolbar)  # Specify the area

        status_bar = QStatusBar(self)
        status_label = QLabel("Ready", self)
        self.time_label = QLabel(parent=self)
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        status_bar.addWidget(status_label)
        status_bar.addWidget(self.time_label, stretch=True)
        self.setStatusBar(status_bar)

        # Create a QTimer to update the time every second
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Update every 1000 milliseconds (1 second)

        # Initial time update
        self.update_time()

    def update_time(self):
        # Get the current time
        current_time = QTime.currentTime()

        # Format the time as h:mm (no leading zero for hour, leading zero for minutes)
        time_string = current_time.toString("h:mm")

        # Update the label's text
        self.time_label.setText(time_string)


class MainWidget(QWidget):
    def __init__(self, parent: QMainWindow = None):
        super().__init__(parent=parent)

        self.main_window = parent

        self.stacked_widget = None
        self.sidebar = None
        self.button_group = None

        self.dashboard_widget = None
        self.ai_assistant_widget = None
        self.tools_widget = None
        self.settings_widget = None
        self.resources_widget = None

        # This will alter this class widgets from None and create them
        self.create_widgets()

        # Once widgets are created we can then add them to the main tab and the dock widget that acts as navigation
        self.add_main_widget()
        self.add_dock_widget()

    def add_main_widget(self):
        # Stacked Widget to display different content
        self.stacked_widget = QStackedWidget(self)
        central_layout = QVBoxLayout(self)
        central_layout.addWidget(self.stacked_widget)

        self.stacked_widget.addWidget(self.dashboard_widget)
        self.stacked_widget.addWidget(self.ai_assistant_widget)
        self.stacked_widget.addWidget(self.tools_widget)
        self.stacked_widget.addWidget(self.resources_widget)
        self.stacked_widget.addWidget(self.settings_widget)

        self.stacked_widget.setCurrentWidget(self.dashboard_widget)
        self.stacked_widget.currentChanged.connect(self.change_active_button)

    def create_widgets(self):
        """Create all the widgets once."""
        self.dashboard_widget = TabbedWidget()

        self.tools_widget = QWidget()
        self.tools_widget.setStyleSheet("background-color: lightgreen;")

        self.ai_assistant_widget = QWidget()
        self.ai_assistant_widget.setStyleSheet("background-color: lightcoral;")

        self.settings_widget = QWidget()
        self.settings_widget.setStyleSheet("background-color: lightgray;")

        self.resources_widget = QWidget()
        self.resources_widget.setStyleSheet("background-color: lightyellow;")

    def add_dock_widget(self):
        # Sidebar navigation
        self.sidebar = Sidebar(parent=self)
        self.main_window.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.sidebar)

        self.button_group = QButtonGroup(self)

        dashboard_btn = self.sidebar.widget().findChild(QPushButton, "Dashboard")
        ai_assistant_btn = self.sidebar.widget().findChild(QPushButton, "Hydra AI")
        tools_btn = self.sidebar.widget().findChild(QPushButton, "Tools")
        resources_btn = self.sidebar.widget().findChild(QPushButton, "Resources")
        settings_btn = self.sidebar.widget().findChild(QPushButton, "Settings")

        for btn in [dashboard_btn, ai_assistant_btn, tools_btn, resources_btn, settings_btn]:
            self.button_group.addButton(btn)

        # Set unique ids for each button
        self.button_group.setId(dashboard_btn, 0)
        self.button_group.setId(ai_assistant_btn, 1)
        self.button_group.setId(tools_btn, 2)
        self.button_group.setId(resources_btn, 3)
        self.button_group.setId(settings_btn, 4)

        dashboard_btn.clicked.connect(self.show_dashboard)
        ai_assistant_btn.clicked.connect(self.show_ai_assistant)
        tools_btn.clicked.connect(self.show_tools)
        resources_btn.clicked.connect(self.show_resources)
        settings_btn.clicked.connect(self.show_settings)

    def show_dashboard(self):
        self.stacked_widget.setCurrentWidget(self.dashboard_widget)
        # self.change_active_button(self.button_group.buttons()[0])

    def show_ai_assistant(self):
        self.stacked_widget.setCurrentWidget(self.ai_assistant_widget)
        # self.change_active_button(self.button_group.buttons()[1])

    def show_tools(self):
        self.stacked_widget.setCurrentWidget(self.tools_widget)
        # self.change_active_button(self.button_group.buttons()[2])

    def show_resources(self):
        self.stacked_widget.setCurrentWidget(self.resources_widget)
        # self.change_active_button(self.button_group.buttons()[3])

    def show_settings(self):
        self.stacked_widget.setCurrentWidget(self.settings_widget)
        # self.change_active_button(self.button_group.buttons()[4])

    @Slot()
    def change_active_button(self, button_idx: int):
        logger.debug("Signal emitted successfully Change active button Function worked")
        button = self.button_group.buttons()[button_idx]

        for btn in self.button_group.buttons():
            if btn == button:
                btn.setStyleSheet(f"""
                        background-color: white;
                        color: black;
                        font-size: 14px;
                        padding: 20px 10px;
                        """)
            else:
                btn.setStyleSheet(f"""
                        background-color: {JORDY_BLUE};
                        color: black;
                        padding: 20px 10px;
                        font-size: 12px;
                        """)
