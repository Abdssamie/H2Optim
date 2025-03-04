from PySide6.QtWidgets import (QMainWindow, QTabWidget, QLabel, QVBoxLayout,
                               QWidget)
from views.Pages.Dashboard.DataTab.excel_like_table import ExcelLikeTable
from views.Pages.Dashboard.DashboardTab.dashboard_tab import Dashboard


class TabbedWidget(QTabWidget):
    def __init__(self, parent: QMainWindow = None):
        super().__init__(parent=parent)
        self.main_window = parent

        self.dashboard_tab = None
        self.table_tab = None
        self.other_tab = None

        self.add_dashboard_tab()
        self.add_table_tab('Data', 1000, 20)

    def add_table_tab(self, title: str, rows: int, columns: int):
        self.table_tab = QWidget()
        layout = QVBoxLayout()

        # Add the Excel-like table widget
        table = ExcelLikeTable(rows, columns)  # Assuming ExcelLikeTable is defined elsewhere
        layout.addWidget(table)

        self.table_tab.setLayout(layout)
        self.addTab(self.table_tab, title)

    def add_dashboard_tab(self):
        self.dashboard_tab = Dashboard(self)
        self.addTab(self.dashboard_tab, "Dashboard")
