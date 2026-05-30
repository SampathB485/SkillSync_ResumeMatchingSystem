def recommend_jobs(candidate_skills, jobs):
    """Recommend jobs based on candidate skills and available job skill sets."""
    recommendations = []
    for job in jobs:
        job_skills = set(job.get("skills", []))
        overlap = job_skills.intersection(candidate_skills)
        score = len(overlap) / max(1, len(job_skills))
        recommendations.append({"job": job, "score": score})
    return sorted(recommendations, key=lambda x: x["score"], reverse=True)
