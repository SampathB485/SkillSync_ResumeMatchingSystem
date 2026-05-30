from nlp.skill_extractor import extract_skills


def analyze_skill_gap(candidate_text, job_text):
    """Return missing skills between candidate resume and job description."""
    candidate_skills = set(extract_skills(candidate_text))
    job_skills = set(extract_skills(job_text))
    missing = job_skills - candidate_skills
    return {
        "candidate_skills": sorted(candidate_skills),
        "job_skills": sorted(job_skills),
        "missing_skills": sorted(missing),
    }
