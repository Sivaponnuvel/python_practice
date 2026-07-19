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


