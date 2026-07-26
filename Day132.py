# 🔹 Question 1 – Update a Student's Age
# Write a Python program to update the age of a student using the student's ID.
# Table: students
# Column Name	Type
# id	INT
# name	VARCHAR
# age	INT
# Program Flow
# Take the student ID from the user.
# Take the new age from the user.
# Update the student's age.
# If the update is successful, display:
# Student Age Updated Successfully ✅
# Otherwise, display:
# Student Not Found ❌
# Example
# Input
# Enter Student ID: 2
# Enter New Age: 23
# Output
# Student Age Updated Successfully ✅
# ⚠️ Conditions
# ✅ Take input from the user
# ✅ Use a parameterized query (%s)
# ✅ Use UPDATE
# ✅ Use commit()
# ✅ Check the result using cursor.rowcount
# ❌ Don't use SELECT before UPDATE
# ❌ Don't use more than one SQL query

import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "student_db",
    password = "siva2025"
)
cursor = con.cursor()

student_id = int(input("Enter Student ID: "))
student_age = int(input("Enter New Age: "))

cursor.execute("update students set age = %s where id = %s",(student_age, student_id))
con.commit()

if cursor.rowcount > 0:
    print("Student Age Updated Successfully ✅")
else:
    print("Student Not Found ❌")


