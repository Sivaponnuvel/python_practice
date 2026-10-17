# Question 1 – List Coding Problem
# Topic: Python Lists
# Write a Python program to find the second-largest unique number in a list.
# Example:
# numbers = [10, 20, 4, 45, 99, 99]
# Expected output:
# Second Largest Number: 45
# Requirements:
# 1. Find the second-largest distinct number.
# 2. Don't count duplicate values more than once.
# 3. Don't hardcode the answer.
# 4. Handle the case where a second-largest unique number doesn't exist.

numbers = [10, 20, 4, 45, 99, 99]

unique_list = list(set(numbers))
unique_list.sort()

if len(unique_list) < 2:
    print("Second largest unique number doesn't exist")
else:
    print(f"Second Largest Number: {unique_list[-2]}")


# Question 2 – OOP: Inheritance
# Topic: Classes, Objects, Inheritance and super()
# Create a parent class Employee and a child class Developer.
# Requirements:
# 1. Employee class should have name and salary attributes.
# 2. Create a method display_details() to print the employee's name and salary.
# 3. Create a Developer class that inherits from Employee.
# 4. Add a programming_language attribute to Developer.
# 5. Use super() to initialize the parent-class attributes.
# 6. Override display_details() in Developer to display all three details.
# Expected output:
# Employee Name: Siva
# Salary: 30000
# Programming Language: Python
# Conditions: Use proper class and object creation. Don't hardcode the output directly.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display_details(self):
        print(f"Employee Name: {self.name}")
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
language = input("Enter prgramming language: ")

obj = Developer(name, salary, language)

obj.display_details()