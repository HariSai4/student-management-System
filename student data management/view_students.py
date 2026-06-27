import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="student_db"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM students")

students = cursor.fetchall()

if len(students) == 0:
    print("No students found.")
else:
    print("\n--- Student Records ---")
    for student in students:
        print(f"ID: {student[0]}")
        print(f"Name: {student[1]}")
        print(f"Age: {student[2]}")
        print(f"Course: {student[3]}")
        print(f"Email: {student[4]}")
        print("-" * 30)

cursor.close()
conn.close()