from PySide6.QtGui import QPalette, QColor

# Define the cold color scheme with only three main colors
BACKGROUND_COLOR = QColor("#2D3A45")  # A cool dark gray-blue for background
TEXT_COLOR = QColor("#FFFFFF")  # White for high contrast text
HIGHLIGHT_COLOR = QColor("#3A8FB7")  # Soft blue for highlighting
PLACEHOLDER_COLOR = QColor("#7D8A97")  # Soft light blue-gray for placeholders
TOOLTIP_BG_COLOR = QColor("#2A3742")  # Darker background for tooltips
TOOLTIP_TEXT_COLOR = QColor("#B0C6D6")  # Light grayish-blue for tooltip text
SHADOW_COLOR = QColor("#1C242C")  # Dark shadow color
MID_COLOR = QColor("#4F5A65")  # Mid-tone for elements like borders and separators
LINK_COLOR = QColor("#4C7B94")  # Soft blue for links
LINK_VISITED_COLOR = QColor("#3B5A6C")  # Slightly darker blue for visited links


def create_cold_palette():
    """Creates a QPalette with a cool blue color scheme for a balanced engineering application UI."""
    palette = QPalette()

    # Set the main color roles
    palette.setColor(QPalette.ColorRole.Window, BACKGROUND_COLOR)
    palette.setColor(QPalette.ColorRole.WindowText, TEXT_COLOR)
    palette.setColor(QPalette.ColorRole.Base, BACKGROUND_COLOR)
    palette.setColor(QPalette.ColorRole.AlternateBase, BACKGROUND_COLOR)  # Use the same as background
    palette.setColor(QPalette.ColorRole.Text, TEXT_COLOR)
    palette.setColor(QPalette.ColorRole.Button, BACKGROUND_COLOR)  # Matching button color with the background
    palette.setColor(QPalette.ColorRole.ButtonText, TEXT_COLOR)

    # Highlight and accent colors for selection
    palette.setColor(QPalette.ColorRole.Highlight, HIGHLIGHT_COLOR)
    palette.setColor(QPalette.ColorRole.HighlightedText, TEXT_COLOR)

    # Optional: defining darker and lighter shades
    palette.setColor(QPalette.ColorRole.Light, QColor("#4F5A65"))  # Lighter shade of background
    palette.setColor(QPalette.ColorRole.Dark, QColor("#1C242C"))  # Darker shade for contrast

    # Additional roles
    palette.setColor(QPalette.ColorRole.PlaceholderText, PLACEHOLDER_COLOR)
    palette.setColor(QPalette.ColorRole.ToolTipBase, TOOLTIP_BG_COLOR)
    palette.setColor(QPalette.ColorRole.ToolTipText, TOOLTIP_TEXT_COLOR)
    palette.setColor(QPalette.ColorRole.Shadow, SHADOW_COLOR)
    palette.setColor(QPalette.ColorRole.Mid, MID_COLOR)
    # palette.setColor(QPalette.ColorRole.Link, LINK_COLOR)
    # palette.setColor(QPalette.ColorRole.LinkVisited, LINK_VISITED_COLOR)

    return palette
