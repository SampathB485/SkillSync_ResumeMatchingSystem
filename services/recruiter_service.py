from database.db_connection import get_connection


def register_recruiter(name, company_name, email, password):

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO Recruiter
            (name, company_name, email, password)
            VALUES (?, ?, ?, ?)
        """, (name, company_name, email, password))

        conn.commit()
        conn.close()

        return True, "Recruiter registered successfully!"

    except Exception as e:
        return False, str(e)