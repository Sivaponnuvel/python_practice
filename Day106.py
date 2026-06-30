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


# 🔹 Question 2 – Display Students Sorted by Age and Name
# Using table:
# students
# Write a Python program to:
# 👉 Display all students.
# Use the following query:
# SELECT *
# FROM students
# ORDER BY age ASC, name ASC;
# This means:
# First sort by age (smallest to largest).
# If two students have the same age, sort them alphabetically by name.
# Example Table
# ID	Name	Age
# 1	Siva	23
# 2	Ram	21
# 3	Arun	23
# 4	Vijay	21
# Example Output
# --- Students Sorted ---
# ID: 2
# Name: Ram
# Age: 21
# ID: 4
# Name: Vijay
# Age: 21
# ID: 3
# Name: Arun
# Age: 23
# ID: 1
# Name: Siva
# Age: 23
# If there are no records:
# No Students Found ❌
# ⚠️ Conditions
# ✅ Use ORDER BY age ASC, name ASC
# ✅ Use fetchall()
# ✅ Display using a loop
# ❌ Don't sort in Python
# ❌ Don't use sorted()

cursor.execute("select * from students order by age asc, name asc")
detail = cursor.fetchall()

if detail:
    print("--- Students Sorted ---")
    for i in detail:
        print(f"ID: {i[0]}")
        print(f"Name: {i[1]}")
        print(f"Age: {i[2]}")
else:
    print("No Students Found ❌")

cursor.close()
con.close()