# 🔹 Question 1 – Find Students Older Than Average Age
# Using table:
# students
# Write a Python program to:
# 👉 Find all students whose age is greater than the average age of all students.
# Query
# SELECT *
# FROM students
# WHERE age > (
#     SELECT AVG(age)
#     FROM students
# )
# Example
# If ages are:
# 20
# 22
# 24
# 26
# Average:
# 23
# Output:
# Students Older Than Average:
# ID: 3
# Name: Arun
# Age: 24
# ID: 4
# Name: Vijay
# Age: 26
# If no records
# No Students Found ❌
# ⚠️ Conditions
# ✅ Use subquery
# ✅ Use AVG()
# ✅ Use fetchall()
# ✅ Display using loop
# ❌ Don't calculate average in Python
# ❌ Don't run two separate queries

import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "student_db",
    password = "siva2025"
)
cursor = con.cursor()

cursor.execute("select * from students where age > (select avg(age) from students)")
detail = cursor.fetchall()

if detail:
    print("Students Older Than Average:")
    for i in detail:
        print(f"ID: {i[0]}")
        print(f"Name: {i[1]}")
        print(f"Age: {i[2]}")
else:
    print("No Students Found ❌")


