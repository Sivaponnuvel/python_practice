# 🔹 Question 1 – MySQL: Display Students Above Average Age
# Write a Python program to display all students whose age is greater than the average age of all students.
# Table: students
# Column	Type
# id	INT
# name	VARCHAR
# age	INT
# Example Data
# id   name    age
# 1    Siva    21
# 2    Rahul   25
# 3    Priya   20
# 4    Arun    28
# 5    Vijay   22
# Average age:
# 23.2
# Expected Output
# Students Above Average Age:
# Rahul : 25
# Arun  : 28
# ⚠️ Conditions
# ✅ Use mysql.connector
# ✅ Take database connection
# ✅ Use one SQL query only
# ✅ Use a subquery with AVG()
# ✅ Use fetchall()
# ✅ Display using a loop
# ❌ Don't calculate average in Python
# ❌ Don't use a separate SELECT AVG() query
# ❌ Don't filter the result in Python
# 💡 Hint
# Think about:
# SELECT ...
# FROM students
# WHERE age > (SELECT AVG(age) FROM students)

import mysql.connector

con =  mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "student_db",
    password = "siva2025"
)
cursor = con.cursor()

cursor.execute("select * from students where age > (select avg(age) from students)")
details = cursor.fetchall()

if details:
    print("Students Above Average Age:")
    for i in details:
        print(f"{i[1]} : {i[2]}")


# 🔹 Question 2 – MySQL Interview: Second Highest Age
# Use your existing students table:
# Column	Type
# id	INT
# name	VARCHAR
# age	INT
# Example
# id   name    age
# 1    Siva    21
# 2    Rahul   25
# 3    Priya   20
# 4    Arun    28
# 5    Vijay   25
# Expected Output
# Second Highest Age: 25
# If there is no second highest age:
# Second Highest Age: None
# ⚠️ Conditions
# ✅ Use one SQL query only
# ✅ Use MAX() with a subquery
# ✅ Use fetchone()
# ❌ Don't fetch all ages and calculate in Python
# ❌ Don't use ORDER BY
# ❌ Don't use more than one SQL query
# 💡 Hint
# The SQL logic is:
# SELECT MAX(age)
# FROM students
# WHERE age < (SELECT MAX(age) FROM students)

cursor.execute("select max(age) from students where age < (select max(age) from students)")
detail = cursor.fetchone()

if detail:
    print(f"Second Highest Age: {detail[0]}")
else:
    print("Second Highest Age: None")

cursor.close()
con.close()