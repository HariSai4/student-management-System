import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123"
)

cursor = conn.cursor()
cursor.execute("SHOW DATABASES")

for db in cursor:
    print(db)