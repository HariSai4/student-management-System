import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="student_db"
)

cursor = conn.cursor()

student_id = int(input("Enter Student ID: "))

query = "SELECT * FROM students WHERE id = %s"
cursor.execute(query, (student_id,))

student = cursor.fetchone()

if student:
    print("\nStudent Found")
    print("ID:", student[0])
    print("Name:", student[1])
    print("Age:", student[2])
    print("Course:", student[3])
    print("Email:", student[4])
else:
    print("Student not found.")

cursor.close()
conn.close()