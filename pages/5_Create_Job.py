import streamlit as st

from services.job_service import create_job
from utils.validators import validate_job_input


if not st.session_state.get("logged_in"):

    st.warning("Please login first.")

    st.switch_page(
        "pages/2_Recruiter_Login.py"
    )


st.header("Create Job")


with st.form("create_job_form"):

    job_title = st.text_input(
        "Job Title",
        placeholder="e.g., Senior Python Developer"
    )

    job_description = st.text_area(
        "Job Description",
        placeholder="Describe the job responsibilities and requirements...",
        height=200
    )

    required_skills = st.text_input(
        "Required Skills (comma separated)",
        placeholder="e.g., Python, Django, PostgreSQL, REST API"
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
        # Validate inputs
        is_valid, message = validate_job_input(job_title, job_description, required_skills)
        
        if not is_valid:
            st.error(message)
        else:
            # Create the job
            success, response_message = create_job(
                recruiter_id=st.session_state["recruiter_id"],
                job_title=job_title.strip(),
                job_description=job_description.strip(),
                required_skills=required_skills.strip(),
                experience_required=experience_required
            )
            
            if success:
                st.success(response_message)
                st.balloons()
            else:
                st.error(response_message)