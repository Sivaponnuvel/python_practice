# 🔹 Question 1 – Search Students using Age and Name (AND)
# Using table:
# students
# Write a Python program to:
# 👉 Take:
# Name
# Age
# 👉 Search using:
# SELECT * FROM students
# WHERE name = %s AND age = %s
# 👉 If record found:
# Student Found ✅
# ID: 1
# Name: Siva
# Age: 23
# 👉 Otherwise:
# No Matching Student ❌
# Example Output
# Enter Name: Siva
# Enter Age: 23
# Student Found ✅
# ID: 1
# Name: Siva
# Age: 23
# ⚠️ Conditions
# ✅ Use AND
# ✅ Use fetchall()
# ✅ Use loop to display records
# ✅ Use parameterized query

import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "siva2025",
    database = "student_db"
)

cursor = con.cursor()

name = input("Enter Name: ")
age = int(input("Enter Age: "))
cursor.execute("select * from students where name = %s AND age = %s",(name, age))
details = cursor.fetchall()

if details:
    print("Student Found ✅")
    for i in details:
        print(f"ID: {i[0]}")
        print(f"Name: {i[1]}")
        print(f"Age: {i[2]}")
else:
    print("No Matching Student ❌")


# 🔹 Question 2 – Display Students Sorted by Age
# Using table:
# students
# Write a Python program to:
# 👉 Fetch all students
# 👉 Sort by age in ascending order using MySQL
# SELECT * FROM students
# ORDER BY age ASC
# 👉 Display records
# Example Output:
# --- Students Sorted By Age ---
# ID: 2
# Name: Ram
# Age: 20
# ID: 3
# Name: Arun
# Age: 21
# ID: 1
# Name: Siva
# Age: 23
# After completing ASC:
# Try:
# ORDER BY age DESC
# to see highest age first.
# ⚠️ Conditions
# ✅ Use ORDER BY
# ✅ Use fetchall()
# ✅ Sorting should happen in MySQL
# ❌ Don't sort using Python

cursor.execute("select * from students order by age asc")
detail = cursor.fetchall()
print("--- Students Sorted By Age ---")
for i in detail:
    print(f"ID: {i[0]}")
    print(f"Name: {i[1]}")
    print(f"Age: {i[2]}")

cursor.execute("select * from students order by age desc")
detail1 = cursor.fetchall()
print("--- Students Sorted By Age (Descending) ---") 
for i in detail1:
    print(f"ID: {i[0]}")
    print(f"Name: {i[1]}")
    print(f"Age: {i[2]}")

cursor.close()
con.close()