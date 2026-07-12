# 🔹 Question 1 – Display Students Older Than a Given Age
# Using table:
# students
# Take age from the user.
# Example:
# Enter Age: 23
# Query:
# SELECT *
# FROM students
# WHERE age > %s;
# Example Output:
# Students Found:
# ID: 8
# Name: Shafeek
# Age: 24
# ID: 11
# Name: Pavin
# Age: 27
# ID: 12
# Name: Guru
# Age: 26
# If no records:
# No Students Found ❌
# Conditions
# ✅ Use WHERE
# ✅ Use parameterized query
# ✅ Use fetchall()
# ✅ Display using loop
# ❌ Don't filter in Python

import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "student_db",
    password = "siva2025"
)
cursor = con.cursor()

age = int(input("Enter Age: "))
cursor.execute("select * from students where age > %s",(age,))
details = cursor.fetchall()

if details:
    print("Students Found:")
    for i in details:
        print(f"ID: {i[0]}")
        print(f"Name: {i[1]}")
        print(f"Age: {i[2]}")
else:
    print("No Students Found ❌")


# 🔹 Question 2 – Display Total Students and Average Age
# Use one query only:
# SELECT COUNT(*), AVG(age)
# FROM students;
# Example Output:
# Student Statistics
# ------------------
# Total Students : 5
# Average Age    : 24.6
# If no records:
# No Students Found ❌
# Conditions
# ✅ Use COUNT(*)
# ✅ Use AVG()
# ✅ Use fetchone()
# ❌ Don't calculate average in Python
# ❌ Don't execute two separate queries

cursor.execute("select count(*), avg(age) from students")
detail = cursor.fetchone()

if detail and detail[0] > 0:
    print("Student Statistics")
    print("------------------")
    print(f"Total Students : {detail[0]}")
    print(f"Average Age    : {detail[1]:.1f}")
else:
    print("No Students Found ❌")

cursor.close()
con.close()