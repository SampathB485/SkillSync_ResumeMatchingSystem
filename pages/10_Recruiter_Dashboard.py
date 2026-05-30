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

st.button("Create Job")

st.button("Upload Resume")

st.button("View Rankings")

st.button("Skill Gap Analysis")


st.divider()


if st.button("Logout"):

    st.session_state.clear()

    st.switch_page(
        "pages/2_Recruiter_Login.py"
    )