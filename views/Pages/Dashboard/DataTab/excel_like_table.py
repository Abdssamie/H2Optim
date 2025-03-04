from PySide6.QtWidgets import QTableWidget, QTableWidgetItem


class ExcelLikeTable(QTableWidget):
    def __init__(self, num_rows: int = 1000000, num_columns: int = 26*26):
        super().__init__()

        # Set row and column counts
        self.setRowCount(num_rows)
        self.setColumnCount(num_columns)

        # Generate column headers
        self.setHorizontalHeaderLabels(self.generate_column_headers(num_columns))

    def generate_column_headers(self, num_columns: int):
        """Generate column headers like A, B, ..., Z, AA, AB, etc."""
        headers = []
        for i in range(num_columns):
            headers.append(self.column_name(i))
        return headers

    @staticmethod
    def column_name(index: int) -> str:
        """Convert a zero-based index to Excel-like column name."""
        name = ""
        while index >= 0:
            name = chr(index % 26 + ord("A")) + name
            index = index // 26 - 1
        return name
