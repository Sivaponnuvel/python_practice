# 🔹 Question 1 – Update a Student's Age
# Write a Python program to update the age of a student using the student's ID.
# Table: students
# Column Name	Type
# id	INT
# name	VARCHAR
# age	INT
# Program Flow
# Take the student ID from the user.
# Take the new age from the user.
# Update the student's age.
# If the update is successful, display:
# Student Age Updated Successfully ✅
# Otherwise, display:
# Student Not Found ❌
# Example
# Input
# Enter Student ID: 2
# Enter New Age: 23
# Output
# Student Age Updated Successfully ✅
# ⚠️ Conditions
# ✅ Take input from the user
# ✅ Use a parameterized query (%s)
# ✅ Use UPDATE
# ✅ Use commit()
# ✅ Check the result using cursor.rowcount
# ❌ Don't use SELECT before UPDATE
# ❌ Don't use more than one SQL query

import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "student_db",
    password = "siva2025"
)
cursor = con.cursor()

student_id = int(input("Enter Student ID: "))
student_age = int(input("Enter New Age: "))

cursor.execute("update students set age = %s where id = %s",(student_age, student_id))
con.commit()

if cursor.rowcount > 0:
    print("Student Age Updated Successfully ✅")
else:
    print("Student Not Found ❌")


# 🔹 Question 2 – Increase Age by 1 for Students Older Than a Given Age
# Write a Python program to increase the age by 1 for all students whose age is greater than the age entered by the user.
# Table: students
# Column Name	Type
# id	INT
# name	VARCHAR
# age	INT
# Program Flow
# Take an age from the user.
# Increase the age of all students whose age is greater than the entered age.
# If records are updated, display:
# Total Students Updated: <count>
# Otherwise, display:
# No Students Updated ❌
# Example
# Input
# Enter Age: 20
# Suppose the table contains:
# id	name	age
# 1	Siva	21
# 2	Rahul	22
# 3	Priya	20
# After execution:
# id	name	age
# 1	Siva	22
# 2	Rahul	23
# 3	Priya	20
# Output
# Total Students Updated: 2
# ⚠️ Conditions
# ✅ Use one UPDATE query
# ✅ Use a parameterized query (%s)
# ✅ Use commit()
# ✅ Use cursor.rowcount
# ❌ Don't update records in Python
# ❌ Don't use SELECT before UPDATE
# ❌ Don't use more than one SQL query

age = int(input("Enter Age: "))
cursor.execute("update students set age = age + 1 where age > %s",(age,))
con.commit()

if cursor.rowcount > 0:
    print(f"Total Students Updated: {cursor.rowcount}")
else:
    print("No Students Updated ❌")

cursor.close()
con.close()