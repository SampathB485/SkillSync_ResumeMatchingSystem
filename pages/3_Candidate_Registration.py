import streamlit as st
from pathlib import Path
import time

from nlp.resume_parser import parse_resume
from services.candidate_service import register_candidate
from utils.validators import validate_email, validate_password

UPLOAD_DIR = Path(__file__).resolve().parent.parent / "uploads" / "resumes"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

st.header("Candidate Registration")

with st.form("candidate_registration"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    resume = st.file_uploader("Upload Resume")
    submitted = st.form_submit_button("Register")

    if submitted:
        if not name:
            st.error("Name is required.")
        elif not validate_email(email):
            st.error("Enter a valid email.")
        elif not validate_password(password):
            st.error("Password must be at least 6 characters.")
        else:
            resume_path = None
            resume_text = ""
            if resume is not None:
                filename = f"{int(time.time())}_{resume.name}"
                saved_path = UPLOAD_DIR / filename
                saved_path.write_bytes(resume.getvalue())
                resume_path = str(saved_path)
                resume_text = parse_resume(resume_path)

            success, message = register_candidate(
                name,
                email,
                password,
                resume_path=resume_path,
                resume_text=resume_text,
            )

            if success:
                st.success(message)
                st.info("You can now login using the Candidate Login page.")
            else:
                st.error(message)
