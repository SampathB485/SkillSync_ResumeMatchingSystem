import hashlib
import sqlite3

from database.db_connection import get_connection


def _hash_password(password):
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def register_candidate(name, email, password, resume_path=None, resume_text=""):
    """Register a new candidate in the database."""
    password_hash = _hash_password(password)
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Candidate (name, email, password, resume_path, resume_text) VALUES (?, ?, ?, ?, ?)",
                (name, email, password_hash, resume_path, resume_text),
            )
            conn.commit()
            return True, "Candidate registered successfully."
    except sqlite3.IntegrityError as error:
        if "UNIQUE constraint failed: Candidate.email" in str(error):
            return False, "Email is already registered."
        return False, "Failed to register candidate."


def login_candidate(email, password):
    password_hash = _hash_password(password)
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT candidate_id, name, email, resume_path FROM Candidate WHERE email = ? AND password = ?",
            (email, password_hash),
        )
        return cursor.fetchone()


def save_candidate_resume(candidate_id, resume_path, resume_text):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE Candidate SET resume_path = ?, resume_text = ? WHERE candidate_id = ?",
            (resume_path, resume_text, candidate_id),
        )
        conn.commit()
        return cursor.rowcount == 1


def get_candidate_by_id(candidate_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT candidate_id, name, email, resume_path, resume_text FROM Candidate WHERE candidate_id = ?",
            (candidate_id,),
        )
        return cursor.fetchone()


def get_all_candidates_with_text():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT candidate_id, name, email, resume_path, resume_text FROM Candidate WHERE resume_text IS NOT NULL AND resume_text <> ''"
        )
        return cursor.fetchall()
