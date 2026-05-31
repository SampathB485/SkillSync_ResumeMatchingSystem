import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR / "database" / "skillsync.db"

conn = sqlite3.connect(DATABASE_PATH)
cursor = conn.cursor()

# Recruiter Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Recruiter (
    recruiter_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    company_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")

# Job Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Job (
    job_id INTEGER PRIMARY KEY AUTOINCREMENT,
    recruiter_id INTEGER,
    job_title TEXT NOT NULL,
    job_description TEXT NOT NULL,
    required_skills TEXT NOT NULL,
    experience_required INTEGER,
    posted_date TEXT,
    FOREIGN KEY (recruiter_id)
        REFERENCES Recruiter(recruiter_id)
)
""")

# Candidate Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Candidate (
    candidate_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    resume_path TEXT,
    resume_text TEXT,
    job_id INTEGER,
    FOREIGN KEY (job_id)
        REFERENCES Job(job_id)
)
""")

# MatchResult Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS MatchResult (
    result_id INTEGER PRIMARY KEY AUTOINCREMENT,
    candidate_id INTEGER,
    job_id INTEGER,
    match_score REAL,
    missing_skills TEXT,
    ranking INTEGER,
    FOREIGN KEY (candidate_id)
        REFERENCES Candidate(candidate_id),
    FOREIGN KEY (job_id)
        REFERENCES Job(job_id)
)
""")

cursor.execute("PRAGMA table_info(Candidate)")
columns = [row[1] for row in cursor.fetchall()]
if "password" not in columns:
    cursor.execute("ALTER TABLE Candidate ADD COLUMN password TEXT")
if "resume_text" not in columns:
    cursor.execute("ALTER TABLE Candidate ADD COLUMN resume_text TEXT")

conn.commit()
conn.close()

print("Database and tables created successfully!")