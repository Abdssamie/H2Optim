import logging
import logging.config
import os
import colorlog


# Custom formatter that assigns unique colors to level names, messages, and data.
class LevelBasedColoredFormatter(colorlog.ColoredFormatter):
    level_colors = {
        "DEBUG": "\033[36m",     # Cyan
        "INFO": "\033[32m",      # Green
        "WARNING": "\033[33m",   # Yellow
        "ERROR": "\033[31m",     # Red
        "CRITICAL": "\033[91m",  # Bright Red
    }

    # Removed data_color

    def format(self, record):
        level_color = self.level_colors.get(record.levelname, "\033[0m")
        message_color = "\033[0m"  # Default to white for messages
        if record.levelname in ["ERROR", "CRITICAL", "WARNING"]:
            message_color = level_color  # Match level color for error/critical/notice

        record.level_color = level_color
        record.message_color = message_color
        # Removed data_color from record
        record.reset = "\033[0m"  # Reset code

        return super().format(record)


# Create logs directory if it doesn't exist
LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Logging configuration dictionary
LOG_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "custom_colored": {
            "()": "logging_config.LevelBasedColoredFormatter",  # Corrected path
            "format": (
                "%(asctime)s  %(level_color)s%(levelname)s%(reset)s  %(name)s :\t"
                "%(message_color)s%(message)s%(reset)s"  # Removed data_color from format
            ),
            "datefmt": "%Y-%m-%d %H:%M:%S"
        },
        "detailed": {
            "format": "[%(asctime)s] [%(levelname)s] [%(name)s]: %(message)s",  # Removed data_color from format
            "datefmt": "%Y-%m-%d %H:%M:%S"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "custom_colored",
            "level": "DEBUG",
        },
        "file": {
            "class": "logging.FileHandler",
            "formatter": "detailed",
            "level": "DEBUG",
            "filename": os.path.join(LOG_DIR, "app.log"),
            "mode": "a",
            "encoding": "utf-8"
        },
        "null": {
            "class": "logging.NullHandler",
        }
    },
    "root": {
        "handlers": ["console", "file"],
        "level": "DEBUG",
    },
    "loggers": {
        "pymongo": {
            "handlers": ["null"],
            "level": "WARNING",
            "propagate": False,
        }
    }
}


def setup_logging():
    logging.config.dictConfig(LOG_CONFIG)


setup_logging()

# Example logger usage
logger = logging.getLogger(__name__)
logger.debug("This is a debug message.")  # Removed extra data
logger.info("This is an info message.")  # Removed extra data
logger.warning("This is a warning message.")  # Removed extra data
logger.error("This is an error message.")  # Removed extra data
logger.critical("This is a critical message.")  # Removed extra data
