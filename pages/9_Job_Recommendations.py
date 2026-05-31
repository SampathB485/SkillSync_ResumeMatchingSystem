import streamlit as st
import pandas as pd

from services.candidate_service import get_candidate_by_id
from services.job_service import get_all_jobs
from services.match_service import compute_match_score
from nlp.skill_extractor import extract_skills

if not st.session_state.get("candidate_logged_in"):
    st.warning("Please login first.")
    st.switch_page("pages/4_Candidate_Login.py")

st.header("Job Recommendations")

candidate = get_candidate_by_id(st.session_state["candidate_id"])
if not candidate:
    st.error("Candidate record not found.")
    st.stop()

candidate_name = candidate[1]
resume_text = candidate[4] or ""

st.subheader(f"Welcome, {candidate_name}")

if not resume_text:
    st.warning("No resume text found. Please register with a resume or upload one first.")

jobs = get_all_jobs()
if not jobs:
    st.info("No jobs are available at the moment.")
    st.stop()

recommendations = []
for job_id, title, description, required_skills, experience_required, posted_date in jobs:
    job_text = f"{description}\n{required_skills}"
    score = compute_match_score(resume_text, job_text)
    candidate_skills = set(extract_skills(resume_text))
    job_skill_set = set(extract_skills(job_text))
    missing_skills = sorted(job_skill_set - candidate_skills)
    recommendations.append({
        "Job ID": job_id,
        "Job Title": title,
        "Match Score": round(score, 3),
        "Required Skills": required_skills,
        "Missing Skills": ", ".join(missing_skills) if missing_skills else "None",
        "Experience Required": experience_required,
        "Posted Date": posted_date,
    })

sorted_recommendations = sorted(recommendations, key=lambda item: item["Match Score"], reverse=True)

df = pd.DataFrame(sorted_recommendations)
if df.empty:
    st.info("No matching jobs found for your resume yet.")
else:
    st.write("### Recommended Jobs")
    st.dataframe(df, use_container_width=True)
    top = sorted_recommendations[:3]
    if top:
        st.write("### Top Matches")
        for job in top:
            st.markdown(
                f"**{job['Job Title']}** — Score: {job['Match Score']} \n\n"
                f"Required Skills: {job['Required Skills']}\n\n"
                f"Missing Skills: {job['Missing Skills']}\n\n"
                f"Experience Required: {job['Experience Required']} years\n\n"
                f"Posted Date: {job['Posted Date']}"
            )
