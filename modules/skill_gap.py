"""Skill gap analysis - identifies missing skills and gaps."""


def skill_gap(resume_skills, job_skills):
    """
    Analyze skill gap between resume and job requirements.
    
    Args:
        resume_skills (list): Skills the candidate has
        job_skills (list): Skills the job requires
        
    Returns:
        list: Skills present in job_skills but missing from resume_skills
    """
    resume_set = set(resume_skills) if isinstance(resume_skills, (list, set)) else set()
    job_set = set(job_skills) if isinstance(job_skills, (list, set)) else set()
    
    missing_skills = sorted(list(job_set - resume_set))
    return missing_skills


def analyze_skill_gap(resume_skills, job_skills):
    """
    Perform detailed skill gap analysis.
    
    Args:
        resume_skills (list): Skills the candidate has
        job_skills (list): Skills the job requires
        
    Returns:
        dict: Detailed gap analysis including matched, missing, and extra skills
    """
    resume_set = set(resume_skills) if isinstance(resume_skills, (list, set)) else set()
    job_set = set(job_skills) if isinstance(job_skills, (list, set)) else set()
    
    matched_skills = sorted(list(resume_set.intersection(job_set)))
    missing_skills = sorted(list(job_set - resume_set))
    extra_skills = sorted(list(resume_set - job_set))
    
    gap_percentage = (len(missing_skills) / len(job_set) * 100) if job_set else 0
    
    return {
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "extra_skills": extra_skills,
        "gap_percentage": round(gap_percentage, 2),
        "match_percentage": round(100 - gap_percentage, 2),
        "total_required": len(job_set),
        "total_matched": len(matched_skills),
        "total_missing": len(missing_skills)
    }
