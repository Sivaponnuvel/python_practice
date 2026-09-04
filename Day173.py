# 🔹 Question 1 – OOP: Student Result System
# Write a Python program using a class to calculate a student's total, average, and result.
# Create a class:
# Student
# The class should have:
# name
# marks
# Create methods:
# calculate_total()
# calculate_average()
# display_result()
# Program Flow
# Take the student's name and marks for 3 subjects from the user.
# Input:
# Enter Student Name: Siva
# Enter Tamil Mark: 85
# Enter English Mark: 78
# Enter Maths Mark: 92
# Output:
# Student Name: Siva
# Total: 255
# Average: 85.0
# Result: Pass
# Result Rule
# Average >= 50 → Pass
# Average < 50 → Fail
# ⚠️ Conditions
# ✅ Use a class
# ✅ Use __init__()
# ✅ Use self
# ✅ Use multiple methods
# ✅ Use input()
# ✅ Store the 3 marks in a list
# ❌ Don't calculate total/average outside the class
# ❌ Don't use sum()
# ❌ Don't use statistics
# ❌ Don't import any libraries

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_total(self):
        total_mark = 0
        for i in self.marks:
            total_mark += i
        return total_mark

    def calculate_average(self):
        total = self.calculate_total()
        avg  = total / len(self.marks)
        return avg

    def display_result(self):
        total = self.calculate_total()
        avg = self.calculate_average()
        result = ""
        if avg >= 50:
            result = "Pass"
        else:
            result = "Fail"

        print(f"Student Name: {self.name}")
        print(f"Total: {total}")
        print(f"Average: {avg}")
        print(f"Result: {result}")

name = input("Enter Student Name: ")
tamil = int(input("Enter Tamil Mark: "))
english = int(input("Enter English Mark: "))
maths = int(input("Enter Maths Mark: "))
marks = [tamil, english, maths]

obj = Student(name, marks)
obj.display_result()


# 🔹 Question 2 – Decorator: Check Positive Number
# Write a Python program using a decorator to check whether the number passed to a function is positive or not.
# Create a decorator:
# check_positive
# Apply it to:
# display_number(number)
# Program Flow
# Take a number from the user.
# If the number is positive, the decorator should allow the function to execute.
# Example 1:
# Enter a number: 25
# Output:
# Positive number ✅
# Number: 25
# If the number is zero or negative:
# Example 2:
# Enter a number: -10
# Output:
# Number must be positive ❌
# ⚠️ Conditions
# ✅ Create a decorator function
# ✅ Create a wrapper function
# ✅ Use @check_positive
# ✅ Use *args
# ✅ Call the original function only when the number is positive
# ✅ Use input()
# ❌ Don't put the positive-number checking logic inside display_number()
# ❌ Don't use any libraries
# 💡 Hint
# Your decorator should follow this general idea:
# def check_positive(func):
#     def wrapper(*args):
#         # check the number
#         # call func() if valid
#     return wrapper

def check_positive(func):
    def wrapper(*args):
        number = args[0]
        if number > 0:
            print("Positive number ✅")
            return func(*args)
        else:
            print("Number must be positive ❌")
    return wrapper

@check_positive
def display_number(number):
    print(f"Number: {number}")

number = int(input("Enter a number: "))
display_number(number)