import streamlit as st
import pandas as pd

from services.job_service import get_jobs_by_recruiter


if not st.session_state.get("logged_in"):

    st.warning("Please login first.")

    st.switch_page(
        "pages/2_Recruiter_Login.py"
    )


st.header("My Jobs")


jobs = get_jobs_by_recruiter(
    st.session_state["recruiter_id"]
)


if jobs:

    df = pd.DataFrame(
        jobs,
        columns=[
            "Job ID",
            "Job Title",
            "Required Skills",
            "Experience",
            "Posted Date"
        ]
    )

    st.dataframe(
        df,
        use_container_width=True
    )

else:

    st.info(
        "No jobs created yet."
    )