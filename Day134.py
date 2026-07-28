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


# 🔹 Question 2 – Delete Students Younger Than a Given Age
# Write a Python program to delete all students whose age is less than the age entered by the user.
# Table: students
# Column Name	Type
# id	INT
# name	VARCHAR
# age	INT
# Program Flow
# Take an age from the user.
# Delete all students whose age is less than the entered age.
# If records are deleted, display:
# Total Students Deleted: <count>
# Otherwise, display:
# No Students Deleted ❌
# Example
# Input
# Enter Age: 20
# Suppose the table contains:
# id	name	age
# 1	Siva	18
# 2	Rahul	21
# 3	Priya	19
# 4	Vijay	22
# After execution:
# id	name	age
# 2	Rahul	21
# 4	Vijay	22
# Output
# Total Students Deleted: 2
# ⚠️ Conditions
# ✅ Use one DELETE query
# ✅ Use a parameterized query (%s)
# ✅ Use commit()
# ✅ Use cursor.rowcount
# ❌ Don't delete records in Python
# ❌ Don't use SELECT before DELETE
# ❌ Don't use more than one SQL query

age = int(input("Enter Age: "))
cursor.execute("delete from students where age < %s",(age,))
con.commit()

if cursor.rowcount > 0:
    print(f"Total Students Deleted: {cursor.rowcount}")
else:
    print("No Students Deleted ❌")

cursor.close()
con.close()