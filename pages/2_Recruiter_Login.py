import streamlit as st

st.header("Recruiter Login")
st.write("This is the recruiter login page.")

with st.form("recruiter_login"):
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    submitted = st.form_submit_button("Login")

    if submitted:
        st.success("Recruiter login submitted.")
