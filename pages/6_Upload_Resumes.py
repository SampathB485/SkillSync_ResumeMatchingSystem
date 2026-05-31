import streamlit as st
from pathlib import Path
import time

from nlp.resume_parser import parse_resume
from utils.validators import validate_resume_upload


if not st.session_state.get("logged_in"):
    st.warning("Please login first.")
    st.switch_page("pages/2_Recruiter_Login.py")


UPLOAD_DIR = Path(__file__).resolve().parent.parent / "uploads" / "resumes"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


st.header("Upload Resumes")
st.write("Upload candidate resumes to store them in the system.")


uploaded_files = st.file_uploader(
    "Upload resumes",
    accept_multiple_files=True,
    type=["pdf", "txt", "doc", "docx"]
)


if uploaded_files:
    saved_files = []
    errors = []
    
    for uploaded_file in uploaded_files:
        try:
            # Validate file
            is_valid, message = validate_resume_upload(uploaded_file.name, uploaded_file.size)
            
            if not is_valid:
                errors.append(f"❌ {uploaded_file.name}: {message}")
                continue
            
            # Save file
            timestamp = int(time.time() * 1000)  # milliseconds for uniqueness
            filename = f"{timestamp}_{uploaded_file.name}"
            file_path = UPLOAD_DIR / filename
            
            try:
                file_path.write_bytes(uploaded_file.getvalue())
                saved_files.append((file_path, uploaded_file.name))
            except IOError as e:
                errors.append(f"❌ {uploaded_file.name}: Failed to save file - {str(e)}")
                continue
                
        except Exception as e:
            errors.append(f"❌ {uploaded_file.name}: Unexpected error - {str(e)}")
            continue
    
    # Display results
    if saved_files:
        st.success(f"✓ {len(saved_files)} resume(s) uploaded successfully.")
        
        for saved_path, original_name in saved_files:
            with st.expander(f"📄 {original_name}"):
                try:
                    resume_text = parse_resume(str(saved_path))
                    if resume_text:
                        preview = resume_text[:500] + ("..." if len(resume_text) > 500 else "")
                        st.write("**Preview:**")
                        st.text(preview)
                    else:
                        st.info("Resume file was saved, but text extraction returned no content.")
                except Exception as e:
                    st.warning(f"Could not extract text from resume: {str(e)}")
    
    if errors:
        st.error("Some files could not be uploaded:")
        for error in errors:
            st.write(error)

