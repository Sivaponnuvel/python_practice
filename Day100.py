# 🔹 Question 1 – Count Students Above a Given Age
# Using table:
# students
# Write a Python program to:
# 👉 Take an age from user
# Example:
# Enter Age: 21
# 👉 Find how many students have age greater than the given age.
# Query:
# SELECT COUNT(*)
# FROM students
# WHERE age > %s
# 👉 Display:
# Students Above Age 21: 4
# Example Output
# Enter Age: 22
# Students Above Age 22: 2
# ⚠️ Conditions
# ✅ Use COUNT(*)
# ✅ Use WHERE
# ✅ Use fetchone()
# ✅ Use parameterized query
# ❌ Don't count using Python loops
# ❌ Let MySQL calculate the count

import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "student_db",
    password = "siva2025"
)
cursor = con.cursor()

age = int(input("Enter Age: "))
cursor.execute("select count(*) from students where age > %s",(age,))

detail = cursor.fetchone()

print(f"Students Above Age {age}: {detail[0]}")


# 🔹 Question 2 – Group Students by Age
# Using table:
# students
# Write a Python program to:
# 👉 Display how many students belong to each age.
# Query:
# SELECT age, COUNT(*)
# FROM students
# GROUP BY age
# Example
# If table contains:
# Name	Age
# Siva	23
# Ram	21
# Arun	23
# Vijay	21
# Karthik	25
# Output:
# Age Wise Student Count:
# Age 21 : 2 Student(s)
# Age 23 : 2 Student(s)
# Age 25 : 1 Student(s)
# ⚠️ Conditions
# ✅ Use GROUP BY
# ✅ Use COUNT(*)
# ✅ Use fetchall()
# ✅ Display using loop
# ❌ Don't group records in Python dictionary
# ❌ Let MySQL perform grouping
# Example Output
# Enter Age: 22
# Students Above Age 22: 2
# Age Wise Student Count:
# Age 21 : 2 Student(s)
# Age 23 : 2 Student(s)
# Age 25 : 1 Student(s)

cursor.execute("select age,count(*) from students group by age")
details = cursor.fetchall()

for i in details:
    print(f"Age {i[0]} : {i[1]} Student(s)")

cursor.close()
con.close()