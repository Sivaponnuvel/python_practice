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


