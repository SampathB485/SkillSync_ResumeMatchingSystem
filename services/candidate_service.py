from database.db_connection import get_connection


def register_candidate(name, email, password, resume_path=None):
    """Register a new candidate in the database."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO candidates (name, email, password, resume_path) VALUES (?, ?, ?, ?)",
            (name, email, password, resume_path),
        )
        conn.commit()
        return cursor.lastrowid
