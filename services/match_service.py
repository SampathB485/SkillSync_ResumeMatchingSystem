from nlp.skill_extractor import extract_skills


def compute_match_score(candidate_text, job_text):
    """Compute a simple match score between candidate resume text and job description text."""
    candidate_skills = set(extract_skills(candidate_text))
    job_skills = set(extract_skills(job_text))
    if not job_skills:
        return 0.0
    overlap = candidate_skills.intersection(job_skills)
    return len(overlap) / len(job_skills)
