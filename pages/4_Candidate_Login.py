import streamlit as st

from services.candidate_service import login_candidate

st.header("Candidate Login")

with st.form("candidate_login"):
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    submitted = st.form_submit_button("Login")

    if submitted:
        candidate = login_candidate(email, password)
        if candidate:
            st.session_state["candidate_logged_in"] = True
            st.session_state["candidate_id"] = candidate[0]
            st.session_state["candidate_name"] = candidate[1]
            st.session_state["candidate_email"] = candidate[2]
            st.success("Login Successful")
            st.write("You are now logged in as a candidate.")
            if st.button("Go to Job Recommendations"):
                st.switch_page("pages/9_Job_Recommendations.py")
        else:
            st.error("Invalid Email or Password")
