# 🔹 Question 1 – Display Students Younger Than a Given Age
# Using table:
# students
# Write a Python program to:
# 👉 Take an age from the user.
# Example:
# Enter Age: 25
# Use the query:
# SELECT *
# FROM students
# WHERE age < %s;
# Example Output:
# Students Found:
# ID: 6
# Name: Siva
# Age: 23
# ID: 10
# Name: Kishor
# Age: 23
# If no records exist:
# No Students Found ❌
# ⚠️ Conditions
# ✅ Use WHERE
# ✅ Use a parameterized query
# ✅ Use fetchall()
# ✅ Display using a loop
# ❌ Don't filter records in Python

import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "student_db",
    password = "siva2025"
)
cursor = con.cursor()

age = int(input("Enter Age: "))
cursor.execute("select * from students where age < %s",(age,))
detail = cursor.fetchall()

if detail:
    print("Students Found:")
    for i in detail:
        print(f"ID: {i[0]}")
        print(f"Name: {i[1]}")
        print(f"Age: {i[2]}")
else:
    print("No Students Found ❌")


# 🔹 Question 2 – Display Youngest Student(s)
# Using table:
# students
# Write a Python program to display all students whose age is equal to the minimum age in the table.
# Use only one query:
# SELECT *
# FROM students
# WHERE age = (
#     SELECT MIN(age)
#     FROM students
# );
# Example Output:
# Youngest Student(s):
# ID: 6
# Name: Siva
# Age: 20
# ID: 9
# Name: Ram
# Age: 20
# If no records exist:
# No Students Found ❌
# ⚠️ Conditions
# ✅ Use a subquery
# ✅ Use MIN()
# ✅ Use fetchall()
# ✅ Display using a loop
# ❌ Don't execute two separate queries
# ❌ Don't calculate the minimum age in Python

cursor.execute("select * from students where age = (select min(age) from students)")
details = cursor.fetchall()

if details:
    print("Youngest Student(s):")
    for i in details:
        print(f"ID: {i[0]}")
        print(f"Name: {i[1]}")
        print(f"Age: {i[2]}")
else:
    print("No Students Found ❌")

cursor.close()
con.close()