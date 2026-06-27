import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="student_db"
)

cursor = conn.cursor()
cursor.execute("SHOW TABLES")

for table in cursor:
    print(table)