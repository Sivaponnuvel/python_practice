# 🔹 Question 1 – Delete Student Record
# Using:
# student_db
# students
# Write a Python program to:
# 👉 Take Student ID from user
# 👉 Delete the student using:
# DELETE FROM students
# WHERE id = %s
# 👉 If record deleted:
# Student Deleted Successfully ✅
# 👉 Otherwise:
# Student Not Found ❌
# 👉 After deletion display all remaining students.
# Example Output:
# Enter Student ID: 3
# Student Deleted Successfully ✅
# --- Remaining Students ---
# ID: 1
# Name: Siva
# Age: 23
# ID: 2
# Name: Ram
# Age: 21
# ⚠️ Conditions
# ✅ Use rowcount
# ✅ Use commit()
# ✅ Use SELECT * FROM students
# ✅ Close connection properly

import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "student_db",
    password = "siva2025"
)
cursor = con.cursor()

student_id = int(input("Enter Student ID: "))
cursor.execute("delete from students where id = %s", (student_id,))
con.commit()

if cursor.rowcount > 0:
    print("Student Deleted Successfully ✅")
    print("--- Remaining Students ---")
    cursor.execute("select * from students")
    detail = cursor.fetchall()
    for i in detail:
        print(f"ID: {i[0]}")    
        print(f"Name: {i[1]}")    
        print(f"Age: {i[2]}")
else:
    print("Student Not Found ❌")


