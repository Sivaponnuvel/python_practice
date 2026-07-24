# 🔹 Question 1 – Display the Number of Students in Each Age Group
# Write a Python program to display how many students belong to each age.
# Table: students
# Column Name	Type
# id	INT
# name	VARCHAR
# age	INT
# Program Flow
# Count the number of students for each age.
# Display the age and the total number of students.
# Example
# Suppose the table contains:
# id	name	age
# 1	Siva	21
# 2	Rahul	22
# 3	Priya	21
# 4	Vijay	20
# 5	Arun	22
# Output
# Age : 20  Total Students : 1
# Age : 21  Total Students : 2
# Age : 22  Total Students : 2
# ⚠️ Conditions
# ✅ Use GROUP BY
# ✅ Use COUNT(*)
# ✅ Use fetchall()
# ✅ Display using a loop
# ❌ Don't count records in Python
# ❌ Don't use more than one SQL query

import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "student_db",
    password = "siva2025"
)
cursor = con.cursor()

cursor.execute("select count(*), age from students group by age")
details = cursor.fetchall()

for i in details:
    print(f"Age : {i[1]}  Total Students : {i[0]}")


# 🔹 Question 2 – Display Age Groups Having More Than One Student
# Write a Python program to display only those age groups that have more than one student.
# Table: students
# Column Name	Type
# id	INT
# name	VARCHAR
# age	INT
# Example
# Suppose the table contains:
# id	name	age
# 1	Siva	21
# 2	Rahul	22
# 3	Priya	21
# 4	Vijay	20
# 5	Arun	22
# Output
# Age : 21  Total Students : 2
# Age : 22  Total Students : 2
# ⚠️ Conditions
# ✅ Use GROUP BY
# ✅ Use HAVING
# ✅ Use COUNT(*)
# ✅ Use fetchall()
# ✅ Display using a loop
# ❌ Don't filter the result in Python
# ❌ Don't use WHERE COUNT(*)
# ❌ Don't use more than one SQL query

cursor.execute("select count(*), age from students group by age having count(*) > 1")
detail = cursor.fetchall()

for i in detail:
    print(f"Age : {i[1]}  Total Students : {i[0]}")

cursor.close()
con.close()
