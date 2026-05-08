# 🔹 Question 1 – Student Management (Add + View)
# 👉 Write a Python program to:
# Create an empty nested dictionary:
# students = {}
# 👉 Show menu:
# 1. Add Student
# 2. View Students
# 3. Exit
# 👉 Functionalities:
# ✅ Add Student
# Take:
# name
# age
# marks
# Store like:
# students[name] = {"age": age, "marks": marks}
# If student already exists:
# Student already exists ❌
# ✅ View Students
# Print all students:
# Siva - Age: 23, Marks: 85
# If no students:
# No students found ❌
# ✅ Exit
# Print:
# Exiting...

students = {}
while True:
    print("Menu:\n1. Add Student\n2. View Students\n3. Exit")
    user = int(input("Choose 1 or 2 or 3: "))
    if user == 1:
        n = int(input("Enter number of students: "))
        for i in range(n):
            name = input("Enter your name: ")
            if name in students:
                print("Student already exists ❌")
            else:
                age = int(input("Enter your age: "))
                marks = int(input("Enter mark: "))
                students[name] = {"age": age, "marks": marks}
    elif user == 2:
        if students:
            for key, value in students.items():
                print(f"{key} - Age: {value['age']}, Marks: {value['marks']}")
        else:
            print("No students found ❌")
    elif user == 3:
        print("Exiting...")
        break


# 🔹 Question 2 – Search + Update Student
# 👉 Using same nested dictionary:
# Show menu:
# 1. Search Student
# 2. Update Marks
# 3. Exit
# ✅ Search Student
# Ask student name.
# If exists:
# Name: Siva
# Age: 23
# Marks: 85
# Else:
# Student not found ❌
# ✅ Update Marks
# Ask:
# student name
# new marks
# If exists:
# update marks
# print updated details
# Else:
# Student not found ❌

while True:
    print("Menu:\n1. Search Student\n2. Update Marks\n3. Exit")
    user = int(input("Choose 1 or 2 or 3: "))
    if user == 1:
        student_name = input("Enter student name to search: ")
        if student_name in students:
            print(f"Name: {student_name}\nAge: {students[student_name]['age']}\nMarks: {students[student_name]['marks']}")
        else:
            print("Student not found ❌")
    elif user == 2:
        student_name1 = input("Enter student name to update: ")
        if student_name1 in students:
            new_mark = int(input("Enter new mark: "))
            students[student_name1]["marks"] = new_mark
            print(f"Updated details:\nName: {student_name1}\nAge: {students[student_name1]['age']}\nMarks: {students[student_name1]['marks']}")
        else:
            print("Student not found ❌")
    elif user == 3:
        print("Exiting...")
        break