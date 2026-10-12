# 🟢 Question 1 – Lambda Functions and sorted()
# Topic: Sorting data using custom conditions
# Imagine you're developing an application that stores student records.
# Given this list:
# students = [    {"name": "Arun", "marks": 78},    {"name": "Siva", "marks": 92},    {"name": "Priya", "marks": 85},    {"name": "Kumar", "marks": 65}]
# Write a Python program to:
# 1. Sort students by marks in descending order using sorted() and a lambda function.
# 2. Print each student's name and marks in sorted order.
# 3. Find and print the student with the highest marks.
# Expected output:
# Students Sorted by Marks:
# Siva - 92
# Priya - 85
# Arun - 78
# Kumar - 65
# Top Student: Siva
# Highest Marks: 92
# Rules:
# - Use sorted() with a lambda function.
# - Do not use external libraries.
# - Do not manually hardcode the top student's name.

students = [
    {"name": "Arun", "marks": 78},
    {"name": "Siva", "marks": 92},
    {"name": "Priya", "marks": 85},
    {"name": "Kumar", "marks": 65}
]

sorted_students = sorted(students, key=lambda student: student['marks'], reverse=True)

print("Students Sorted by Marks:")
for i in sorted_students:
    print(f"{i['name']} - {i['marks']}")

top_student = sorted_students[0]

print(f"Top Student: {top_student['name']}")
print(f"Highest Marks: {top_student['marks']}")


