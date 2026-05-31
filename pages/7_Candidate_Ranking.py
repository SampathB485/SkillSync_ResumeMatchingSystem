import streamlit as st
import pandas as pd

from services.job_service import get_jobs_by_recruiter, get_job_by_id
from services.candidate_service import get_all_candidates_with_text
from services.match_service import evaluate_candidate_for_job, save_match_result

if not st.session_state.get("logged_in"):
    st.warning("Please login first.")
    st.switch_page("pages/2_Recruiter_Login.py")

st.header("Candidate Ranking")
st.write("Rank candidates for your open job postings using skill match and keyword overlap.")

jobs = get_jobs_by_recruiter(st.session_state["recruiter_id"])
if not jobs:
    st.info("You have no jobs yet. Create a job before ranking candidates.")
    st.stop()

job_options = {job[0]: f"{job[1]} ({job[0]})" for job in jobs}
selected_job_id = st.selectbox("Select a job to rank candidates", list(job_options.keys()), format_func=lambda x: job_options[x])

if st.button("Run Candidate Ranking"):
    job = get_job_by_id(selected_job_id)
    candidates = get_all_candidates_with_text()
    if not candidates:
        st.info("No candidates with parsed resumes are available yet.")
        st.stop()

    rankings = []
    for candidate in candidates:
        result = evaluate_candidate_for_job(candidate, job)
        rankings.append(
            {
                "Candidate ID": candidate[0],
                "Candidate Name": candidate[1],
                "Match Score": result["score"],
                "Missing Skills": ", ".join(result["missing_skills"]) if result["missing_skills"] else "None",
                "Matched Skills": ", ".join(result["matched_skills"]) if result["matched_skills"] else "None",
                "Resume Path": candidate[3] or "Not available",
            }
        )

    rankings = sorted(rankings, key=lambda item: item["Match Score"], reverse=True)
    for rank, item in enumerate(rankings, start=1):
        save_match_result(item["Candidate ID"], selected_job_id, item["Match Score"], item["Missing Skills"].split(", ") if item["Missing Skills"] != "None" else [], rank)
        item["Ranking"] = rank

    df = pd.DataFrame(rankings)
    st.success("Candidate ranking completed.")
    st.dataframe(df, use_container_width=True)
    st.markdown("### Top Candidate")
    if not df.empty:
        top = df.iloc[0]
        st.write(f"**{top['Candidate Name']}** — Score {top['Match Score']}")
