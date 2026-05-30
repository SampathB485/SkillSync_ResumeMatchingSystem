import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR / "database" / "skillsync.db"

def get_connection():
    return sqlite3.connect(DATABASE_PATH)