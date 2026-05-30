import streamlit as st

st.set_page_config(
    page_title="SkillSync",
    page_icon="📄",
    layout="wide"
)

st.title("📄 SkillSync")
st.subheader("Intelligent Resume Screening and Job Matching System")

st.write(
    """
    Welcome to SkillSync.

    This system helps recruiters and job seekers by:
    
    - Resume Analysis
    - Skill Extraction
    - Job Matching
    - Candidate Ranking
    - Skill Gap Analysis
    """
)

st.success("System Initialized Successfully!")