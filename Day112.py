# 🔹 Question 1 – Search Students Using NOT LIKE
# Using table:
# students
# Write a Python program to:
# 👉 Take the ending letter of a student's name from the user.
# Example:
# Enter Ending Letter: a
# Use the query:
# SELECT *
# FROM students
# WHERE name NOT LIKE %s;
# Pass the parameter as:
# ("%" + letter,)
# Display all matching students.
# Example Table
# ID	Name	Age
# 1	Siva	23
# 2	Ram	21
# 3	Karthik	24
# 4	Aruna	22
# Example Output
# Enter Ending Letter: a
# Students Found:
# ID: 2
# Name: Ram
# Age: 21
# ID: 3
# Name: Karthik
# Age: 24
# If no records exist:
# No Students Found ❌
# ⚠️ Conditions
# ✅ Use NOT LIKE
# ✅ Use parameterized query
# ✅ Use fetchall()
# ✅ Display using a loop
# ❌ Don't filter names in Python

import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "student_db",
    password = "siva2025"
)
cursor = con.cursor()

letter = input("Enter Ending Letter: ")
cursor.execute("select * from students where name not like %s",("%" + letter,))
details = cursor.fetchall()

if details:
    print("Students Found:")
    for i in details:
        print(f"ID: {i[0]}")
        print(f"Name: {i[1]}")
        print(f"Age: {i[2]}")
else:
    print("No Students Found ❌")


# 🔹 Question 2 – Display Student Count Greater Than a Given Age (GROUP BY + HAVING)
# Using table:
# students
# Write a Python program to:
# 👉 Take an age from the user.
# Example:
# Enter Age: 21
# Use the query:
# SELECT age, COUNT(*)
# FROM students
# GROUP BY age
# HAVING age > %s;
# Display all matching groups.
# Example Table
# ID	Name	Age
# 1	Siva	20
# 2	Ram	21
# 3	Arun	22
# 4	Vijay	22
# 5	Karthik	24
# Example Output
# Enter Age: 21
# Age Groups:
# Age 22 : 2 Student(s)
# Age 24 : 1 Student(s)
# If no matching age groups exist:
# No Matching Age Groups ❌
# ⚠️ Conditions
# ✅ Use GROUP BY
# ✅ Use HAVING
# ✅ Use parameterized query
# ✅ Use fetchall()
# ✅ Display using a loop
# ❌ Don't filter age groups in Python
# ❌ Don't execute multiple queries

age = input("Enter Age: ")
cursor.execute("select age, count(*) from students group by age having age > %s",(age,))
detail = cursor.fetchall()

if detail:
    print("Age Groups:")
    for i in detail:
        print(f"Age {i[0]} : {i[1]} Student(s)")
else:
    print("No Matching Age Groups ❌")

cursor.close()
con.close()