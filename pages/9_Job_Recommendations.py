import streamlit as st
import pandas as pd

from services.candidate_service import get_candidate_by_id
from services.job_service import get_all_jobs
from ml.recommendation_engine import recommend_jobs_by_text

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
    st.stop()

jobs = get_all_jobs()
if not jobs:
    st.info("No jobs are available at the moment.")
    st.stop()

# Prepare job data with text field for recommendation engine
jobs_with_data = []
for job_id, title, description, required_skills, experience_required, posted_date in jobs:
    job_text = f"{description}\n{required_skills}"
    jobs_with_data.append({
        "job_id": job_id,
        "title": title,
        "description": description,
        "required_skills": required_skills,
        "experience_required": experience_required,
        "posted_date": posted_date,
        "text": job_text
    })

# Get recommendations using the recommendation engine
recommendations = recommend_jobs_by_text(resume_text, jobs_with_data)

if not recommendations:
    st.info("No matching jobs found for your resume.")
    st.stop()

# Prepare data for display
display_data = []
for rec in recommendations:
    job = rec["job"]
    display_data.append({
        "Job ID": job["job_id"],
        "Job Title": job["title"],
        "Match Score": rec["score"],
        "Required Skills": job["required_skills"],
        "Missing Skills": ", ".join(rec["missing_skills"]) if rec["missing_skills"] else "None",
        "Matched Skills": len(rec["matched_skills"]),
        "Experience Required": job["experience_required"],
        "Posted Date": job["posted_date"],
    })

df = pd.DataFrame(display_data)
st.write("### Recommended Jobs")
st.dataframe(df, use_container_width=True)

# Display top matches with details
st.markdown("### 🌟 Top Matches")
top_matches = recommendations[:3]

for idx, rec in enumerate(top_matches, 1):
    job = rec["job"]
    with st.expander(f"{idx}. {job['title']} (Score: {rec['score']:.1%})", expanded=(idx == 1)):
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Match Score", f"{rec['score']:.1%}")
            st.metric("Skills Matched", f"{rec['skill_match_count']}/{rec['total_skills_required']}")
        with col2:
            st.metric("Experience Required", f"{job['experience_required']} years")
            st.write(f"**Posted:** {job['posted_date']}")
        
        st.write("**Job Description:**")
        st.text(job["description"][:500] + ("..." if len(job["description"]) > 500 else ""))
        
        st.write("**Required Skills:**")
        st.write(job["required_skills"])
        
        if rec["matched_skills"]:
            st.write("✅ **Your Matching Skills:**")
            st.write(", ".join(rec["matched_skills"]))
        
        if rec["missing_skills"]:
            st.write("📚 **Skills to Develop:**")
            st.write(", ".join(rec["missing_skills"]))
