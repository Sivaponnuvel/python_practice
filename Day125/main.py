# 🔹 Question 1 – File Handling: Count the Number of Lines
# Write a Python program to count the total number of lines in a text file.
# Program Flow
# Ask the user to enter the file name.
# Open the file in read mode.
# Count the total number of lines.
# Display the result.
# Example
# Sample File (notes.txt)
# Python
# Java
# C++
# MySQL
# Input
# Enter File Name: notes.txt
# Output
# Total Lines: 4
# ⚠️ Conditions
# ✅ Take the file name from the user
# ✅ Open the file using with
# ✅ Use a loop to count the lines
# ✅ Display only the total number of lines
# ❌ Don't use readlines()
# ❌ Don't import any libraries

try:
    filename = input("Enter File Name: ")
    with open(filename) as file:
        line_count = 0
        for i in file:
            line_count += 1
        print(f"Total Lines: {line_count}")

except FileNotFoundError:
    print("File Not Found ❌")


# 🔹 Question 2 – JSON: Search for a Student by ID
# A JSON file named students.json contains the following data:
# [
#     {"id": 1, "name": "Siva", "age": 21},
#     {"id": 2, "name": "Rahul", "age": 22},
#     {"id": 3, "name": "Vijay", "age": 20}
# ]
# Write a Python program to search for a student using the student ID.
# Program Flow
# Read the JSON file.
# Ask the user to enter a student ID.
# If the ID exists, display the student's details.
# Otherwise, display:
# Student Not Found ❌
# Example
# Input
# Enter Student ID: 2
# Output
# ID: 2
# Name: Rahul
# Age: 22
# ⚠️ Conditions
# ✅ Read data from students.json
# ✅ Use the json module
# ✅ Take the ID from the user
# ✅ Use a loop to search
# ✅ Stop searching once the student is found
# ❌ Don't use list comprehensions
# ❌ Don't use filter()

import json

search_id = int(input("Enter Student ID: "))
with open("D:/Backend/Python/Own try/practice/Day125/students.json","r")as file:
    read = json.load(file)
    for i in read:
        if search_id == i['id']:
            print(f"ID: {i['id']}")
            print(f"Name: {i['name']}")
            print(f"Age: {i['age']}")
            break
    else:
        print("Student Not Found ❌")