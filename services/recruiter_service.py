from database.db_connection import get_connection


def register_recruiter(name, company_name, email, password):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO Recruiter
        (name, company_name, email, password)
        VALUES (?, ?, ?, ?)
    """, (name, company_name, email, password))

    conn.commit()
    conn.close()


def login_recruiter(email, password):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT recruiter_id,
               name,
               company_name
        FROM Recruiter
        WHERE email = ?
        AND password = ?
    """, (email, password))

    recruiter = cursor.fetchone()

    conn.close()

    return recruiter