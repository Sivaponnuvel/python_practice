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


# 🔹 Question 2 – Display the Oldest Student(s)
# Write a Python program to display the details of the student(s) having the maximum age.
# Note: If more than one student has the same maximum age, display all of them.
# Table: students
# Column Name	Type
# id	INT
# name	VARCHAR
# age	INT
# Example
# Output
# 2 Rahul 24
# 5 Vijay 24
# ⚠️ Conditions
# ✅ Use only one SQL query
# ✅ Use MAX(age)
# ✅ Use fetchall()
# ✅ Display using a loop
# ❌ Don't first fetch all records and then find the maximum age in Python
# ❌ Don't use two SQL queries

cursor.execute("select * from students where age = (select max(age) from students)")
detail = cursor.fetchall()

for i in detail:
    print(f"{i[0]} {i[1]} {i[2]}")

cursor.close()
con.close()