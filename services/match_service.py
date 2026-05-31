from database.db_connection import get_connection
from nlp.skill_extractor import extract_skills


def compute_match_score(candidate_text, job_text):
    """Compute a simple match score between candidate resume text and job description text."""
    candidate_skills = set(extract_skills(candidate_text))
    job_skills = set(extract_skills(job_text))
    if not job_skills:
        return 0.0
    overlap = candidate_skills.intersection(job_skills)
    return len(overlap) / len(job_skills)


def evaluate_candidate_for_job(candidate, job):
    _, _, _, _, resume_text = candidate
    _, _, description, required_skills, _, _ = job
    job_text = f"{description}\n{required_skills}"
    score = compute_match_score(resume_text or "", job_text)
    candidate_skills = set(extract_skills(resume_text or ""))
    job_skills = set(extract_skills(job_text))
    missing_skills = sorted(job_skills - candidate_skills)
    matched_skills = sorted(candidate_skills.intersection(job_skills))
    return {
        "score": round(score, 3),
        "missing_skills": missing_skills,
        "matched_skills": matched_skills,
        "candidate_skills": sorted(candidate_skills),
        "job_skills": sorted(job_skills),
    }


def save_match_result(candidate_id, job_id, match_score, missing_skills, ranking):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM MatchResult WHERE candidate_id = ? AND job_id = ?",
            (candidate_id, job_id),
        )
        cursor.execute(
            "INSERT INTO MatchResult (candidate_id, job_id, match_score, missing_skills, ranking) VALUES (?, ?, ?, ?, ?)",
            (candidate_id, job_id, match_score, ", ".join(missing_skills), ranking),
        )
        conn.commit()


def get_all_match_results():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT
                mr.result_id,
                c.name,
                j.job_title,
                mr.match_score,
                mr.missing_skills,
                mr.ranking,
                j.posted_date
            FROM MatchResult mr
            JOIN Candidate c ON mr.candidate_id = c.candidate_id
            JOIN Job j ON mr.job_id = j.job_id
            ORDER BY mr.job_id, mr.ranking
        """)
        return cursor.fetchall()


def get_match_results_for_recruiter(recruiter_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT
                mr.result_id,
                c.name,
                j.job_title,
                mr.match_score,
                mr.missing_skills,
                mr.ranking,
                j.posted_date
            FROM MatchResult mr
            JOIN Candidate c ON mr.candidate_id = c.candidate_id
            JOIN Job j ON mr.job_id = j.job_id
            WHERE j.recruiter_id = ?
            ORDER BY mr.job_id, mr.ranking
        """, (recruiter_id,))
        return cursor.fetchall()
