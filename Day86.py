# 🔹 Question 1 – Create Database and Table (MySQL)
# Write a Python program to:
# 👉 Import:
# mysql.connector
# 👉 Connect to MySQL Server
# 👉 Create a database:
# student_db
# 👉 Use the database
# 👉 Create a table:
# students
# Columns:
# Column	Type
# id	INT AUTO_INCREMENT PRIMARY KEY
# name	VARCHAR(100)
# age	INT
# 👉 Commit changes
# 👉 Close connection
# Example Output
# Database Created Successfully ✅
# Table Created Successfully ✅
# ⚠️ Conditions:
# ✅ Use mysql.connector.connect()
# ✅ Use cursor()
# ✅ Use execute()
# ✅ Use commit()
# ✅ Use close()

import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "siva2025" 
)
cursor = con.cursor()

cursor.execute("create database if not exists student_db")
print("Database Created Successfully ✅")

cursor.execute("use student_db")

cursor.execute("""
               create table if not exists students(
               id int primary key auto_increment,
               name varchar(100),
               age int)
""")
print("Table Created Successfully ✅")
con.commit()



# 🔹 Question 2 – Insert and View Students
# Using the same database:
# student_db
# and table:
# students
# 👉 Take details for 3 students from user
# Input:
# Name
# Age
# 👉 Insert records into database
# 👉 After insertion print:
# Student Added Successfully ✅
# 👉 Fetch all student records
# 👉 Display them like:
# Example Output
# Enter Name: Siva
# Enter Age: 23
# Enter Name: Ram
# Enter Age: 21
# Enter Name: Arun
# Enter Age: 22
# Student Added Successfully ✅
# --- Student Records ---
# ID: 1
# Name: Siva
# Age: 23
# ID: 2
# Name: Ram
# Age: 21
# ID: 3
# Name: Arun
# Age: 22
# ⚠️ Conditions:
# ✅ Use:
# cursor.execute(
#     "INSERT INTO students(name, age) VALUES (%s, %s)",
#     (name, age)
# )
# ✅ Use loop
# ✅ Use SELECT * FROM students
# ❌ Do not manually enter ID


for i in range(3):
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    cursor.execute("insert into students(name,age) values (%s, %s)",(name,age))
print("Student Added Successfully ✅")

cursor.execute("select * from students")
details = cursor.fetchall()

print("--- Student Records ---")
for i in details:
    print(f"ID: {i[0]}")
    print(f"Name: {i[1]}")
    print(f"Age: {i[2]}")

con.commit()
cursor.close()
con.close()