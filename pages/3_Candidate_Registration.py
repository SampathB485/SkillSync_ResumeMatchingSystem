import streamlit as st

st.header("Candidate Registration")
st.write("This is the candidate registration page.")

with st.form("candidate_registration"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    resume = st.file_uploader("Upload Resume")
    submitted = st.form_submit_button("Register")

    if submitted:
        st.success("Candidate registration submitted.")
