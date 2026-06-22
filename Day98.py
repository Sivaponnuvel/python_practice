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


# Question 2 – Search Students Using IN
# Using table students, write a Python program to search students whose age is in a given list.
# Take input
# Enter Age 1: 20
# Enter Age 2: 23
# Enter Age 3: 25
# Query
# SELECT * FROM students WHERE age IN (%s, %s, %s)
# Example Output
# Matching Students:
# ID: 1
# Name: Siva
# Age: 23
# ID: 4
# Name: Vijay
# Age: 25
# If no records found
# No Matching Students ❌
# ⚠️ Conditions
# Use IN
# Use fetchall()
# Use parameterized query with three placeholders
# ❌ Don't filter in Python loops

age_1 = int(input("Enter Age 1: "))
age_2 = int(input("Enter Age 2: "))
age_3 = int(input("Enter Age 3: "))

cursor.execute("select * from students where age in (%s, %s, %s)",(age_1, age_2, age_3))
details = cursor.fetchall()

if details:
    print("Matching Students:")
    for i in details:
        print(f"ID: {i[0]}")
        print(f"Name: {i[1]}")
        print(f"Age: {i[2]}")
else:
    print("No Matching Students ❌")

cursor.close()
con.close()