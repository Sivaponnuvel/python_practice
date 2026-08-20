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


