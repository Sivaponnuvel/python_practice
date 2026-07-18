# 🔹 Question 1 – Display Students Older Than a Given Age
# Write a Python program to display all students whose age is greater than the age entered by the user.
# Table: students
# Column Name	Type
# id	INT
# name	VARCHAR
# age	INT
# Program Flow
# Take an age from the user.
# Display all students whose age is greater than the entered age.
# Example
# Input
# Enter Age: 20
# Output
# 2 Rahul 21
# 4 Priya 23
# ⚠️ Conditions
# ✅ Take input from the user
# ✅ Use a parameterized query (%s)
# ✅ Use fetchall()
# ✅ Display the records using a loop
# ❌ Don't filter records in Python
# ❌ Don't use string formatting inside the SQL query

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
    for i in details:
        print(f"{i[0]} {i[1]} {i[2]}")
else:
    print("No Students Found ❌")


# 🔹 Question 2 – Count Students Between Two Ages
# Write a Python program to count how many students have an age between two values (inclusive).
# Table: students
# Column Name	Type
# id	INT
# name	VARCHAR
# age	INT
# Program Flow
# Take the minimum age from the user.
# Take the maximum age from the user.
# Display the total number of students whose age is between those two values (including both values).
# Example
# Input
# Enter Minimum Age: 18
# Enter Maximum Age: 22
# Output
# Total Students: 5
# ⚠️ Conditions
# ✅ Take both values from the user
# ✅ Use one SQL query
# ✅ Use COUNT(*)
# ✅ Use a parameterized query (%s)
# ✅ Use fetchone()
# ❌ Don't count records in Python
# ❌ Don't use more than one SQL query

min_age = int(input("Enter Minimum Age: "))
max_age = int(input("Enter Maximum Age: "))
cursor.execute("select count(*) from students where age between %s and %s",(min_age, max_age))
detail = cursor.fetchone()

print(f"Total Students: {detail[0]}")

cursor.close()
con.close()