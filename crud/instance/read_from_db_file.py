import sqlite3

def read_from_database(db_file):
    try:
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Applicant") 
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print("Error reading data from SQLite table:", error)
    finally:
        if connection:
            connection.close()

db_file_path = "data.db"
read_from_database(db_file_path)
