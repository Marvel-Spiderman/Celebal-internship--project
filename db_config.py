
import pyodbc

def fetch_employees():
    try:
        connection = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=xxx.xxx.xxx.xxx;'
            'DATABASE=CompanyDB;'
            'UID=YourUsername;'
            'PWD=YourPassword123'
        )
        cursor = connection.cursor()
        cursor.execute("SELECT TOP 5 * FROM Employees")
        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return results
    except Exception as e:
        print("Database connection error:", e)
        return []
