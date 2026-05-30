import streamlit as st


if not st.session_state.get("logged_in"):

    st.warning(
        "Please login first."
    )

    st.switch_page(
        "pages/2_Recruiter_Login.py"
    )


st.title("Recruiter Dashboard")


st.subheader(
    f"Welcome, {st.session_state['recruiter_name']}"
)

st.write(
    f"Company: {st.session_state['company_name']}"
)


st.divider()

st.write("Recruiter Functions")


if st.button("Create Job"):

    st.switch_page(
        "pages/5_Create_Job.py"
    )


if st.button("View Jobs"):

    st.switch_page(
        "pages/12_View_Jobs.py"
    )


if st.button("Upload Resume"):

    st.switch_page(
        "pages/6_Upload_Resumes.py"
    )


if st.button("View Rankings"):

    st.switch_page(
        "pages/11_View_Rankings.py"
    )


if st.button("Skill Gap Analysis"):

    st.switch_page(
        "pages/8_Skill_Gap_Analysis.py"
    )


st.divider()


if st.button("Logout"):

    st.session_state.clear()

    st.switch_page(
        "pages/2_Recruiter_Login.py"
    )