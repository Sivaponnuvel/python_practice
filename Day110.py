# 🔹 Question 1 – Display Students Whose Name Length is Greater Than a Given Number
# Using table:
# students
# Write a Python program to:
# 👉 Take a number from the user.
# Example:
# Enter Minimum Name Length: 4
# Use the query:
# SELECT *
# FROM students
# WHERE LENGTH(name) > %s;
# Display all matching students.
# Example Table
# ID	Name	Age
# 1	Ram	21
# 2	Siva	23
# 3	Karthik	24
# 4	Arun	22
# Example Output
# Enter Minimum Name Length: 4
# Matching Students:
# ID: 3
# Name: Karthik
# Age: 24
# If no records are found:
# No Matching Students ❌
# ⚠️ Conditions
# ✅ Use LENGTH()
# ✅ Use WHERE
# ✅ Use parameterized query
# ✅ Use fetchall()
# ❌ Don't calculate string length in Python
# ❌ Don't filter records using Python loops

import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "student_db",
    password = "siva2025"
)
cursor = con.cursor()

length = int(input("Enter Minimum Name Length: "))
cursor.execute("select * from students where length(name) > %s", (length,))
details = cursor.fetchall()

if details:
    print("Matching Students:")
    for i in details:
        print(f"ID: {i[0]}")
        print(f"Name: {i[1]}")
        print(f"Age: {i[2]}")
else:
    print("No Matching Students ❌")


