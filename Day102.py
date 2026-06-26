# 🔹 Question 1 – Find Students Older Than Average Age
# Using table:
# students
# Write a Python program to:
# 👉 Find all students whose age is greater than the average age of all students.
# Query
# SELECT *
# FROM students
# WHERE age > (
#     SELECT AVG(age)
#     FROM students
# )
# Example
# If ages are:
# 20
# 22
# 24
# 26
# Average:
# 23
# Output:
# Students Older Than Average:
# ID: 3
# Name: Arun
# Age: 24
# ID: 4
# Name: Vijay
# Age: 26
# If no records
# No Students Found ❌
# ⚠️ Conditions
# ✅ Use subquery
# ✅ Use AVG()
# ✅ Use fetchall()
# ✅ Display using loop
# ❌ Don't calculate average in Python
# ❌ Don't run two separate queries

import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "student_db",
    password = "siva2025"
)
cursor = con.cursor()

cursor.execute("select * from students where age > (select avg(age) from students)")
detail = cursor.fetchall()

if detail:
    print("Students Older Than Average:")
    for i in detail:
        print(f"ID: {i[0]}")
        print(f"Name: {i[1]}")
        print(f"Age: {i[2]}")
else:
    print("No Students Found ❌")


# 🔹 Question 2 – Count Students in Each Age Group Having More Than One Student
# Using table:
# students
# Write a Python program to:
# 👉 Display only ages that have more than one student.
# Query
# SELECT age, COUNT(*)
# FROM students
# GROUP BY age
# HAVING COUNT(*) > 1
# Example
# Table:
# Name	Age
# Siva	23
# Ram	21
# Arun	23
# Vijay	21
# Karthik	25
# Output:
# Age Groups With More Than One Student:
# Age 21 : 2 Student(s)
# Age 23 : 2 Student(s)
# Age 25 should not appear because only one student belongs to that age.
# If no matching groups
# No Matching Age Groups ❌
# ⚠️ Conditions
# ✅ Use GROUP BY
# ✅ Use HAVING
# ✅ Use COUNT(*)
# ✅ Use fetchall()
# ❌ Don't filter groups using Python
# ❌ Let MySQL perform the grouping and filtering

cursor.execute("select age, count(*) from students group by age having count(*) > 1")
details = cursor.fetchall()

if details:
    print("Age Groups With More Than One Student:") 
    for i in details:
        print(f"Age {i[0]} : {i[1]} Student(s)")
else:
    print("No Matching Age Groups ❌")

cursor.close()
con.close()