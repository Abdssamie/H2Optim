from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,

)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np


# Chart Widget Classes
class LineChartWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        figure = Figure()
        canvas = FigureCanvas(figure)
        ax = figure.add_subplot()
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        ax.plot(x, y, label="Sine Wave")
        ax.set_title("Line Chart")
        ax.legend()
        layout.addWidget(canvas)


class BarChartWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        figure = Figure()
        canvas = FigureCanvas(figure)
        ax = figure.add_subplot()
        categories = ["A", "B", "C", "D"]
        values = [4, 7, 1, 8]
        ax.bar(categories, values, color="skyblue")
        ax.set_title("Bar Chart")
        layout.addWidget(canvas)


class ScatterChartWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        figure = Figure()
        canvas = FigureCanvas(figure)
        ax = figure.add_subplot()
        x = np.random.rand(50)
        y = np.random.rand(50)
        ax.scatter(x, y, color="green")
        ax.set_title("Scatter Chart")
        layout.addWidget(canvas)


class PieChartWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        figure = Figure()
        canvas = FigureCanvas(figure)
        ax = figure.add_subplot()
        sizes = [30, 20, 25, 25]
        labels = ["Group A", "Group B", "Group C", "Group D"]
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.set_title("Pie Chart")
        layout.addWidget(canvas)


class HistogramWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        figure = Figure()
        canvas = FigureCanvas(figure)
        ax = figure.add_subplot()
        data = np.random.randn(1000)
        ax.hist(data, bins=30, color="purple")
        ax.set_title("Histogram")
        layout.addWidget(canvas)


class AreaChartWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        figure = Figure()
        canvas = FigureCanvas(figure)
        ax = figure.add_subplot()
        x = np.linspace(0, 10, 100)
        y = np.sin(x) + 0.5
        ax.fill_between(x, y, color="lightblue", alpha=0.6)
        ax.set_title("Area Chart")
        layout.addWidget(canvas)
