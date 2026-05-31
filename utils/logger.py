"""Simple logging utility for the application."""
import logging
from datetime import datetime
from pathlib import Path


# Create logs directory if it doesn't exist
LOGS_DIR = Path(__file__).resolve().parent.parent / "logs"
LOGS_DIR.mkdir(exist_ok=True)

# Configure logging
LOG_FILE = LOGS_DIR / f"skillsync_{datetime.now().strftime('%Y%m%d')}.log"

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)


def get_logger(name):
    """
    Get a logger instance for a module.
    
    Args:
        name (str): Module name (typically __name__)
        
    Returns:
        logging.Logger: Logger instance
    """
    return logging.getLogger(name)


def log_info(message, logger_name="skillsync"):
    """Log an info message."""
    get_logger(logger_name).info(message)


def log_error(message, logger_name="skillsync", exception=None):
    """Log an error message."""
    if exception:
        get_logger(logger_name).error(message, exc_info=exception)
    else:
        get_logger(logger_name).error(message)


def log_warning(message, logger_name="skillsync"):
    """Log a warning message."""
    get_logger(logger_name).warning(message)


def log_debug(message, logger_name="skillsync"):
    """Log a debug message."""
    get_logger(logger_name).debug(message)
