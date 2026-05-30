import streamlit as st

from services.job_service import create_job


if not st.session_state.get("logged_in"):

    st.warning("Please login first.")

    st.switch_page(
        "pages/2_Recruiter_Login.py"
    )


st.header("Create Job")


with st.form("create_job_form"):

    job_title = st.text_input(
        "Job Title"
    )

    job_description = st.text_area(
        "Job Description"
    )

    required_skills = st.text_input(
        "Required Skills (comma separated)"
    )

    experience_required = st.number_input(
        "Experience Required (Years)",
        min_value=0,
        max_value=30,
        value=0
    )

    submit = st.form_submit_button(
        "Create Job"
    )

    if submit:

        create_job(
            recruiter_id=st.session_state["recruiter_id"],
            job_title=job_title,
            job_description=job_description,
            required_skills=required_skills,
            experience_required=experience_required
        )

        st.success(
            "Job Created Successfully"
        )