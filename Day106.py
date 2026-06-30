# 🔹 Question 1 – Display Student Details Using Column Aliases
# Using table:
# students
# Write a Python program to:
# 👉 Fetch all student records.
# Use the following query:
# SELECT
#     id AS Student_ID,
#     name AS Student_Name,
#     age AS Student_Age
# FROM students;
# Display the records like:
# --- Student Details ---
# Student ID   : 1
# Student Name : Siva
# Student Age  : 23
# Student ID   : 2
# Student Name : Ram
# Student Age  : 21
# If the table is empty:
# No Students Found ❌
# ⚠️ Conditions
# ✅ Use AS (column aliases)
# ✅ Use fetchall()
# ✅ Display using a loop
# ❌ Don't rename columns in Python
# ❌ Don't use SELECT *

import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "student_db",
    password = "siva2025"
)
cursor = con.cursor()

cursor.execute("select id as Student_ID, name as Student_Name, age as Student_Age from students")
details = cursor.fetchall()

if details:
    print("--- Student Details ---")
    for i in details:
        print(f"Student ID   : {i[0]}")
        print(f"Student Name : {i[1]}")
        print(f"Student Age  : {i[2]}")
else:
    print("No Students Found ❌")


