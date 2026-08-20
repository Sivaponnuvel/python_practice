# 🔹 Question 1 – JSON: Find Student with Highest Marks
# A JSON file named students.json contains:
# [
#     {"id": 1, "name": "Siva", "marks": 85},
#     {"id": 2, "name": "Rahul", "marks": 92},
#     {"id": 3, "name": "Priya", "marks": 78},
#     {"id": 4, "name": "Arun", "marks": 88}
# ]
# Write a Python program to find the student who scored the highest marks.
# Program Flow
# Open students.json.
# Read the JSON data using json.load().
# Use a loop to find the student with the highest marks.
# Display the student's name and marks.
# Expected Output
# Top Student : Rahul
# Marks       : 92
# ⚠️ Conditions
# ✅ Use the json module
# ✅ Use json.load()
# ✅ Use a dictionary/list from the JSON data
# ✅ Use a loop
# ✅ Find the highest marks manually
# ❌ Don't use max()
# ❌ Don't sort the data
# ❌ Don't use collections
# ❌ Don't import any other library

import json

filename = "D:/Backend/Python/Own try/python_practice/Day157/students.json"

with open(filename, "r")as file:
    read = json.load(file)

top_student = read[0]['name']
top_marks = read[0]['marks']

for i in read:
    if i['marks'] > top_marks:
        top_student = i['name']
        top_marks = i['marks']

print(f"Top Student : {top_student}")
print(f"Marks       : {top_marks}")


# 🔹 Question 2 – Modules: Student Utility Module
# Create your own module named:
# student_utils.py
# 📁 Project Structure
# Day157/
# │
# ├── main.py
# │
# └── student_utils.py
# File 1: student_utils.py
# Create these three functions:
# calculate_average(marks)
# Returns the average of the marks.
# find_highest(marks)
# Returns the highest mark.
# find_lowest(marks)
# Returns the lowest mark.
# Conditions for the functions
# Use loops to find highest and lowest.
# Don't use max().
# Don't use min().
# calculate_average() should calculate the average.
# File 2: main.py
# Program Flow
# Import student_utils.
# Take marks from the user as space-separated integers.
# Convert them into a list.
# Call all three functions.
# Display the results.
# Example
# Input:
# Enter Marks: 85 92 78 88 90
# Output:
# Average : 86.6
# Highest : 92
# Lowest  : 78
# ⚠️ Conditions
# ✅ Create your own module student_utils.py
# ✅ Import the module into main.py
# ✅ Use functions from the module
# ✅ Take input from the user
# ✅ Use a list
# ✅ Use loops where required
# ❌ Don't write the functions again inside main.py
# ❌ Don't use max()
# ❌ Don't use min()
# ❌ Don't import external libraries

from student_utils import calculate_average, find_highest, find_lowest

marks = list(map(int, input("Enter Marks: ").split()))

print(f"Average : {calculate_average(marks)}")
print(f"Highest : {find_highest(marks)}")
print(f"Lowest  : {find_lowest(marks)}")