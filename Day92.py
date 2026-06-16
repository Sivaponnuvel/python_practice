# 🔹 Question 1 – Find Average Age of Students
# Using table:
# students
# Write a Python program to:
# 👉 Calculate average age using MySQL
# Query:
# SELECT AVG(age) FROM students
# 👉 Display result
# Example Output:
# Average Age: 22.5
# ⚠️ Conditions
# ✅ Use AVG()
# ✅ Use fetchone()
# ✅ Let MySQL calculate average
# ❌ Don't calculate average in Python

import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "student_db",
    password = "siva2025"
)
cursor = con.cursor()

cursor.execute("select avg(age) from students")
details = cursor.fetchone()

print(f"Average Age: {details[0]}")


