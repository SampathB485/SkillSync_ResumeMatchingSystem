"""Matcher - computes match score between resume and job."""
from nlp.skill_extractor import extract_skills


def match(resume_data, job_data):
    """
    Compute matching score between a resume and a job (0-1).
    
    Args:
        resume_data (dict or str): Resume data or text
        job_data (dict or str): Job data or text
        
    Returns:
        float: Match score between 0 and 1
    """
    # Handle string input (text) or dict input (structured data)
    if isinstance(resume_data, str):
        resume_text = resume_data
    else:
        resume_text = resume_data.get("text", "") if isinstance(resume_data, dict) else str(resume_data)
    
    if isinstance(job_data, str):
        job_text = job_data
    else:
        job_text = job_data.get("text", "") if isinstance(job_data, dict) else str(job_data)
    
    # Extract skills from both
    resume_skills = set(extract_skills(resume_text))
    job_skills = set(extract_skills(job_text))
    
    # If no job skills defined, return 0
    if not job_skills:
        return 0.0
    
    # Calculate skill overlap percentage
    skill_overlap = len(resume_skills.intersection(job_skills)) / len(job_skills)
    
    return round(skill_overlap, 3)
