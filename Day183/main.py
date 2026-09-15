# 🔹 Question 1 – Module + Class + return
# Create a module named:
# employee.py
# Inside the module, create a class:
# Employee
# The class should have:
# name
# salary
# Create a method:
# get_details()
# The method should return the employee's details.
# Then create:
# main.py
# Import the Employee class and create an object.
# Program Flow
# Input:
# Enter employee name: Siva
# Enter salary: 25000
# Expected Output:
# Employee Name: Siva
# Salary: 25000
# ⚠️ Conditions
# ✅ Create employee.py
# ✅ Create Employee class
# ✅ Use __init__()
# ✅ Store name and salary
# ✅ Create get_details()
# ✅ Use return inside get_details()
# ✅ Import Employee into main.py
# ✅ Create an object
# ✅ Use input()
# ❌ Don't print employee details inside get_details()
# ❌ Don't create the class directly inside main.py
# ❌ Don't use libraries
# 💡 Interview focus: Understand the difference between:
# return
# and
# print()

from employee import Employee

name = input("Enter employee name: ")
salary = int(input("Enter salary: "))

obj = Employee(name, salary)
print(obj.get_details())


# 🔹 Question 2 – JSON: Store and Read Student Data
# Write a Python program that takes student details from the user and stores them in a JSON file.
# Take:
# name
# age
# course
# Program Flow
# Input:
# Enter student name: Siva
# Enter age: 22
# Enter course: Python Full Stack
# Store the data in:
# student.json
# The JSON file should contain data similar to:
# {
#     "name": "Siva",
#     "age": 22,
#     "course": "Python Full Stack"
# }
# Then read the JSON file and display:
# Student Details:
# Name: Siva
# Age: 22
# Course: Python Full Stack
# ⚠️ Conditions
# ✅ Use input()
# ✅ Create a Python dictionary for the student data
# ✅ Use the json module
# ✅ Use json.dump() to write data
# ✅ Use json.load() to read data
# ✅ Store data in student.json
# ✅ Display the data after reading
# ❌ Don't manually write JSON syntax into the file
# ❌ Don't hardcode student details
# ❌ Don't use any module other than json

import json

student = {}

name = input("Enter student name: ")
age = int(input("Enter age: "))
course = input("Enter course: ")

student['name'] = name
student['age'] = age
student['course'] = course

with open("D:/Backend/Python/Own try/python_practice/Day183/student.json", "w")as file:
    json.dump(student, file)

with open("D:/Backend/Python/Own try/python_practice/Day183/student.json", "r")as file:
    read = json.load(file)

    print(f"Name: {read['name']}")
    print(f"Age: {read['age']}")
    print(f"Course: {read['course']}")