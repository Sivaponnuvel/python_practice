# 🔹 Question 1 – Find Total Age of All Students
# Using table:
# students
# Write a Python program to:
# 👉 Calculate total age of all students using MySQL
# Query:
# SELECT SUM(age) FROM students
# 👉 Display result
# Example Output
# Total Age: 91
# Conditions
# ✅ Use SUM()
# ✅ Use fetchone()
# ✅ Let MySQL calculate the total
# ❌ Don't use Python loops to add ages
# ❌ Don't fetch all records and calculate manually
# Example
# If table contains:
# ID	Name	Age
# 1	Siva	23
# 2	Ram	21
# 3	Arun	22
# Output:
# Total Age: 66

import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "student_db",
    password = "siva2025"
)
cursor = con.cursor()

cursor.execute("select sum(age) from students")
detail = cursor.fetchone()

print(f"Total Age: {detail[0]}")


