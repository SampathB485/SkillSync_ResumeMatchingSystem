from database.db_connection import get_connection
from nlp.skill_extractor import extract_skills
from ml.tfidf_matcher import compute_tfidf_similarity


def compute_match_score(candidate_text, job_text):
    """
    Compute hybrid match score using both skill-based and TF-IDF similarity.
    
    Combines:
    - Skill overlap (70% weight): Exact skill matches
    - TF-IDF similarity (30% weight): Semantic content match
    
    Args:
        candidate_text (str): Resume text
        job_text (str): Job description text
        
    Returns:
        float: Match score between 0 and 1
    """
    # Skill-based matching (70% weight)
    candidate_skills = set(extract_skills(candidate_text))
    job_skills = set(extract_skills(job_text))
    
    if not job_skills:
        skill_score = 0.0
    else:
        overlap = candidate_skills.intersection(job_skills)
        skill_score = len(overlap) / len(job_skills)
    
    # TF-IDF semantic matching (30% weight)
    tfidf_score = compute_tfidf_similarity(candidate_text, job_text)
    
    # Combine scores
    hybrid_score = (skill_score * 0.7) + (tfidf_score * 0.3)
    
    return hybrid_score


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
