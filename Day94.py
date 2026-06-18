# 🔹 Question 1 – Find Youngest and Oldest Student
# Using table:
# students
# Write a Python program to:
# 👉 Find the youngest student using MySQL
# SELECT * FROM students
# ORDER BY age ASC
# LIMIT 1
# 👉 Find the oldest student using MySQL
# SELECT * FROM students
# ORDER BY age DESC
# LIMIT 1
# 👉 Display:
# Youngest Student:
# ID: 2
# Name: Ram
# Age: 20
# Oldest Student:
# ID: 5
# Name: Vijay
# Age: 25
# ⚠️ Conditions
# ✅ Use ORDER BY
# ✅ Use LIMIT 1
# ✅ Use fetchone()
# ❌ Don't find youngest/oldest using Python loops
# ❌ Don't use MIN() or MAX()
# Example Output
# Youngest Student:
# ID: 2
# Name: Ram
# Age: 20
# Oldest Student:
# ID: 5
# Name: Vijay
# Age: 25

import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "student_db",
    password = "siva2025"
)

cursor = con.cursor()

cursor.execute("select * from students order by age asc limit 1")
youngest = cursor.fetchone()
print("Youngest Student:")
print(f"ID: {youngest[0]}")
print(f"Name: {youngest[1]}")
print(f"Age: {youngest[2]}")

cursor.execute("select * from students order by age desc limit 1")
oldest = cursor.fetchone()
print("Oldest Student:")
print(f"ID: {oldest[0]}")
print(f"Name: {oldest[1]}")
print(f"Age: {oldest[2]}")


# 🔹 Question 2 – Display Top N Students (LIMIT)
# Using table:
# students
# Write a Python program to:
# 👉 Take a number from user
# Enter Limit: 3
# 👉 Fetch only that many students
# Query:
# SELECT * FROM students
# LIMIT %s
# 👉 Display records
# Example:
# Top 3 Students:
# ID: 1
# Name: Siva
# Age: 23
# ID: 2
# Name: Ram
# Age: 21
# ID: 3
# Name: Arun
# Age: 22
# 👉 If table is empty:
# No Students Found ❌
# ⚠️ Conditions
# ✅ Use LIMIT
# ✅ Use parameterized query
# ✅ Use fetchall()
# ✅ Display using loop
# ❌ Don't fetch all records and slice in Python
# ❌ Let MySQL handle the limit
# Example Output
# Enter Limit: 2
# Top 2 Students:
# ID: 1
# Name: Siva
# Age: 23
# ID: 2
# Name: Ram
# Age: 21

limit =  int(input("Enter Limit: "))
cursor.execute("select * from students limit %s",(limit,))
details = cursor.fetchall()

if details:
    print(f"Top {limit} Students:")
    for i in details:
        print(f"ID: {i[0]}")
        print(f"Name: {i[1]}")
        print(f"Age: {i[2]}")
else:
    print("No Students Found ❌")

cursor.close()
con.close()