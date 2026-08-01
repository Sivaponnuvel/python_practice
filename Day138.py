# 🔹 Question 1 – Display Students Sorted by Age and Name
# Write a Python program to display all students sorted by age in ascending order. If two students have the same age, sort them by name in ascending order.
# Table: students
# Column Name	Type
# id	INT
# name	VARCHAR
# age	INT
# Program Flow
# Retrieve all student records.
# Sort by:
# age (Ascending)
# name (Ascending)
# Display all records.
# Example
# Suppose the table contains:
# id	name	age
# 1	Siva	21
# 2	Rahul	20
# 3	Arun	21
# 4	Vijay	20
# Output
# 2 Rahul 20
# 4 Vijay 20
# 3 Arun 21
# 1 Siva 21
# ⚠️ Conditions
# ✅ Use one SQL query
# ✅ Use ORDER BY
# ✅ Sort by two columns
# ✅ Use ASC
# ✅ Use fetchall()
# ✅ Display using a loop
# ❌ Don't sort in Python
# ❌ Don't use more than one SQL query

import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "student_db",
    password = "siva2025"
)
cursor = con.cursor()

cursor.execute("select * from students order by age asc, name asc")
details = cursor.fetchall()

for i in details:
    print(f"{i[0]} {i[1]} {i[2]}")


