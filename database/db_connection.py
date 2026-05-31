import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR / "database" / "skillsync.db"


def get_connection():
    """
    Get a SQLite database connection.
    
    Supports context manager protocol for automatic cleanup:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(...)
    
    Returns:
        sqlite3.Connection: Database connection with proper configuration
    """
    conn = sqlite3.connect(str(DATABASE_PATH), check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn