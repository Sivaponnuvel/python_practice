# 🔹 Question 1 – Update Student Name Using REPLACE()
# Using table:
# students
# Write a Python program to:
# 👉 Take:
# Student ID
# New Name
# 👉 Update the student's name using:
# UPDATE students
# SET name = %s
# WHERE id = %s
# 👉 After updating:
# Display the updated record.
# If no record exists:
# Student Not Found ❌
# Example Output
# Enter Student ID: 2
# Enter New Name: Karthik
# Student Updated Successfully ✅
# Updated Record:
# ID: 2
# Name: Karthik
# Age: 21
# ⚠️ Conditions
# ✅ Use UPDATE
# ✅ Use WHERE
# ✅ Use cursor.rowcount
# ✅ Use fetchone()
# ✅ Use commit()
# ❌ Don't update using Python variables only

import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "student_db",
    password = "siva2025"
)
cursor = con.cursor()

id = int(input("Enter Student ID: "))
name = input("Enter New Name: ")
cursor.execute("update students set name = %s where id = %s",(name,id))
con.commit()

if cursor.rowcount > 0:
    cursor.execute("select * from students where id = %s",(id,))
    detail = cursor.fetchone()
    print("Student Updated Successfully ✅")
    print("Updated Record:")
    print(f"ID: {detail[0]}")
    print(f"Name: {detail[1]}")
    print(f"Age: {detail[2]}")
else:
    print("Student Not Found ❌")


