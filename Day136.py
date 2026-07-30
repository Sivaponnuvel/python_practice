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


