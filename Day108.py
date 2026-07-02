# 🔹 Question 1 – Display Students Whose Name Starts With a Given Letter
# Using table:
# students
# Write a Python program to:
# 👉 Take the first letter of a student's name from the user.
# Example:
# Enter Starting Letter: S
# Use the query:
# SELECT *
# FROM students
# WHERE name LIKE %s;
# Pass the parameter as:
# (letter + "%",)
# Display all matching students.
# Example Output
# Enter Starting Letter: S
# Matching Students:
# ID: 1
# Name: Siva
# Age: 23
# ID: 5
# Name: Surya
# Age: 20
# If no students are found:
# No Matching Students ❌
# ⚠️ Conditions
# ✅ Use LIKE
# ✅ Use parameterized query
# ✅ Use fetchall()
# ✅ Display using a loop
# ❌ Don't filter names in Python
# ❌ Don't use startswith()

import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "student_db",
    password = "siva2025"
)
cursor = con.cursor()

letter = input("Enter Starting Letter: ")
cursor.execute("select * from students where name like %s",(letter + "%",))
details = cursor.fetchall()

if details:
    print("Matching Students:")
    for i in details:
        print(f"ID: {i[0]}")
        print(f"Name: {i[1]}")
        print(f"Age: {i[2]}")
else:
    print("No Matching Students ❌")


# 🔹 Question 2 – Display Student Count for Each Name (GROUP BY)
# Using table:
# students
# Write a Python program to display how many students have the same name.
# Use the query:
# SELECT name, COUNT(*)
# FROM students
# GROUP BY name;
# Display the output like:
# --- Student Name Count ---
# Siva  : 2 Student(s)
# Ram   : 3 Student(s)
# Arun  : 1 Student(s)
# If the table is empty:
# No Students Found ❌
# Example Table
# ID	Name	Age
# 1	Siva	23
# 2	Ram	21
# 3	Siva	24
# 4	Arun	22
# 5	Ram	20
# Example Output
# --- Student Name Count ---
# Siva : 2 Student(s)
# Ram  : 2 Student(s)
# Arun : 1 Student(s)
# ⚠️ Conditions
# ✅ Use GROUP BY
# ✅ Use COUNT(*)
# ✅ Use fetchall()
# ✅ Display using a loop
# ❌ Don't count names using a Python dictionary
# ❌ Let MySQL perform the grouping

cursor.execute("select name, count(*) from students group by name")
detail = cursor.fetchall()

if detail:
    print("--- Student Name Count ---")
    for i in detail:
        print(f"{i[0]} : {i[1]} Student(s)")
else:
    print("No Students Found ❌")

cursor.close()
con.close()