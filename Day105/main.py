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


