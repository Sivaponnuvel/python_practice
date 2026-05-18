# 🔹 Question 1 – Student Result Management System
# Write a Python program to:
# 👉 Create an empty list:
# students = []
# 👉 Create 5 functions:
# add_student(students, roll_no, name, marks)
# view_students(students)
# find_student(students, search_roll)
# calculate_grade(mark)
# top_student(students)
# 👉 Function Details:
# ✅ add_student()
# Store student as dictionary inside list
# Example:
# {
#     "roll_no": 101,
#     "name": "Siva",
#     "marks": 87
# }
# ✅ view_students()
# Print all student details
# ✅ find_student()
# Search student using roll number
# If found → print details
# Otherwise:
# Student not found ❌
# ✅ calculate_grade(mark)
# Rules:
# 90 and above  -> A
# 75 to 89      -> B
# 50 to 74      -> C
# below 50      -> Fail
# ✅ top_student()
# Find highest mark student
# Print student name and marks
# 👉 While viewing students, also print grade
# Example:
# Name: Siva
# Marks: 87
# Grade: B
# 👉 Take details for 3 students from user input
# 👉 Call all functions properly

students = []
# add student
def add_student(students, roll_no, name, marks):
    student = {"roll_no": roll_no, "name": name, "marks": marks}
    students.append(student)
# view student
def view_students(students):
    print("All Students:")
    for i in students:
        print(f"Roll_No: {i['roll_no']}, Name: {i['name']}, Marks: {i['marks']}, Grade: {calculate_grade(i['marks'])}")
# find the student
def find_student(students, search_roll):
    for i in students:
        if i['roll_no'] == search_roll:
            print("Student Found:")
            print(f"Roll_No: {i['roll_no']}, Name: {i['name']}, Marks: {i['marks']}")
            return
    print("Student not found ❌")
# calculate the grade
def calculate_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 75:
        return "B"
    elif mark >= 50 :
        return "C"
    else:
        return "Fail"
# top student
def top_student(students):
    print("Top Student:")
    top_mark = students[0]
    for i in students:
        if i['marks'] > top_mark['marks']:
            top_mark = i
    print(f"Name: {top_mark['name']}")
    print(f"Marks: {top_mark['marks']}")
    print(f"Grade: {calculate_grade(top_mark['marks'])}")

for i in range(3):
    roll_no = int(input("Enter your roll number: "))
    name = input("Enter your name: ")
    marks = int(input("Enter your marks: "))
    add_student(students,roll_no,name,marks)
view_students(students)
search_roll = int(input("Enter your roll number: "))
find_student(students,search_roll)
top_student(students)


