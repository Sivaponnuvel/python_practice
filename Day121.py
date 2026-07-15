# 🔹 Question 1 – Dictionary: Student Phone Directory
# Write a Python program to create a simple student phone directory.
# Program Flow
# Take details for 5 students.
# Example:
# Enter Student Name: Siva
# Enter Phone Number: 9876543210
# Store the details in a dictionary where:
# Key → Student Name
# Value → Phone Number
# After storing all entries:
# Take a student name to search.
# Example:
# Enter Student Name to Search: Siva
# If found:
# Student Found ✅
# Name : Siva
# Phone: 9876543210
# Otherwise:
# Student Not Found ❌
# ⚠️ Conditions
# ✅ Use a dictionary
# ✅ Use a loop to take input
# ✅ Search using the dictionary key
# ❌ Don't use lists
# ❌ Don't use JSON or files

students = {}

for i in range(5):
    name = input("Enter Student Name: ")
    phone = input("Enter Phone Number: ")
    students[name] = phone

search = input("Enter Student Name to Search: ")
if search in students:
    print("Student Found ✅")
    print(f"Name: {search}")
    print(f"Phone: {students[search]}")
else:
    print("Student Not Found ❌")


