import streamlit as st

st.header("Upload Resumes")
st.write("This is the resume upload page.")

uploaded_files = st.file_uploader("Upload resumes", accept_multiple_files=True)
if uploaded_files:
    st.success(f"{len(uploaded_files)} file(s) uploaded.")
