# 🔹 Question 1 – Exception Handling: Login System
# Write a Python program to:
# 👉 Create a custom exception:
# InvalidLoginError
# 👉 Create a function:
# login(username, password)
# Rules:
# ✅ Valid credentials:
# username = "admin"
# password = "1234"
# ✅ If username is incorrect:
# Raise:
# Invalid Username ❌
# ✅ If password is incorrect:
# Raise:
# Invalid Password ❌
# ✅ If both are correct:
# Print:
# Login Successful ✅
# 👉 Take username and password from user
# 👉 Handle exceptions using try-except
# Example Output
# Enter Username: admin
# Enter Password: 1234
# Login Successful ✅
# OR
# Enter Username: siva
# Enter Password: 1234
# Invalid Username ❌
# ⚠️ Conditions:
# ✅ Create custom exception class
# ✅ Use raise
# ✅ Use try-except

class InvalidLoginError(Exception):
    pass

def login(username, password):
    if username != "admin":
        raise InvalidLoginError("Invalid Username ❌")
    elif password != "1234":
        raise InvalidLoginError("Invalid Password ❌")
    
try:
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    login(username, password)
    print("Login Successful ✅")
except InvalidLoginError as e:
    print(e)


# 🔹 Question 2 – JSON: Student Marks Manager
# Write a Python program to:
# 👉 Create a JSON file:
# students.json
# 👉 Store data like:
# [
#     {"id": 1, "name": "Siva", "marks": 85},
#     {"id": 2, "name": "Ram", "marks": 72}
# ]
# 👉 Create functions:
# view_students()
# add_student(student_id, name, marks)
# find_topper()
# Function Details
# ✅ view_students()
# Print all students
# Example:
# ID: 1
# Name: Siva
# Marks: 85
# ✅ add_student(student_id, name, marks)
# Add a new student to JSON file
# Print:
# Student Added ✅
# ✅ find_topper()
# Find student with highest marks manually
# ❌ Do not use max()
# Print:
# Topper:
# Siva - 85
# Program Flow
# Create initial JSON data
# View students
# Take new student details from user
# Add student
# Find topper
# ⚠️ Conditions:
# ✅ Use json.load()
# ✅ Use json.dump()
# ✅ Use functions
# ✅ Use file handling
# ❌ Do not use max()

import json

file_path = "D:/Backend/Python/Own try/practice/Day85/students.json"

students = [{"id": 1, "name": "Siva", "marks": 85}, {"id": 2, "name": "Ram", "marks": 72}]

with open(file_path, "w") as file:
    json.dump(students,file)

def view_students():
    with open(file_path,"r")as file:
        students = json.load(file)
        for i in students:
            print(f"ID: {i['id']}")
            print(f"Name: {i['name']}")
            print(f"Marks: {i['marks']}")
def add_student(student_id, name, marks):
    with open(file_path,"r")as file:
        students = json.load(file)
    students.append({"id": student_id, "name": name, "marks": marks})
    with open(file_path,"w")as file:
        json.dump(students, file)
    print("Student Added ✅")
def find_topper():
    with open(file_path,"r")as file:
        students = json.load(file)
    topper = students[0]
    for i in students:
        if i["marks"] > topper["marks"]:
            topper = i
    print("Topper:")
    print(f"{topper['name']} - {topper['marks']}")

view_students()

student_id = int(input("Enter ID: "))
name = input("Enter Name: ")
marks = int(input("Enter Mark: "))
add_student(student_id, name, marks)

find_topper()