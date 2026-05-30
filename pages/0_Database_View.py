import streamlit as st
import pandas as pd

from database.db_connection import get_connection


st.title("Database Viewer")


conn = get_connection()


tables = [
    "Recruiter",
    "Job",
    "Candidate",
    "MatchResult"
]


selected_table = st.selectbox(
    "Select Table",
    tables
)


query = f"SELECT * FROM {selected_table}"

df = pd.read_sql_query(
    query,
    conn
)

st.dataframe(
    df,
    use_container_width=True
)

conn.close()