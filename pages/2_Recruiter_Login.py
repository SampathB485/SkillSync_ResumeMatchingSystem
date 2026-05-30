import streamlit as st

from services.recruiter_service import login_recruiter


st.title("Recruiter Login")


email = st.text_input("Email")

password = st.text_input(
    "Password",
    type="password"
)


if st.button("Login"):

    recruiter = login_recruiter(
        email,
        password
    )

    if recruiter:

        st.session_state["logged_in"] = True
        st.session_state["recruiter_id"] = recruiter[0]
        st.session_state["recruiter_name"] = recruiter[1]
        st.session_state["company_name"] = recruiter[2]

        st.success("Login Successful")

        st.switch_page(
            "pages/10_Recruiter_Dashboard.py"
        )

    else:

        st.error(
            "Invalid Email or Password"
        )