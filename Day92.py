# 🔹 Question 1 – Find Average Age of Students
# Using table:
# students
# Write a Python program to:
# 👉 Calculate average age using MySQL
# Query:
# SELECT AVG(age) FROM students
# 👉 Display result
# Example Output:
# Average Age: 22.5
# ⚠️ Conditions
# ✅ Use AVG()
# ✅ Use fetchone()
# ✅ Let MySQL calculate average
# ❌ Don't calculate average in Python

import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "student_db",
    password = "siva2025"
)
cursor = con.cursor()

cursor.execute("select avg(age) from students")
details = cursor.fetchone()

print(f"Average Age: {details[0]}")


# 🔹 Question 2 – Display Students Between Age Range
# Using table:
# students
# Write a Python program to:
# 👉 Take:
# Minimum Age
# Maximum Age
# 👉 Search using:
# SELECT * FROM students
# WHERE age BETWEEN %s AND %s
# 👉 Display matching students
# Example:
# Enter Minimum Age: 20
# Enter Maximum Age: 23
# Output:
# Matching Students:
# ID: 1
# Name: Siva
# Age: 20
# ID: 3
# Name: Ram
# Age: 22
# ID: 5
# Name: Arun
# Age: 23
# 👉 If no records found:
# No Matching Students ❌
# ⚠️ Conditions
# ✅ Use BETWEEN
# ✅ Use fetchall()
# ✅ Use parameterized query
# ✅ Filtering should happen in MySQL
# ❌ Don't filter in Python loops


min_age = int(input("Enter Minimum Age: "))
max_age = int(input("Enter Maximum Age: "))
cursor.execute("select * from  students where age between %s and %s",(min_age,max_age))
detail = cursor.fetchall()

if detail:
    print("Matching Students:")
    for i in detail:
        print(f"ID: {i[0]}")
        print(f"Name: {i[1]}")
        print(f"Age: {i[2]}")
else:
    print("No Matching Students ❌")

cursor.close()
con.close()