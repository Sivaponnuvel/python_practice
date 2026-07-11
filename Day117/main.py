# 🔹 Question 1 – Modules: Temperature Converter
# Create the following structure:
# Day117/
# │
# ├── converter.py
# └── main.py
# converter.py
# Create the following functions:
# celsius_to_fahrenheit(celsius)
# fahrenheit_to_celsius(fahrenheit)
# Formulas:
# F = (C × 9/5) + 32
# C = (F − 32) × 5/9
# Both functions should return the converted value.
# main.py
# Import the functions from converter.py.
# Display the menu:
# 1. Celsius to Fahrenheit
# 2. Fahrenheit to Celsius
# Take:
# Enter Choice:
# Enter Temperature:
# Display the converted temperature.
# Example Output 1
# 1. Celsius to Fahrenheit
# 2. Fahrenheit to Celsius
# Enter Choice: 1
# Enter Temperature: 25
# Converted Temperature: 77.0°F
# Example Output 2
# Enter Choice: 2
# Enter Temperature: 98.6
# Converted Temperature: 37.0°C
# ⚠️ Conditions
# ✅ Create your own module
# ✅ Import functions into main.py
# ✅ Functions should return values
# ❌ Don't write all code in one file

from converter import celsius_to_fahrenheit, fahrenheit_to_celsius

print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = int(input("Enter Choice: "))
temp = float(input("Enter Temperature: "))

if choice == 1:
    print(f"Converted Temperature: {celsius_to_fahrenheit(temp)}°F")
elif choice == 2:
    print(f"Converted Temperature: {fahrenheit_to_celsius(temp)}°C")
else:
    print("Wrong Choice ❌")


# 🔹 Question 2 – JSON: Student Marks Management
# Create a file:
# students.json
# Store the following data:
# [
#     {"id": 1, "name": "Siva", "marks": 85},
#     {"id": 2, "name": "Ram", "marks": 72},
#     {"id": 3, "name": "Arun", "marks": 91}
# ]
# Create two functions:
# view_students()
# Display:
# --- Student Details ---
# ID: 1
# Name: Siva
# Marks: 85
# for all students.
# search_student(student_name)
# Take a student name from the user.
# If found:
# Student Found ✅
# ID: 2
# Name: Ram
# Marks: 72
# Otherwise:
# Student Not Found ❌
# Program Flow
# Display all students.
# Ask for a student name.
# Search and display the result.
# ⚠️ Conditions
# ✅ Use json.load()
# ✅ Use functions
# ✅ Use file handling
# ✅ Search manually using a loop
# ❌ Don't use list comprehensions
# ❌ Don't use external libraries

import json
filename = "D:/Backend/Python/Own try/practice/Day117/students.json"

students = [
    {"id": 1, "name": "Siva", "marks": 85},
    {"id": 2, "name": "Vijay", "marks": 72},
    {"id": 3, "name": "Kishore", "marks": 91}
]

with open(filename,"w")as file:
    json.dump(students, file)

def view_students():
    with open(filename, 'r')as file:
        read = json.load(file)
        print("--- Student Details ---")
        for i in read:
            print(f"ID: {i['id']}")
            print(f"Name: {i['name']}")
            print(f"Marks: {i['marks']}")

def search_student(student_name):
    with open(filename, 'r')as file:
        read = json.load(file)
        for i in read:
            if student_name == i['name']:
                print("Student Found ✅")
                print(f"ID: {i['id']}")
                print(f"Name: {i['name']}")
                print(f"Marks: {i['marks']}")
                return
        print("Student Not Found ❌")

view_students()
student_name = input("Enter Student Name: ").capitalize()
search_student(student_name)