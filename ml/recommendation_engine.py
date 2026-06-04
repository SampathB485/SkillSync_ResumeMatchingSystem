from nlp.skill_extractor import extract_skills
from services.match_service import compute_match_score


def recommend_jobs(candidate_skills, jobs):
    """
    Recommend jobs based on candidate skills and available job skill sets.
    
    Args:
        candidate_skills (set or list): Skills the candidate has
        jobs (list): List of job dictionaries with 'skills' key
        
    Returns:
        list: Jobs sorted by match score (descending), with scores included
    """
    recommendations = []
    candidate_skill_set = set(candidate_skills) if not isinstance(candidate_skills, set) else candidate_skills
    
    for job in jobs:
        job_skills = set(job.get("skills", []))
        if not job_skills:
            score = 0.0
        else:
            overlap = job_skills.intersection(candidate_skill_set)
            score = len(overlap) / len(job_skills)
        
        recommendations.append({"job": job, "score": score})
    
    return sorted(recommendations, key=lambda x: x["score"], reverse=True)


def recommend_jobs_by_text(candidate_text, jobs_with_text):
    """
    Recommend jobs based on candidate resume text and job descriptions.
    Uses TF-IDF + skill-based matching for more accurate recommendations.
    
    Args:
        candidate_text (str): Candidate's resume text
        jobs_with_text (list): List of jobs, each with 'text' (job description) and other fields
        
    Returns:
        list: Jobs sorted by match score (descending), with detailed scoring info
    """
    if not candidate_text or not isinstance(candidate_text, str):
        candidate_text = ""
    
    recommendations = []
    
    for job in jobs_with_text:
        job_text = job.get("text", "")
        if not job_text:
            job_text = f"{job.get('description', '')}\n{job.get('required_skills', '')}"
        
        # Compute hybrid score (skill-based + TF-IDF)
        score = compute_match_score(candidate_text, job_text)
        
        # Extract skills for detailed analysis
        candidate_skills = set(extract_skills(candidate_text))
        job_skills = set(extract_skills(job_text))
        matched_skills = candidate_skills.intersection(job_skills)
        missing_skills = job_skills - candidate_skills
        
        recommendations.append({
            "job": job,
            "score": round(score, 3),
            "matched_skills": sorted(matched_skills),
            "missing_skills": sorted(missing_skills),
            "skill_match_count": len(matched_skills),
            "total_skills_required": len(job_skills)
        })
    
    return sorted(recommendations, key=lambda x: x["score"], reverse=True)
