# Question 1 – Search Student by ID (WHERE)
# Create a program to:
# 👉 Take student ID from user
# 👉 Search using:
# SELECT * FROM students WHERE id = %s
# 👉 If found:
# Student Found ✅
# ID: 1
# Name: Siva
# Age: 23
# 👉 Otherwise:
# Student Not Found ❌
# ⚠️ Use:
# fetchone()
# WHERE

import mysql.connector

con =  mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "student_db",
    password = "siva2025"
)
cursor = con.cursor()

student_id = int(input("Enter ID: "))
cursor.execute("select * from students where id = %s",(student_id,))

details = cursor.fetchone()

if details:
    print("Student Found ✅")
    print(f"ID: {details[0]}")
    print(f"Name: {details[1]}")
    print(f"Age: {details[2]}")
else:
    print("Student Not Found ❌")


# 🔹 Question 2 – Update Student Age
# Using the same table:
# students
# Write a Python program to:
# 👉 Take:
# Student ID
# New Age
# 👉 Update age using:
# UPDATE students
# SET age = %s
# WHERE id = %s
# 👉 After update:
# Print:
# Student Updated Successfully ✅
# 👉 Then display the updated student record.
# Example:
# Enter Student ID: 2
# Enter New Age: 25
# Student Updated Successfully ✅
# Updated Record:
# ID: 2
# Name: Ram
# Age: 25
# ⚠️ Conditions
# ✅ Use:
# cursor.rowcount
# to check whether any record was updated
# ✅ If ID does not exist:
# Student Not Found ❌
# ✅ Use commit()
# ✅ Close connection properly

id = int(input("Enter Student ID: "))
age = int(input("Enter New Age: "))
cursor.execute("update students set age = %s where id = %s",(age, id))
con.commit()

if cursor.rowcount > 0:
    cursor.execute("select * from students where id = %s",(id,))
    detail = cursor.fetchone()
    print("Student Updated Successfully ✅")
    print("Updated Record: ")
    print(f"ID: {detail[0]}")
    print(f"Name: {detail[1]}")
    print(f"Age: {detail[2]}")
else:
    print("Student Not Found ❌")

cursor.close()
con.close()