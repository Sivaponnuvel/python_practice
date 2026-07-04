# 🔹 Question 1 – Display Students Whose Name Length is Greater Than a Given Number
# Using table:
# students
# Write a Python program to:
# 👉 Take a number from the user.
# Example:
# Enter Minimum Name Length: 4
# Use the query:
# SELECT *
# FROM students
# WHERE LENGTH(name) > %s;
# Display all matching students.
# Example Table
# ID	Name	Age
# 1	Ram	21
# 2	Siva	23
# 3	Karthik	24
# 4	Arun	22
# Example Output
# Enter Minimum Name Length: 4
# Matching Students:
# ID: 3
# Name: Karthik
# Age: 24
# If no records are found:
# No Matching Students ❌
# ⚠️ Conditions
# ✅ Use LENGTH()
# ✅ Use WHERE
# ✅ Use parameterized query
# ✅ Use fetchall()
# ❌ Don't calculate string length in Python
# ❌ Don't filter records using Python loops

import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "student_db",
    password = "siva2025"
)
cursor = con.cursor()

length = int(input("Enter Minimum Name Length: "))
cursor.execute("select * from students where length(name) > %s", (length,))
details = cursor.fetchall()

if details:
    print("Matching Students:")
    for i in details:
        print(f"ID: {i[0]}")
        print(f"Name: {i[1]}")
        print(f"Age: {i[2]}")
else:
    print("No Matching Students ❌")


# 🔹 Question 2 – Display Students Whose Age is Equal to the Highest Age
# Using table:
# students
# Write a Python program to display all students whose age is equal to the highest age in the table.
# Use only one query:
# SELECT *
# FROM students
# WHERE age = (
#     SELECT MAX(age)
#     FROM students
# );
# Example Table
# ID	Name	Age
# 1	Siva	23
# 2	Ram	25
# 3	Arun	25
# 4	Vijay	21
# Example Output
# Oldest Student(s):
# ID: 2
# Name: Ram
# Age: 25
# ID: 3
# Name: Arun
# Age: 25
# If no records exist:
# No Students Found ❌
# ⚠️ Conditions
# ✅ Use a subquery
# ✅ Use MAX()
# ✅ Use fetchall()
# ✅ Display using a loop
# ❌ Don't execute two separate queries
# ❌ Don't calculate the maximum age in Python

cursor.execute("select * from students where age = (select max(age) from students)")
detail = cursor.fetchall()

if detail:
    print("Oldest Student(s):")
    for i in detail:
        print(f"ID: {i[0]}")
        print(f"Name: {i[1]}")
        print(f"Age: {i[2]}")
else:
    print("No Students Found ❌")

cursor.close()
con.close()