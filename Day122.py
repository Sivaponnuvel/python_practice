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


# 🔹 Question 2 – Display Student Count and Maximum Age
# Using table:
# students
# Write a Python program to display:
# Total number of students
# Maximum age among students
# Use only one query:
# SELECT COUNT(*), MAX(age)
# FROM students;
# Example Output
# Student Statistics
# ------------------
# Total Students : 12
# Maximum Age    : 27
# If there are no students:
# No Students Found ❌
# ⚠️ Conditions
# ✅ Use COUNT(*)
# ✅ Use MAX(age)
# ✅ Use fetchone()
# ✅ Use only one query
# ❌ Don't execute two separate queries
# ❌ Don't calculate the maximum age in Python

cursor.execute("select count(*), max(age) from students")
details = cursor.fetchone()

if details[0] > 0:
    print("Student Statistics")
    print("------------------")
    print(f"Total Students : {details[0]}")
    print(f"Maximum Age    : {details[1]}")
else:
    print("No Students Found ❌")

cursor.close()
con.close()