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


# 🔹 Question 2 – Sets: Common Subjects
# Write a Python program to find the common subjects chosen by two students.
# Program Flow
# Take subjects as space-separated input.
# Example:
# Enter Subjects for Student 1:
# Python Java MySQL HTML
# Enter Subjects for Student 2:
# Python Django HTML CSS
# Convert both inputs into sets.
# Find the common subjects using a set operation.
# Example Output
# Common Subjects:
# Python
# HTML
# If there are no common subjects:
# No Common Subjects ❌
# ⚠️ Conditions
# ✅ Use set()
# ✅ Use set intersection (& or intersection())
# ✅ Display the common subjects using a loop
# ❌ Don't compare subjects using nested loops
# ❌ Don't use lists for comparison

student1 = input("Enter Subjects for Student 1: ").split()
student2 = input("Enter Subjects for Student 2: ").split()
student1 = set(student1)
student2 = set(student2)

common_subjects = student1 & student2
if common_subjects:
    print("Common Subjects:")
    for i in common_subjects:
        print(i)
else:
    print("No Common Subjects ❌")