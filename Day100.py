# 🔹 Question 1 – Count Students Above a Given Age
# Using table:
# students
# Write a Python program to:
# 👉 Take an age from user
# Example:
# Enter Age: 21
# 👉 Find how many students have age greater than the given age.
# Query:
# SELECT COUNT(*)
# FROM students
# WHERE age > %s
# 👉 Display:
# Students Above Age 21: 4
# Example Output
# Enter Age: 22
# Students Above Age 22: 2
# ⚠️ Conditions
# ✅ Use COUNT(*)
# ✅ Use WHERE
# ✅ Use fetchone()
# ✅ Use parameterized query
# ❌ Don't count using Python loops
# ❌ Let MySQL calculate the count

import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "student_db",
    password = "siva2025"
)
cursor = con.cursor()

age = int(input("Enter Age: "))
cursor.execute("select count(*) from students where age > %s",(age,))

detail = cursor.fetchone()

print(f"Students Above Age {age}: {detail[0]}")


