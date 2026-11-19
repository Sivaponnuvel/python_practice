# Question 1 – Write and Read a File
# Interview Topics: open(), write(), read(), with open(), File Handling.
# Write a Python program to get student details from the user, save them into a text file, and read the saved details.
# Requirements:
# 1. Get student name, age, and course using input().
# 2. Create a file named student.txt.
# 3. Use with open() with write mode ("w").
# 4. Write all student details into the file.
# 5. Open the same file using read mode ("r").
# 6. Read and display all saved details.
# Sample Input:
# Enter student name: Arun
# Enter student age: 22
# Enter student course: Python Full Stack
# Expected Output:
# Student Details:
# Name: Arun
# Age: 22
# Course: Python Full Stack

filename = "D:/Backend/Python/Own try/python_practice/Day248/student.txt"

name = input("Enter student name: ")
age = input("Enter student age: ")
course = input("Enter student course: ")

with open(filename, 'w')as file:
    file.write(f"{name}\n")
    file.write(f"{age}\n")
    file.write(f"{course}\n")

with open(filename, 'r')as file:
    read = file.readlines()

    print("Student Details:")
    print(f"Name: {read[0].strip()}")
    print(f"Age: {read[1].strip()}")
    print(f"Course: {read[2].strip()}")


