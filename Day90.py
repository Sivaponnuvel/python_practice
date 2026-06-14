# 🔹 Question 1 – Search Students Using OR Condition
# Using table:
# students
# Write a Python program to:
# 👉 Take two ages from user
# Enter Age 1: 20
# Enter Age 2: 23
# 👉 Search using:
# SELECT * FROM students
# WHERE age = %s OR age = %s
# 👉 Display all matching students
# Example Output:
# Matching Students:
# ID: 1
# Name: Siva
# Age: 23
# ID: 2
# Name: Ram
# Age: 20
# 👉 If no records found:
# No Matching Students ❌
# ⚠️ Conditions
# ✅ Use OR
# ✅ Use fetchall()
# ✅ Use loop
# ✅ Use parameterized query
# ❌ Don't filter in Python

import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "student_db",
    password = "siva2025"
)

cursor = con.cursor()

age1 = int(input("Enter Age 1: "))
age2 = int(input("Enter Age 2: "))
cursor.execute("select * from students where age = %s or age = %s",(age1, age2))
details = cursor.fetchall()

if details:
    print("Matching Students:")
    for i in details:
        print(f"ID: {i[0]}")    
        print(f"Name: {i[1]}")    
        print(f"Age: {i[2]}")
        print()
else:
    print("No Matching Students ❌")


