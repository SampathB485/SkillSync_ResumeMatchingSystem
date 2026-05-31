import streamlit as st
import pandas as pd

from services.job_service import get_jobs_by_recruiter, get_job_by_id
from services.candidate_service import get_all_candidates_with_text
from services.match_service import evaluate_candidate_for_job

if not st.session_state.get("logged_in"):
    st.warning("Please login first.")
    st.switch_page("pages/2_Recruiter_Login.py")

st.header("Skill Gap Analysis")
st.write("Identify the strongest candidates and the missing skills they need for a given job.")

jobs = get_jobs_by_recruiter(st.session_state["recruiter_id"])
if not jobs:
    st.info("You have no jobs yet. Add a job first to run skill-gap analysis.")
    st.stop()

job_options = {job[0]: f"{job[1]} ({job[0]})" for job in jobs}
selected_job_id = st.selectbox("Select a job for skill gap analysis", list(job_options.keys()), format_func=lambda x: job_options[x])

if st.button("Analyze Skill Gap"):
    job = get_job_by_id(selected_job_id)
    candidates = get_all_candidates_with_text()
    if not candidates:
        st.info("No candidates with parsed resumes are available yet.")
        st.stop()

    gap_data = []
    for candidate in candidates:
        result = evaluate_candidate_for_job(candidate, job)
        gap_data.append(
            {
                "Candidate Name": candidate[1],
                "Match Score": result["score"],
                "Missing Skills": ", ".join(result["missing_skills"]) if result["missing_skills"] else "None",
                "Skill Overlap": len(result["matched_skills"]),
                "Total Required Skills": len(result["job_skills"]),
                "Resume Available": "Yes" if candidate[3] else "No",
            }
        )

    df = pd.DataFrame(sorted(gap_data, key=lambda item: item["Match Score"], reverse=True))
    st.dataframe(df, use_container_width=True)
    st.markdown("### Suggested next steps")
    st.write("Use this table to identify skills candidates need for the selected job.")
