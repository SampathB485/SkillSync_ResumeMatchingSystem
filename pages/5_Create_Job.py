import streamlit as st

if not st.session_state.get("logged_in"):

    st.warning(
        "Please login first."
    )

    st.switch_page(
        "pages/2_Recruiter_Login.py"
    )
#Dont change the above code. It is used to check if the recruiter is logged in or not. If not, it redirects to the login page.

st.header("Create Job")
st.write("This is the job creation page.")

with st.form("create_job"):
    title = st.text_input("Job Title")
    description = st.text_area("Job Description")
    skills = st.text_input("Required Skills")
    location = st.text_input("Location")
    submitted = st.form_submit_button("Create Job")

    if submitted:
        st.success("Job created successfully.")
