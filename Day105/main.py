# 🔹 Question 1 – Context Manager: File Logger
# Write a Python program to:
# Create a class:
# FileLogger
# The class should work as a custom context manager.
# Constructor
# Accept one argument:
# filename
# Implement:
# __enter__()
# Open the file in append mode and return the file object.
# Implement:
# __exit__()
# Close the file and print:
# File Closed Successfully ✅
# Program Flow
# Take a message from the user.
# Use your context manager like this:
# with FileLogger("log.txt") as file:
#     file.write(message + "\n")
# After writing, display:
# Message Saved Successfully ✅
# Example Output
# Enter Message: Python is awesome
# Message Saved Successfully ✅
# File Closed Successfully ✅
# If you open log.txt afterwards, it should contain:
# Python is awesome
# ⚠️ Conditions
# ✅ Create a custom context manager using __enter__() and __exit__()
# ✅ Use the with statement
# ✅ Open the file in append mode
# ❌ Don't use contextlib
# ❌ Don't manually call close() outside the class

class FileLogger:
    def __init__(self, filename):
        self.filename = filename
    def __enter__(self):
        self.file = open(self.filename, "a")
        return self.file
    def __exit__(self, exc_type, exc, tb):
        self.file.close()
        print("File Closed Successfully ✅")

message = input("Enter Message: ")
with FileLogger("D:/Backend/Python/Own try/practice/Day105/log.txt")as file:
    file.write(message + "\n")
    print("Message Saved Successfully ✅")


# 🔹 Question 2 – OOP: Operator Overloading
# Create a class:
# Book
# Constructor
# Accept:
# title
# pages
# Overload the + operator.
# When two Book objects are added:
# book1 + book2
# Return the total number of pages.
# Program Flow
# Take input for two books.
# Example:
# Enter Book 1 Title: Python
# Enter Book 1 Pages: 350
# Enter Book 2 Title: MySQL
# Enter Book 2 Pages: 250
# Create objects.
# Add them:
# total = book1 + book2
# Display:
# Total Pages: 600
# Example Output
# Enter Book 1 Title: Python
# Enter Book 1 Pages: 300
# Enter Book 2 Title: Django
# Enter Book 2 Pages: 450
# Total Pages: 750
# ⚠️ Conditions
# ✅ Use __add__()
# ✅ Create two objects
# ✅ Return the total pages
# ❌ Don't create a separate function for addition
# ❌ Don't add page values directly outside the class

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    def __add__(self, other):
        return self.pages + other.pages

title1 = input("Enter Book 1 Title: ")
pages1 = int(input("Enter Book 1 Pages: "))
title2 = input("Enter Book 2 Title: ")
pages2 = int(input("Enter Book 2 Pages: "))

book1 = Book(title1, pages1)
book2 = Book(title2, pages2)
print(f"Total Pages: {book1 + book2}")