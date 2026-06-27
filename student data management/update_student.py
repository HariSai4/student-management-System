import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="student_db"
)

cursor = conn.cursor()

student_id = int(input("Enter Student ID to update: "))
new_email = input("Enter new email: ")

query = "UPDATE students SET email = %s WHERE id = %s"
cursor.execute(query, (new_email, student_id))

conn.commit()

if cursor.rowcount > 0:
    print("Student updated successfully!")
else:
    print("Student not found.")

cursor.close()
conn.close()