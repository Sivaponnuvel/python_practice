# 🔹 Question 1 – Search Students Using NOT LIKE
# Using table:
# students
# Write a Python program to:
# 👉 Take the ending letter of a student's name from the user.
# Example:
# Enter Ending Letter: a
# Use the query:
# SELECT *
# FROM students
# WHERE name NOT LIKE %s;
# Pass the parameter as:
# ("%" + letter,)
# Display all matching students.
# Example Table
# ID	Name	Age
# 1	Siva	23
# 2	Ram	21
# 3	Karthik	24
# 4	Aruna	22
# Example Output
# Enter Ending Letter: a
# Students Found:
# ID: 2
# Name: Ram
# Age: 21
# ID: 3
# Name: Karthik
# Age: 24
# If no records exist:
# No Students Found ❌
# ⚠️ Conditions
# ✅ Use NOT LIKE
# ✅ Use parameterized query
# ✅ Use fetchall()
# ✅ Display using a loop
# ❌ Don't filter names in Python

import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "student_db",
    password = "siva2025"
)
cursor = con.cursor()

letter = input("Enter Ending Letter: ")
cursor.execute("select * from students where name not like %s",("%" + letter,))
details = cursor.fetchall()

if details:
    print("Students Found:")
    for i in details:
        print(f"ID: {i[0]}")
        print(f"Name: {i[1]}")
        print(f"Age: {i[2]}")
else:
    print("No Students Found ❌")


