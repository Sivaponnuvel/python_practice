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



