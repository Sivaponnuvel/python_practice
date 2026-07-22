# 🔹 Question 1 – Display Unique Ages
# Write a Python program to display all unique ages from the students table in ascending order.
# Table: students
# Column Name	Type
# id	INT
# name	VARCHAR
# age	INT
# Program Flow
# Retrieve all unique ages from the table.
# Display them in ascending order.
# Example
# Suppose the table contains:
# id	name	age
# 1	Siva	21
# 2	Rahul	22
# 3	Priya	21
# 4	Vijay	20
# Output
# 20
# 21
# 22
# ⚠️ Conditions
# ✅ Use DISTINCT
# ✅ Use ORDER BY
# ✅ Use ASC
# ✅ Use fetchall()
# ✅ Display using a loop
# ❌ Don't remove duplicates in Python
# ❌ Don't use more than one SQL query

import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "student_db",
    password = "siva2025"
)
cursor = con.cursor()

cursor.execute("select distinct(age) from students order by age asc")
detail = cursor.fetchall()

for i in detail:
    print(i[0])


