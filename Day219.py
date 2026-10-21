# 🔹 Question 1 – List Coding Problem
# Topic: Lists, Loops and Conditional Statements
# Write a Python program to find the missing number in a list containing distinct numbers from 1 to n.
# Example:
# nums = [1, 2, 4, 5, 6]n = 6
# Expected output:
# Missing Number: 3
# Requirements:
# 1. Get the list of numbers and n from the user.
# 2. Find the number missing from the range 1 to n.
# 3. Display the missing number.
# 4. Your program should work for different input lists.
# Conditions:
# - Use a loop and conditional statements.
# - Do not use external libraries.
# - Do not hardcode the missing number.
# - Do not use sorting.
# - Do not use the mathematical sum formula \(n(n+1)/2\).

n = int(input("Enter the value of n: "))

nums = []
print("Enter the numbers:")

for i in range(n - 1):
    num = int(input())
    nums.append(num)

missing_number = 0

for number in range(1, n + 1):
    if number not in nums:
        missing_number = number
        break

print("Missing Number:", missing_number)


# 🔹 Question 2 – OOP Coding Problem
# Topic: Inheritance, Constructors and Instance Attributes
# Create a parent class named Employee and a child class named Developer.
# Requirements:
# 1. Create an Employee class with an __init__() method.
# 2. Initialize name and salary using the constructor.
# 3. Create a display_details() method that prints the employee's name and salary.
# 4. Create a Developer class that inherits from Employee.
# 5. Add a programming_language attribute to Developer.
# 6. Use super() to call the parent class constructor.
# 7. Create a Developer object and display all three details.
# Expected output:
# Name: Arun
# Salary: 30000
# Programming Language: Python
# Conditions:
# - Use proper inheritance and object creation.
# - Use self to access instance attributes.
# - Do not import libraries.
# - Do not hardcode the entire output outside the class methods.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")

class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language
    def display_details(self):
        super().display_details()
        print(f"Programming Language: {self.language}")

name = input("Enter employee name: ")
salary = int(input("Enter salary: "))
language = input("Enter programming language: ")

obj = Developer(name, salary, language)

obj.display_details()