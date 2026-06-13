# 🔹 Question 1 – Search Students using Age and Name (AND)
# Using table:
# students
# Write a Python program to:
# 👉 Take:
# Name
# Age
# 👉 Search using:
# SELECT * FROM students
# WHERE name = %s AND age = %s
# 👉 If record found:
# Student Found ✅
# ID: 1
# Name: Siva
# Age: 23
# 👉 Otherwise:
# No Matching Student ❌
# Example Output
# Enter Name: Siva
# Enter Age: 23
# Student Found ✅
# ID: 1
# Name: Siva
# Age: 23
# ⚠️ Conditions
# ✅ Use AND
# ✅ Use fetchall()
# ✅ Use loop to display records
# ✅ Use parameterized query

import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "siva2025",
    database = "student_db"
)

cursor = con.cursor()

name = input("Enter Name: ")
age = int(input("Enter Age: "))
cursor.execute("select * from students where name = %s AND age = %s",(name, age))
details = cursor.fetchall()

if details:
    print("Student Found ✅")
    for i in details:
        print(f"ID: {i[0]}")
        print(f"Name: {i[1]}")
        print(f"Age: {i[2]}")
else:
    print("No Matching Student ❌")


