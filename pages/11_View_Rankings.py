import streamlit as st
import pandas as pd

from services.match_service import get_all_match_results

if not st.session_state.get("logged_in"):
    st.warning("Please login first.")
    st.switch_page("pages/2_Recruiter_Login.py")

st.header("Saved Candidate Rankings")
st.write("View previously computed candidate rankings for all jobs.")

results = get_all_match_results()
if not results:
    st.info("No ranking results are available yet. Run candidate ranking first.")
    st.stop()

columns = [
    "Result ID",
    "Candidate Name",
    "Job Title",
    "Match Score",
    "Missing Skills",
    "Ranking",
    "Posted Date",
]

df = pd.DataFrame(results, columns=columns)
st.dataframe(df, use_container_width=True)
