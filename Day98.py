# Question 1 – Find Minimum and Maximum Age
# Using table students, write a Python program to find the minimum and maximum age using MySQL.
# Queries
# SELECT MIN(age) FROM students;
# SELECT MAX(age) FROM students;
# Output: 
# Minimum Age: 20
# Maximum Age: 25
# ⚠️ Conditions
# Use MIN() and MAX()
# Use fetchone()
# Let MySQL calculate the values
# ❌ Don't use Python loops to find min/max

import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "student_db",
    password = "siva2025"
)
cursor =  con.cursor()

cursor.execute("select min(age) from students")
min_age = cursor.fetchone()
cursor.execute("select max(age) from students")
max_age = cursor.fetchone()

print(f"Minimum Age: {min_age[0]}")
print(f"Maximum Age: {max_age[0]}")


