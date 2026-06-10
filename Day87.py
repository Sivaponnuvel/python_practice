# Question 1 – Search Student by ID (WHERE)
# Create a program to:
# 👉 Take student ID from user
# 👉 Search using:
# SELECT * FROM students WHERE id = %s
# 👉 If found:
# Student Found ✅
# ID: 1
# Name: Siva
# Age: 23
# 👉 Otherwise:
# Student Not Found ❌
# ⚠️ Use:
# fetchone()
# WHERE

import mysql.connector

con =  mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "student_db",
    password = "siva2025"
)
cursor = con.cursor()

student_id = int(input("Enter ID: "))
cursor.execute("select * from students where id = %s",(student_id,))

details = cursor.fetchone()

if details:
    print("Student Found ✅")
    print(f"ID: {details[0]}")
    print(f"Name: {details[1]}")
    print(f"Age: {details[2]}")
else:
    print("Student Not Found ❌")


