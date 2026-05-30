import streamlit as st

st.header("Candidate Login")
st.write("This is the candidate login page.")

with st.form("candidate_login"):
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    submitted = st.form_submit_button("Login")

    if submitted:
        st.success("Candidate login submitted.")
