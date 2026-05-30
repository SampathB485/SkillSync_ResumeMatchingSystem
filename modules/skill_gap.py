"""Skill gap analysis placeholder."""

def skill_gap(resume_skills, job_skills):
    """Return skills present in job_skills but missing from resume_skills."""
    return list(set(job_skills) - set(resume_skills))
