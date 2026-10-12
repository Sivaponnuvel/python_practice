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


# 🟢 Question 2 – File Handling
# Topic: Reading and writing files with exception handling
# Create a Python program that manages a simple list of tasks using a text file named tasks.txt.
# Your program should:
# 1. Ask the user to enter three tasks.
# 2. Write all three tasks to tasks.txt, with each task on a separate line.
# 3. Open the file again and read all tasks.
# 4. Print the saved tasks with numbering, starting from 1.
# 5. Handle FileNotFoundError when reading the file.
# Example input:
# Enter task 1: Learn Python
# Enter task 2: Practice Django
# Enter task 3: Build API
# Expected output:
# Saved Tasks:
# 1. Learn Python
# 2. Practice Django
# 3. Build API
# Rules:
# - Use open() with appropriate file modes.
# - Use with open(...) to manage the file.
# - Use a for loop to collect the three tasks.
# - Use try-except to handle FileNotFoundError while reading.
# - Do not use external libraries.

filename = "D:/Backend/Python/Own try/python_practice/Day210/tasks.txt"

with open(filename, 'w')as file:
    for i in range(3):
        task = input(f"Enter task {i+1}: ")
        file.write(f"{task}\n")

try:
    with open(filename)as file:
        read = file.readlines()

        print("Saved Tasks:")
        for index, task in enumerate(read, start=1):
            print(f"{index}. {task.strip()}")

except FileNotFoundError:
    print("File not found.")