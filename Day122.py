# 🔹 Question 1 – Display Students Whose Name Contains a Given Word
# Using table:
# students
# Write a Python program to:
# 👉 Take a word from the user.
# Example:
# Enter Text: vi
# Use the query:
# SELECT *
# FROM students
# WHERE name LIKE %s;
# Pass the parameter as:
# ("%" + text + "%",)
# Display all matching students.
# Example Output
# Enter Text: vi
# Matching Students:
# ID: 2
# Name: Vijay
# Age: 23
# ID: 7
# Name: Sivakumar
# Age: 25
# If no matching students:
# No Matching Students ❌
# ⚠️ Conditions
# ✅ Use LIKE
# ✅ Use %text%
# ✅ Use parameterized query
# ✅ Use fetchall()
# ✅ Display using a loop
# ❌ Don't filter in Python

import mysql.connector

con = mysql.connector.connect(
    host  = "localhost",
    user = "root",
    database = "student_db",
    password = "siva2025"
)
cursor = con.cursor()

text = input("Enter Text: ")
cursor.execute("select * from students where name like %s",("%" + text + "%",))
detail  = cursor.fetchall()

if detail:
    print("Matching Students:")
    for i in detail:
        print(f"ID: {i[0]}")
        print(f"Name: {i[1]}")
        print(f"Age: {i[2]}")
else:
    print("No Matching Students ❌")


