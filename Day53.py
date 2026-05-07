# 🔹 Question 1 – Add New Student
# 👉 Write a Python program to:
# Create a nested dictionary with some initial students
# Ask user:
# name
# age
# marks
# 👉 Do:
# If student already exists → print
# "Student already exists ❌"
# Else:
# Add new student
# Print updated dictionary
# 🧠 Example Output:
# Enter name: Siva
# Student already exists ❌
# OR
# Enter name: Arun
# Added successfully ✅
# All Students:
# Siva - Age: 23, Marks: 85
# Arun - Age: 22, Marks: 88

n = int(input("Enter number of students: "))
students = {}
for i in range(n):
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    mark = int(input("Enter mark: "))
    students[name] = {"age": age, "marks": mark}
new_name = input("Enter name: ")
if new_name in students:
    print("Student already exists ❌")
else:
    new_age = int(input("Enter your age: "))
    new_mark = int(input("Enter mark: "))
    students[new_name] = {"age": new_age, "marks": new_mark}
    print("Added successfully ✅")
print("All Students:")
for key, value in students.items():
    print(f"{key} - Age: {value['age']}, Marks: {value['marks']}")


# 🔹 Question 2 – Delete Student
# 👉 Using same dictionary:
# Ask user to enter student name to delete
# 👉 Do:
# If exists → delete student
# Print updated list
# If not → print
# "Student not found ❌"
# 🧠 Example Output:
# Enter name to delete: Ram
# Updated Students:
# Siva - 85
# Arun - 88


user = input("Enter student name to delete: ")
if user in students:
    del students[user]
    print("Updated Students: ")
    for key, value in students.items():
        print(f"{key} - {value['marks']}")
else:
    print("Student not found ❌")