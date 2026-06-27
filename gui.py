import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector

# ---------------- DATABASE CONNECTION ----------------
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root123",   # Replace with your MySQL password
        database="student_db"
    )

# ---------------- ADD STUDENT ----------------
def add_student():
    name = name_entry.get()
    age = age_entry.get()
    course = course_entry.get()
    email = email_entry.get()

    if not name or not age or not course or not email:
        messagebox.showerror("Error", "Please fill all fields")
        return

    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO students(name, age, course, email)
        VALUES (%s, %s, %s, %s)
        """

        values = (name, age, course, email)

        cursor.execute(query, values)
        conn.commit()

        messagebox.showinfo("Success", "Student Added Successfully!")

        # Clear entry boxes
        name_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)
        course_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)

        load_students()

        cursor.close()
        conn.close()

    except Exception as e:
        messagebox.showerror("Database Error", str(e))

# ---------------- LOAD STUDENTS ----------------
def load_students():
    for row in table.get_children():
        table.delete(row)

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()

        for student in students:
            table.insert("", tk.END, values=student)

        cursor.close()
        conn.close()

    except Exception as e:
        messagebox.showerror("Database Error", str(e))

# ---------------- GUI WINDOW ----------------
root = tk.Tk()
root.title("Student Management System")
root.geometry("850x500")

# Labels
tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=10)
tk.Label(root, text="Age").grid(row=1, column=0, padx=10, pady=10)
tk.Label(root, text="Course").grid(row=2, column=0, padx=10, pady=10)
tk.Label(root, text="Email").grid(row=3, column=0, padx=10, pady=10)

# Entry boxes
name_entry = tk.Entry(root, width=30)
age_entry = tk.Entry(root, width=30)
course_entry = tk.Entry(root, width=30)
email_entry = tk.Entry(root, width=30)

name_entry.grid(row=0, column=1)
age_entry.grid(row=1, column=1)
course_entry.grid(row=2, column=1)
email_entry.grid(row=3, column=1)

# Add Button
tk.Button(
    root,
    text="Add Student",
    command=add_student,
    width=20
).grid(row=4, column=1, pady=10)

# Table
table = ttk.Treeview(
    root,
    columns=("ID", "Name", "Age", "Course", "Email"),
    show="headings"
)

table.heading("ID", text="ID")
table.heading("Name", text="Name")
table.heading("Age", text="Age")
table.heading("Course", text="Course")
table.heading("Email", text="Email")

table.column("ID", width=50)
table.column("Name", width=150)
table.column("Age", width=80)
table.column("Course", width=150)
table.column("Email", width=250)

table.grid(row=5, column=0, columnspan=3, padx=10, pady=20)

# Load existing students
load_students()

root.mainloop()