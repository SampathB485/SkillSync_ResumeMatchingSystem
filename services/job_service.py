from database.db_connection import get_connection
from datetime import datetime


def create_job(
    recruiter_id,
    job_title,
    job_description,
    required_skills,
    experience_required
):

    conn = get_connection()
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
    conn.close()


def get_jobs_by_recruiter(recruiter_id):

    conn = get_connection()
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

    conn.close()

    return jobs