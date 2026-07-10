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


# 🔹 Question 2 – Display Students Between Two Ages
# Using table:
# students
# Write a Python program to:
# 👉 Take:
# Enter Minimum Age:
# Enter Maximum Age:
# Use the query:
# SELECT *
# FROM students
# WHERE age BETWEEN %s AND %s
# ORDER BY age ASC;
# Display:
# Students Found:
# ID: 2
# Name: Ram
# Age: 21
# ID: 5
# Name: Arun
# Age: 23
# If no students match:
# No Matching Students ❌
# ⚠️ Conditions
# ✅ Use BETWEEN
# ✅ Use ORDER BY
# ✅ Use parameterized query
# ✅ Use fetchall()
# ✅ Display using a loop
# ❌ Don't filter ages in Python.
# ❌ Don't sort using Python.

min_age = int(input("Enter Minimum Age: "))
max_age = int(input("Enter Maximum Age: "))
cursor.execute("select * from students where age between %s and %s order by age asc",(min_age, max_age))
details = cursor.fetchall()

if details:
    print("Students Found: ")
    for i in details:
        print(f"ID: {i[0]}")
        print(f"Name: {i[1]}")
        print(f"Age: {i[2]}")
else:
    print("No Matching Students ❌")

cursor.close()
con.close()