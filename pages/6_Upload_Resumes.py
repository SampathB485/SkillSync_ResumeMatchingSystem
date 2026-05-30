import streamlit as st

if not st.session_state.get("logged_in"):

    st.warning(
        "Please login first."
    )

    st.switch_page(
        "pages/2_Recruiter_Login.py"
    )
#Dont change the above code. It is used to check if the recruiter is logged in or not. If not, it redirects to the login page.

st.header("Upload Resumes")
st.write("This is the resume upload page.")

uploaded_files = st.file_uploader("Upload resumes", accept_multiple_files=True)
if uploaded_files:
    st.success(f"{len(uploaded_files)} file(s) uploaded.")
