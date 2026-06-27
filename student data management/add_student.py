import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="student_db"
)

cursor = conn.cursor()

name = input("Enter Name: ")
age = int(input("Enter Age: "))
course = input("Enter Course: ")
email = input("Enter Email: ")

query = """
INSERT INTO students(name, age, course, email)
VALUES (%s, %s, %s, %s)
"""

values = (name, age, course, email)

cursor.execute(query, values)
conn.commit()

print("Student added successfully!")