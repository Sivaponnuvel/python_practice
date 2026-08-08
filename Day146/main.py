# 🔹 Question 1 – File Handling: Count Words in a File
# Write a Python program to count the total number of words in a text file.
# Program Flow
# Ask the user to enter the file name.
# Open the file in read mode.
# Count the total number of words in the file.
# Display the result.
# Example
# Sample File (notes.txt)
# Python is easy
# Java is powerful
# MySQL database
# Input
# Enter File Name: notes.txt
# Output
# Total Words: 7
# ⚠️ Conditions
# ✅ Take the file name from the user
# ✅ Use with
# ✅ Use a loop
# ✅ Use split() to count words
# ✅ Handle FileNotFoundError
# ❌ Don't import any libraries
# ❌ Don't use readlines()

try:
    filename = input("Enter File Name: ")
    with open(filename) as file:
        details = file.read().split()
        count = 0
        for i in details:
            count += 1
        print(f"Total Words: {count}")
except FileNotFoundError:
    print("File Not Found ❌")


# 🔹 Question 2 – JSON: Add a New Student
# A JSON file named students.json contains the following data:
# [
#     {"id": 1, "name": "Siva", "age": 21},
#     {"id": 2, "name": "Rahul", "age": 22}
# ]
# Write a Python program to add a new student to the JSON file.
# Program Flow
# Read the JSON data from students.json.
# Take the following inputs from the user:
# Student ID
# Student Name
# Student Age
# Add the new student to the existing list.
# Write the updated data back to the same JSON file.
# Display:
# Student Added Successfully ✅
# Example
# Input
# Enter Student ID: 3
# Enter Student Name: Priya
# Enter Student Age: 20
# Output
# Student Added Successfully ✅
# ⚠️ Conditions
# ✅ Use the json module
# ✅ Read the existing JSON data
# ✅ Append the new student
# ✅ Write back using json.dump()
# ✅ Take input from the user
# ❌ Don't overwrite the file without first reading the existing data
# ❌ Don't import any libraries other than json

import json
filename = "D:/Backend/Python/Own try/python_practice/Day146/students.json"

with open(filename, "r") as file:
    students = json.load(file)

stu_id = int(input("Enter Student ID: "))
stu_name = input("Enter Student Name: ")
stu_age = int(input("Enter Student Age: "))

new_student ={
    "id": stu_id,
    "name": stu_name,
    "age": stu_age
}
students.append(new_student)

with open(filename, "w") as file:
    json.dump(students, file, indent=4)

print("Student Added Successfully ✅")