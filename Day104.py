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


# 🔹 Question 2 – Display Students Within an ID Range
# Using table:
# students
# Write a Python program to:
# 👉 Take:
# Starting ID
# Ending ID
# Search using:
# SELECT *
# FROM students
# WHERE id BETWEEN %s AND %s
# ORDER BY id ASC
# Display all matching students.
# If no records exist:
# No Students Found ❌
# Example Output
# Enter Start ID: 2
# Enter End ID: 5
# Students Found:
# ID: 2
# Name: Ram
# Age: 21
# ID: 3
# Name: Arun
# Age: 22
# ID: 4
# Name: Vijay
# Age: 24
# ID: 5
# Name: Karthik
# Age: 25
# ⚠️ Conditions
# ✅ Use BETWEEN
# ✅ Use ORDER BY
# ✅ Use fetchall()
# ✅ Use parameterized query
# ❌ Don't filter IDs in Python
# ❌ Don't sort using Python

start_id = int(input("Enter Start ID: "))
end_id = int(input("Enter End ID: "))
cursor.execute("select * from students where id between %s and %s order by id asc",(start_id, end_id))
details = cursor.fetchall()

if details:
    print("Students Found:")
    for i in details:
        print(f"ID: {i[0]}")
        print(f"Name: {i[1]}")
        print(f"Age: {i[2]}")
else:
    print("No Students Found ❌")

cursor.close()
con.close()