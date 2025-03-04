from PySide6.QtWidgets import QDockWidget, QVBoxLayout, QWidget, QPushButton, QStyleOptionButton
from PySide6.QtCore import Qt
from utils.helpers import CONSOLAS, CONSOLAS_BOLD, SANS_SERIF, SANS_SERIF_BOLD
from utils.colors import JORDY_BLUE


class Sidebar(QDockWidget):
    def __init__(self, parent=None):
        super(Sidebar, self).__init__(parent)
        self.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)
        self.setFloating(True)

        sidebar_widget = QWidget(self)
        layout = QVBoxLayout(sidebar_widget)

        self.setStyleSheet("""
                        width: 80px;
        """)

        self.dashboard_button = QPushButton("Dashboard", self)
        self.dashboard_button.setObjectName("Dashboard")
        self.dashboard_button.setFont(SANS_SERIF_BOLD)
        self.dashboard_button.setStyleSheet(f"""
                        background-color: white;
                        color: black;
                        font-size: 14px;
                        padding: 20px 10px;
                        """)
        layout.addWidget(self.dashboard_button)

        self.ai_assistant_button = QPushButton("Hydra AI")
        self.ai_assistant_button.setObjectName("Hydra AI")
        self.ai_assistant_button.setFont(SANS_SERIF_BOLD)
        self.ai_assistant_button.setStyleSheet(f"""
                        background-color: {JORDY_BLUE};
                        color: black;
                        padding: 20px 10px;
                        font-size: 12px;
                        """)
        layout.addWidget(self.ai_assistant_button)

        self.tools_button = QPushButton("Tools")
        self.tools_button.setObjectName("Tools")
        self.tools_button.setFont(SANS_SERIF_BOLD)
        self.tools_button.setStyleSheet(f"""
                        background-color: {JORDY_BLUE};
                        color: black;
                        padding: 20px 10px;
                        font-size: 12px;
                        """)
        layout.addWidget(self.tools_button)

        self.resources_button = QPushButton("Resources")
        self.resources_button.setObjectName("Resources")
        self.resources_button.setFont(SANS_SERIF_BOLD)
        self.resources_button.setStyleSheet(f"""
                        background-color: {JORDY_BLUE};
                        color: black;
                        padding: 20px 10px;
                        font-size: 12px;
                        """)
        layout.addWidget(self.resources_button)

        self.settings_button = QPushButton("Settings")
        self.settings_button.setObjectName("Settings")
        self.settings_button.setFont(SANS_SERIF_BOLD)
        self.settings_button.setStyleSheet(f"""
                        background-color: {JORDY_BLUE};
                        color: black;
                        padding: 20px 10px;
                        font-size: 12px;
                        """)
        layout.addWidget(self.settings_button)

        sidebar_widget.setLayout(layout)
        self.setWidget(sidebar_widget)
