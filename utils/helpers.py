from PySide6.QtWidgets import QFileDialog
from PySide6.QtGui import QFont
from pathlib import Path
import os

SANS_SERIF = QFont("Sans-Serif", 10)
CONSOLAS = QFont("Monospace", 10)
SANS_SERIF_BOLD = QFont("Sans-Serif", 10, QFont.Weight.Bold)
CONSOLAS_BOLD = QFont("Monospace", 10, QFont.Weight.Bold)

SUPPORTED_FORMATS = {".json", ".csv", ".xlsx", ".xls", ".xml", ".tsv", ".ods"}
MAX_FILE_SIZE_MB = 50  # Maximum file size in megabytes


def get_data_file(parent=None, caption="Open Data File", start_dir=None):
    """
    Opens a file dialog to select a data file.

    :param parent: The parent widget (optional).
    :param caption: Title of the file dialog.
    :param start_dir: Starting directory for the file dialog.
    :return: Selected file path or None if no file is selected.
    """
    if start_dir is None:
        start_dir = str(Path.home() / "Documents")

    file_types = "Data Files (*.json *.csv *.xlsx *.xls *.xml *.tsv *.ods);;All Files (*)"
    file_path, _ = QFileDialog.getOpenFileName(parent, caption, start_dir, file_types)
    return file_path


def validate_file(file_path):
    """
    Validates the selected file for supported format and size.

    :param file_path: Path to the file.
    :return: True if the file is valid, False otherwise.
    """
    file_extension = Path(file_path).suffix.lower()
    file_size_mb = os.path.getsize(file_path) / (1024 * 1024)  # Convert to MB

    # Check file format
    if file_extension not in SUPPORTED_FORMATS:
        print(f"Unsupported file format: {file_extension}")
        return False

    # Check file size
    if file_size_mb > MAX_FILE_SIZE_MB:
        print(f"File size is too large: {file_size_mb:.2f} MB (max: {MAX_FILE_SIZE_MB} MB)")
        return False

    return True
