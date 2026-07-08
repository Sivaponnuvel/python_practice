# 🔹 Question 1 – Increase Student Age by 1 Year
# Using table:
# students
# Write a Python program to:
# 👉 Take a Student ID from the user.
# Example:
# Enter Student ID: 3
# Use the query:
# UPDATE students
# SET age = age + 1
# WHERE id = %s;
# After updating:
# Retrieve and display the updated student record.
# If no student exists:
# Student Not Found ❌
# Example Output
# Enter Student ID: 3
# Student Age Updated Successfully ✅
# Updated Record:
# ID: 3
# Name: Arun
# Age: 23
# ⚠️ Conditions
# ✅ Use UPDATE
# ✅ Increase age using age = age + 1
# ✅ Use WHERE
# ✅ Use cursor.rowcount
# ✅ Use commit()
# ✅ Use fetchone()
# ❌ Don't calculate the new age in Python.
# ❌ Don't ask the user for the new age.

import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "student_db",
    password = "siva2025"
)
cursor = con.cursor()

student_id = int(input("Enter Student ID: "))
cursor.execute("update students set age = age + 1 where id = %s",(student_id,))
con.commit()

if cursor.rowcount > 0:
    cursor.execute("select * from students where id = %s",(student_id,))
    details = cursor.fetchone()    
    print("Student Age Updated Successfully ✅")
    print("Updated Record:")
    print(f"ID: {details[0]}")
    print(f"Name: {details[1]}")
    print(f"Age: {details[2]}")
else:
    print("Student Not Found ❌")


