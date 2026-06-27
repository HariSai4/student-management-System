import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="student_db"
)

cursor = conn.cursor()

student_id = int(input("Enter Student ID to delete: "))

query = "DELETE FROM students WHERE id = %s"
cursor.execute(query, (student_id,))

conn.commit()

if cursor.rowcount > 0:
    print("Student deleted successfully!")
else:
    print("Student not found.")

cursor.close()
conn.close()
def delete_student():
    selected = table.selection()

    if not selected:
        messagebox.showerror("Error", "Please select a student")
        return

    student = table.item(selected[0])
    student_id = student["values"][0]

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id = %s",
        (student_id,)
    )

    conn.commit()

    cursor.close()
    conn.close()

    messagebox.showinfo("Success", "Student Deleted Successfully!")
    load_students()
tk.Button(
    root,
    text="Delete Student",
    command=delete_student,
    width=20
).grid(row=4, column=2, pady=10)