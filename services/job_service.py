from database.db_connection import get_connection
from datetime import datetime
import sqlite3


def create_job(
    recruiter_id,
    job_title,
    job_description,
    required_skills,
    experience_required
):
    """Create a new job posting."""
    try:
        with get_connection() as conn:
            cursor = conn.cursor()

            posted_date = datetime.now().strftime("%Y-%m-%d")

            cursor.execute("""
                INSERT INTO Job (
                    recruiter_id,
                    job_title,
                    job_description,
                    required_skills,
                    experience_required,
                    posted_date
                )
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                recruiter_id,
                job_title,
                job_description,
                required_skills,
                experience_required,
                posted_date
            ))

            conn.commit()
            return True, "Job posted successfully."
    except sqlite3.Error as error:
        return False, f"Failed to create job: {str(error)}"


def get_jobs_by_recruiter(recruiter_id):
    """Get all jobs posted by a recruiter."""
    try:
        with get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute("""
                SELECT
                    job_id,
                    job_title,
                    required_skills,
                    experience_required,
                    posted_date
                FROM Job
                WHERE recruiter_id = ?
                ORDER BY job_id DESC
            """, (recruiter_id,))

            jobs = cursor.fetchall()
            return jobs
    except sqlite3.Error as error:
        print(f"Database error: {error}")
        return []


def get_job_by_id(job_id):
    """Get a specific job by ID."""
    try:
        with get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute("""
                SELECT
                    job_id,
                    job_title,
                    job_description,
                    required_skills,
                    experience_required,
                    posted_date
                FROM Job
                WHERE job_id = ?
            """, (job_id,))

            job = cursor.fetchone()
            return job
    except sqlite3.Error as error:
        print(f"Database error: {error}")
        return None


def get_all_jobs():
    """Get all jobs in the system."""
    try:
        with get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute("""
                SELECT
                    job_id,
                    job_title,
                    job_description,
                    required_skills,
                    experience_required,
                    posted_date
                FROM Job
                ORDER BY job_id DESC
            """)

            jobs = cursor.fetchall()
            return jobs
    except sqlite3.Error as error:
        print(f"Database error: {error}")
        return []