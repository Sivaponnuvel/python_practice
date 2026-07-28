# 🔹 Question 1 – Delete a Student by ID
# Write a Python program to delete a student from the students table using the student's ID.
# Table: students
# Column Name	Type
# id	INT
# name	VARCHAR
# age	INT
# Program Flow
# Take the student ID from the user.
# Delete the student whose ID matches the entered value.
# If a record is deleted, display:
# Student Deleted Successfully ✅
# Otherwise, display:
# Student Not Found ❌
# Example
# Input
# Enter Student ID: 3
# Output
# Student Deleted Successfully ✅
# ⚠️ Conditions
# ✅ Take input from the user
# ✅ Use a parameterized query (%s)
# ✅ Use DELETE
# ✅ Use commit()
# ✅ Check the result using cursor.rowcount
# ❌ Don't use SELECT before DELETE
# ❌ Don't use more than one SQL query

import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "student_db",
    password = "siva2025"
)
cursor = con.cursor()

stu_id = int(input("Enter Student ID: "))
cursor.execute("delete from students where id = %s",(stu_id,))
con.commit()

if cursor.rowcount > 0:
    print("Student Deleted Successfully ✅")
else:
    print("Student Not Found ❌")


