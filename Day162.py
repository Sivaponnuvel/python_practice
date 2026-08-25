# 🔹 Question 1 – OOP: Multiple Inheritance
# Write a Python program using multiple inheritance.
# Program Flow
# Create two parent classes:
# Class 1: Student
# Constructor should initialize:
# name
# student_id
# Create a method:
# student_details()
# It should display:
# Name       : Siva
# Student ID : 101
# Class 2: Course
# Constructor should initialize:
# course_name
# duration
# Create a method:
# course_details()
# It should display:
# Course   : Python
# Duration : 3 Months
# Create Child Class: Enrollment
# Enrollment should inherit from both:
# Student
# Course
# Its constructor should use the parent constructors to initialize all four values.
# Create a method:
# display()
# Expected output:
# Enrollment Details
# Name       : Siva
# Student ID : 101
# Course     : Python
# Duration   : 3 Months
# Input
# Enter Name: Siva
# Enter Student ID: 101
# Enter Course Name: Python
# Enter Duration: 3 Months
# ⚠️ Conditions
# ✅ Use multiple inheritance
# ✅ Create Student and Course parent classes
# ✅ Create Enrollment(Student, Course)
# ✅ Use __init__()
# ✅ Call both parent constructors
# ✅ Use methods from both parent classes
# ✅ Take input from the user
# ❌ Don't duplicate all parent attributes directly without calling their constructors
# ❌ Don't use global variables
# 💡 Hint
# Student.__init__(self, name, student_id)
# Course.__init__(self, course_name, duration)

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
    def student_details(self):
        print(f"Name       : {self.name}")
        print(f"Student ID : {self.student_id}")

class Course:
    def __init__(self, course_name, duration):
        self.course_name = course_name
        self.duration = duration
    def course_details(self):
        print(f"Course   : {self.course_name}")
        print(f"Duration : {self.duration}")

class Enrollment(Student, Course):
    def __init__(self, name, student_id, course_name, duration):
        Student.__init__(self, name, student_id)
        Course.__init__(self, course_name, duration)

    def display(self):
        print("Enrollment Details")
        self.student_details()
        self.course_details()


name = input("Enter Name: ")
student_id = int(input("Student ID : "))
course_name = input("Enter Course Name: ")
duration = input("Enter Duration: ")

enroll = Enrollment(name, student_id, course_name, duration)
enroll.display()


# 🔹 Question 2 – Recursion: Find the Largest Digit
# Write a Python program to find the largest digit in a number using recursion.
# Example 1
# Input:
# Enter Number: 58391
# Output:
# Largest Digit: 9
# Example 2
# Input:
# Enter Number: 2468
# Output:
# Largest Digit: 8
# Program Flow
# Create a function named:
# find_largest_digit(number)
# Use recursion to compare digits.
# Extract the last digit using % 10.
# Remove the last digit using // 10.
# Return the largest digit.
# ⚠️ Conditions
# ✅ Use a recursive function
# ✅ Use % and //
# ✅ Take input from the user
# ✅ Return the largest digit
# ❌ Don't use loops
# ❌ Don't convert the number to a string
# ❌ Don't use max()
# ❌ Don't import any libraries
# 💡 Hint
# Think about the base case:
# if number < 10:
#     return number
# Then compare:
# last_digit = number % 10
# remaining_largest = find_largest_digit(number // 10)

def find_largest_digit(number):
    if number < 10:
        return number
    else:
        last_digit = number % 10
        remaining_largest = find_largest_digit(number // 10)
        return last_digit if last_digit > remaining_largest else remaining_largest

number = int(input("Enter Number: "))
print(f"Largest Digit: {find_largest_digit(number)}")