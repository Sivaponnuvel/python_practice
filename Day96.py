# 🔹 Question 1 – Find Total Age of All Students
# Using table:
# students
# Write a Python program to:
# 👉 Calculate total age of all students using MySQL
# Query:
# SELECT SUM(age) FROM students
# 👉 Display result
# Example Output
# Total Age: 91
# Conditions
# ✅ Use SUM()
# ✅ Use fetchone()
# ✅ Let MySQL calculate the total
# ❌ Don't use Python loops to add ages
# ❌ Don't fetch all records and calculate manually
# Example
# If table contains:
# ID	Name	Age
# 1	Siva	23
# 2	Ram	21
# 3	Arun	22
# Output:
# Total Age: 66

import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "student_db",
    password = "siva2025"
)
cursor = con.cursor()

cursor.execute("select sum(age) from students")
detail = cursor.fetchone()

print(f"Total Age: {detail[0]}")


# 🔹 Question 2 – Display Unique Ages (DISTINCT)
# Using table:
# students
# Write a Python program to:
# 👉 Fetch all unique ages from the table
# Query:
# SELECT DISTINCT age FROM students
# 👉 Display ages one by one
# Example
# If table contains:
# Name	Age
# Siva	23
# Ram	21
# Arun	23
# Vijay	21
# Karthik	25
# Output:
# Unique Ages:
# 23
# 21
# 25
# Conditions
# ✅ Use DISTINCT
# ✅ Use fetchall()
# ✅ Use loop to display results
# ❌ Don't remove duplicates using Python
# ❌ Let MySQL handle uniqueness
# Example Output
# Unique Ages:
# 20
# 21
# 23
# 25

cursor.execute("select distinct age from students")
details = cursor.fetchall()

print("Unique Ages:")
for i in details:
    print(i[0])

cursor.close()
con.close()