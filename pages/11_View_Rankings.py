import streamlit as st

if not st.session_state.get("logged_in"):

    st.warning(
        "Please login first."
    )

    st.switch_page(
        "pages/2_Recruiter_Login.py"
    )
#Dont change the above code. It is used to check if the recruiter is logged in or not. If not, it redirects to the login page.