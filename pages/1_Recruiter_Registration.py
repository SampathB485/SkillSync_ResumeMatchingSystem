import streamlit as st

from services.recruiter_service import register_recruiter
from utils.validators import (
    validate_email,
    validate_password
)

st.title("Recruiter Registration")

name = st.text_input("Full Name")

company_name = st.text_input("Company Name")

email = st.text_input("Email")

password = st.text_input(
    "Password",
    type="password"
)

if st.button("Register"):

    if not name:
        st.error("Name is required")

    elif not company_name:
        st.error("Company name is required")

    elif not validate_email(email):
        st.error("Enter a valid email")

    elif not validate_password(password):
        st.error(
            "Password must be at least 6 characters"
        )

    else:

        success, message = register_recruiter(
            name,
            company_name,
            email,
            password
        )

        if success:
            st.success(message)

        else:
            st.error(message)