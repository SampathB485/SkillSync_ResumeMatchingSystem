import streamlit as st
from pathlib import Path
import time

from nlp.resume_parser import parse_resume

if not st.session_state.get("logged_in"):
    st.warning("Please login first.")
    st.switch_page("pages/2_Recruiter_Login.py")

UPLOAD_DIR = Path(__file__).resolve().parent.parent / "uploads" / "resumes"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

st.header("Upload Resumes")
st.write("Upload candidate resumes to store them in the system.")

uploaded_files = st.file_uploader("Upload resumes", accept_multiple_files=True)

if uploaded_files:
    saved_files = []
    for uploaded_file in uploaded_files:
        filename = f"{int(time.time())}_{uploaded_file.name}"
        file_path = UPLOAD_DIR / filename
        file_path.write_bytes(uploaded_file.getvalue())
        saved_files.append(file_path)

    if saved_files:
        st.success(f"{len(saved_files)} resume(s) uploaded successfully.")
        for saved_path in saved_files:
            resume_text = parse_resume(saved_path)
            st.write(f"**{saved_path.name}** uploaded.")
            if resume_text:
                st.write(resume_text[:500] + ("..." if len(resume_text) > 500 else ""))
            else:
                st.info("Uploaded resume file was saved, but text extraction returned no content.")
