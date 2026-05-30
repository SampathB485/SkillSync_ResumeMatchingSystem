import streamlit as st

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
