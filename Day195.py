# 🔹 Question 1 – Sum of Digits
# Write a Python program to find the sum of all digits in a given number.
# Examples
# 123 → 1 + 2 + 3 = 6
# 4567 → 4 + 5 + 6 + 7 = 22
# Input
# Enter a number: 12345
# Expected Output
# Sum of digits: 15
# ⚠️ Conditions
# ✅ Use input()
# ✅ Convert the input to an integer
# ✅ Use a while loop
# ✅ Extract digits using arithmetic logic
# ✅ Use % 10 to get the last digit
# ✅ Use // 10 to remove the last digit
# ❌ Don't convert the number into a string
# ❌ Don't use sum()
# ❌ Don't use libraries

number = int(input("Enter a number: "))

sum_num = 0

while number > 0:
    digit = number % 10
    sum_num += digit
    number //= 10

print(f"Sum of digits: {sum_num}")


# 🔹 Question 2 – OOP: Student Class
# Create a Python class called:
# Student
# The class should have these attributes:
# name
# age
# marks
# Create the following method:
# display_student()
# The method should display all student details.
# Program Flow
# Take the details from the user.
# Input:
# Enter student name: Siva
# Enter student age: 22
# Enter student marks: 85
# Expected Output
# Student Name: Siva
# Student Age: 22
# Student Marks: 85
# ⚠️ Conditions
# ✅ Create a Student class
# ✅ Use __init__()
# ✅ Use self
# ✅ Store name, age, and marks
# ✅ Create display_student()
# ✅ Take values using input()
# ✅ Create an object
# ✅ Call display_student()
# ❌ Don't use dictionaries
# ❌ Don't use global variables for student details
# ❌ Don't import libraries

class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display_student(self):
        print(f"Student Name: {self.name}")
        print(f"Student Age: {self.age}")
        print(f"Student Marks: {self.marks}")

name = input("Enter student name: ")
age = int(input("Enter student age: "))
marks = int(input("Enter student marks: "))

stu = Student(name, age, marks)

stu.display_student()