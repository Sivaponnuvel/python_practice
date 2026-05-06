# 🔹 Question 1 – Search Student
# 👉 Write a Python program to:
# Take n students input
# Store in nested dictionary like:
# students = {
#     "Siva": {"age": 23, "marks": 85},
#     "Ram": {"age": 21, "marks": 90}
# }
# 👉 Then:
# Ask user to enter a student name
# If student exists → print:
# Name
# Age
# Marks
# If not → print:
# "Student not found ❌"
# 🧠 Example Output:
# Enter name to search: Siva
# Name: Siva
# Age: 23
# Marks: 85

n = int(input("Enter number of students: "))
students = {}
for i in range(n):
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    mark = int(input("Enter mark: "))
    students[name] = {"age": age, "marks": mark}
user = input("Enter student name to search: ")
if user in students:
    print(f"Name: {user}\nAge: {students[user]['age']}\nMarks: {students[user]['marks']}")
else:
    print("Student not found ❌")


# 🔹 Question 2 – Update Marks
# 👉 Using same dictionary:
# Ask user:
# student name
# new marks
# 👉 Do:
# If student exists → update marks
# Print updated details
# If not → print:
# "Student not found ❌"
# 🧠 Example Output:
# Enter name: Ram
# Enter new marks: 95
# Updated:
# Ram - Age: 21, Marks: 95

user1 = input("Enter name: ")
new_mark = int(input("Enter new marks: "))
if user1 in students:
    students[user1]['marks'] = new_mark
    print("Updated:")
    print(f"{user1} - Age: {students[user1]['age']}, Marks: {students[user1]['marks']}")
else:
    print("Student not found ❌")