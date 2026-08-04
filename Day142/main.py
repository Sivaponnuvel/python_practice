# 🔹 Question 1 – File Handling: Copy File Contents
# Write a Python program to copy the contents of one text file to another text file.
# Program Flow
# Ask the user to enter the source file name.
# Ask the user to enter the destination file name.
# Read the contents of the source file.
# Write the contents into the destination file.
# If the copy is successful, display:
# File Copied Successfully ✅
# If the source file does not exist, display:
# Source File Not Found ❌
# Example
# Sample File (notes.txt)
# Python
# Java
# MySQL
# Input
# Enter Source File: notes.txt
# Enter Destination File: backup.txt
# Output
# File Copied Successfully ✅
# ⚠️ Conditions
# ✅ Take both file names from the user
# ✅ Use with
# ✅ Read from one file
# ✅ Write to another file
# ✅ Handle FileNotFoundError
# ❌ Don't import any libraries
# ❌ Don't use shutil

try:
    src_file = input("Enter Source File: ")
    dest_file = input("Enter Destination File: ")

    with open(src_file) as src:
        content = src.read()

    with open(dest_file, "w") as dest:
        dest.write(content)
        print("File Copied Successfully ✅")

except FileNotFoundError:
    print("File Not Found ❌")


# 🔹 Question 2 – Modules (Intermediate): Create and Use Your Own Module
# This question has 2 files.
# File 1: calculator.py
# Create a module named calculator.py.
# Create the following functions:
# add(a, b)
# subtract(a, b)
# multiply(a, b)
# Each function should return the result.
# File 2: main.py
# Program Flow
# Import the calculator module.
# Take two integers from the user.
# Display:
# Addition
# Subtraction
# Multiplication
# Example
# Input
# Enter First Number: 10
# Enter Second Number: 5
# Output
# Addition       : 15
# Subtraction    : 5
# Multiplication : 50
# ⚠️ Conditions
# ✅ Create your own module (calculator.py)
# ✅ Import the module into main.py
# ✅ Use functions from the module
# ✅ Take input from the user
# ❌ Don't write all functions inside main.py
# ❌ Don't import any built-in math modules

from calculator import add, subtract, multiply

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print(f"Addition       : {add(num1, num2)}")
print(f"Subtraction    : {subtract(num1, num2)}")
print(f"Multiplication : {multiply(num1, num2)}")