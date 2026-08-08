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

