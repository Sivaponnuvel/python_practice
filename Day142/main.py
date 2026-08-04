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


