# 🔹 Question 1 – Delete a Student by ID
# Using table:
# students
# Write a Python program to:
# 👉 Take a Student ID from the user.
# Example:
# Enter Student ID: 3
# Use the query:
# DELETE FROM students
# WHERE id = %s;
# After deleting:
# If the student existed:
# Student Deleted Successfully ✅
# If no student exists:
# Student Not Found ❌
# ⚠️ Conditions
# ✅ Use DELETE
# ✅ Use WHERE
# ✅ Use parameterized query
# ✅ Use cursor.rowcount
# ✅ Use commit()
# ❌ Don't delete records using Python loops.
# ❌ Don't delete all records.

import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "student_db",
    password = "siva2025"
)
cursor = con.cursor()

student_id = int(input("Enter Student ID: "))
cursor.execute("delete from students where id = %s",(student_id,))
con.commit()

if cursor.rowcount > 0:
    print("Student Deleted Successfully ✅")
else:
    print("Student Not Found ❌")


