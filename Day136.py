# 🔹 Question 1 – Insert a New Student
# Write a Python program to insert a new student into the students table.
# Table: students
# Column Name	Type
# id	INT
# name	VARCHAR
# age	INT
# Program Flow
# Take the student's name from the user.
# Take the student's age from the user.
# Insert the record into the table.
# If the record is inserted successfully, display:
# Student Added Successfully ✅
# Example
# Input
# Enter Student Name: Arun
# Enter Student Age: 22
# Output
# Student Added Successfully ✅
# ⚠️ Conditions
# ✅ Take input from the user
# ✅ Use a parameterized query (%s)
# ✅ Use INSERT INTO
# ✅ Use commit()
# ✅ Check the result using cursor.rowcount
# ❌ Don't use SELECT
# ❌ Don't use more than one SQL query

import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "student_db",
    password = "siva2025"
)
cursor = con.cursor()

name = input("Enter Sutdent Name: ")
age = int(input("Enter Student Age: "))

cursor.execute("insert into students(name,age) values(%s, %s)",(name, age))
con.commit()

if cursor.rowcount > 0:
    print("Student Added Successfully ✅")


# 🔹 Question 2 – Insert Multiple Students
# Write a Python program to insert multiple student records into the students table.
# Table: students
# Column Name	Type
# id	INT
# name	VARCHAR
# age	INT
# Program Flow
# Ask the user how many students they want to insert.
# Use a loop to get each student's:
# Name
# Age
# Insert each student into the database.
# After all insertions are complete, commit the transaction once.
# Display:
# Total Students Added: <count>
# Example
# Input
# How Many Students: 2
# Enter Student 1 Name: Priya
# Enter Student 1 Age: 20
# Enter Student 2 Name: Rahul
# Enter Student 2 Age: 21
# Output
# Total Students Added: 2
# ⚠️ Conditions
# ✅ Take the number of students from the user
# ✅ Use a loop
# ✅ Use a parameterized query (%s)
# ✅ Use INSERT INTO
# ✅ Call commit() only once after the loop
# ✅ Use cursor.rowcount
# ❌ Don't use executemany()
# ❌ Don't use more than one INSERT statement inside the loop

n = int(input("How Many Students: "))
total_students = 0

for i in range(1, n + 1):
    name1 = input(f"Enter Student {i} Name: ")
    age1 = int(input(f"Enter Student {i} Age: "))

    cursor.execute("insert into students(name,age) values(%s, %s)",(name1, age1))

    if cursor.rowcount > 0:
        total_students += cursor.rowcount

con.commit()

print(f"Total Students Added: {total_students}")

cursor.close()
con.close()