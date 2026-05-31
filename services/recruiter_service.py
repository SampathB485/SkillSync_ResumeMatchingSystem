import hashlib
import sqlite3

from database.db_connection import get_connection


def _hash_password(password):
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def register_recruiter(name, company_name, email, password):
    password_hash = _hash_password(password)
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Recruiter (name, company_name, email, password) VALUES (?, ?, ?, ?)",
                (name, company_name, email, password_hash),
            )
            conn.commit()
            return True, "Recruiter registered successfully."
    except sqlite3.IntegrityError as error:
        if "UNIQUE constraint failed: Recruiter.email" in str(error):
            return False, "Email is already registered."
        return False, "Failed to register recruiter."


def login_recruiter(email, password):
    password_hash = _hash_password(password)
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT recruiter_id, name, company_name FROM Recruiter WHERE email = ? AND password = ?",
            (email, password_hash),
        )
        return cursor.fetchone()