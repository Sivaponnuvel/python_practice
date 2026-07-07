# 🔹 Question 1 – Interview Question: Second Largest Unique Number
# Write a Python program to find the second largest unique number in a list.
# Program Flow
# Take numbers from the user.
# Example:
# Enter Numbers:
# 10 20 30 40 50 40 50
# Output:
# Second Largest Unique Number: 40
# Example 2
# Input:
# Enter Numbers:
# 5 5 5
# Output:
# No Second Largest Number ❌
# Example 3
# Input:
# Enter Numbers:
# 8 2 9 1 9 6
# Output:
# Second Largest Unique Number: 8
# ⚠️ Conditions
# ✅ Take input from the user
# ✅ Remove duplicate values
# ✅ Use built-in functions like set() and sorted()
# ❌ Don't use loops to manually find the second largest
# ❌ Don't import any libraries

numbers = list(map(int, input("Enter Numbers: ").split()))
asc = sorted(set(numbers))

if len(asc) < 2:
    print("No Second Largest Number ❌")
else:
    print(f"Second Largest Unique Number: {asc[-2]}")


# 🔹 Question 2 – OOP: Employee Salary System
# Create a class:
# Employee
# Constructor
# Accept:
# name
# salary
# Instance Methods
# display()
# Output:
# Name   : Siva
# Salary : 25000
# increment(percent)
# Increase the employee's salary by the given percentage.
# Formula:
# new_salary = salary + (salary × percent / 100)
# Program Flow
# Take details for one employee.
# Example:
# Enter Name: Siva
# Enter Salary: 25000
# Enter Increment Percentage: 10
# Output:
# Updated Employee Details
# Name   : Siva
# Salary : 27500.0
# Example 2
# Enter Name: Ram
# Enter Salary: 18000
# Enter Increment Percentage: 25
# Output:
# Updated Employee Details
# Name   : Ram
# Salary : 22500.0
# ⚠️ Conditions
# ✅ Use a class
# ✅ Use constructor
# ✅ Use two instance methods
# ✅ Update the object's salary
# ❌ Don't calculate the increment outside the class

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display(self):
        print(f"Name   : {self.name}")
        print(f"Salary : {self.salary}")
    def increment(self, percentage):
        self.salary = self.salary + (self.salary * percentage / 100)

name = input("Enter Name: ")
salary = float(input("Enter Salary: "))
percentage = float(input("Enter Increment Percentage: "))

emp = Employee(name, salary)
emp.increment(percentage)

print("Updated Employee Details")
emp.display()