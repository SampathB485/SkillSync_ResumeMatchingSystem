from database.db_connection import get_connection


def create_job(title, description, skills, location):
    """Create a new job posting in the database."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO jobs (title, description, skills, location) VALUES (?, ?, ?, ?)",
            (title, description, skills, location),
        )
        conn.commit()
        return cursor.lastrowid
