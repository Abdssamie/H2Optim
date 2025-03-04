from PySide6.QtWidgets import (
    QGridLayout,
    QTableWidget,
    QWidget,
    QLayoutItem,
    QVBoxLayout,
    QHBoxLayout,
    QLayout,
    QTableWidgetItem,
    QHeaderView,
    QAbstractItemView,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QMouseEvent
# from PySide6.QtCharts import QChart, QChartView
from views.Pages.Dashboard.SampleCharts.chart import (ScatterChartWidget,
                                                      HistogramWidget,
                                                      AreaChartWidget,
                                                      PieChartWidget,
                                                      BarChartWidget,
                                                      LineChartWidget)


class Dashboard(QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setRowCount(4)
        self.setColumnCount(4)

        self.setRowHeight(0, 200)
        self.setRowHeight(1, 300)
        self.setRowHeight(2, 250)
        self.setRowHeight(3, 250)

        self.horizontalHeader().setVisible(False)
        self.verticalHeader().setVisible(False)

        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Interactive)

        self.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

        self.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.setDragDropMode(QAbstractItemView.DragDropMode.NoDragDrop)
        self.create_dashboard_widgets()

    def create_dashboard_widgets(self):
        # Create individual widgets for each cell
        self.create_widget_for_cell(0, 0, ScatterChartWidget)
        self.create_widget_for_cell(0, 1, HistogramWidget)
        self.create_widget_for_cell(0, 2, AreaChartWidget)
        self.create_widget_for_cell(0, 3, PieChartWidget)
        self.create_widget_for_cell(1, 0, BarChartWidget, col_span=2)
        self.create_widget_for_cell(2, 2, LineChartWidget, col_span=2)

    def create_widget_for_cell(self, row, col, chart_widget_class, row_span=1, col_span=1):
        chart_widget = chart_widget_class()  # Create the chart widget
        layout = QVBoxLayout()  # Create a layout for this widget
        layout.addWidget(chart_widget)  # Add the chart widget to the layout

        # Create a container widget, set the layout, and place it in the table cell
        container_widget = QWidget()
        container_widget.setLayout(layout)
        self.setCellWidget(row, col, container_widget)

        # --- Set the span ---
        self.setSpan(row, col, row_span, col_span)
        # ---------------------
