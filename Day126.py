# 🔹 Question 1 – Display Students in Alphabetical Order
# Write a Python program to display all students in ascending alphabetical order based on their names.
# Table: students
# Column Name	Type
# id	INT
# name	VARCHAR
# age	INT
# Program Flow
# Retrieve all student records.
# Display them ordered by name in ascending order.
# Example
# Output
# 2 Arun 20
# 4 Karthik 22
# 3 Priya 19
# 1 Siva 21
# ⚠️ Conditions
# ✅ Use ORDER BY
# ✅ Use ASC
# ✅ Use fetchall()
# ✅ Display using a loop
# ❌ Don't sort the records in Python

import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "student_db",
    password = "siva2025"
)
cursor = con.cursor()

cursor.execute("select * from students order by name asc")
details = cursor.fetchall()

for i in details:
    print(f"{i[0]} {i[1]} {i[2]}")


