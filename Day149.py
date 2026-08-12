# 🔹 Question 1 – Advanced OOP: Inheritance + Method Overriding
# Write a Python program using inheritance and method overriding.
# Program Flow
# Create a parent class named Employee.
# Constructor __init__() should initialize:
# name
# salary
# Create a method:
# display()
# which displays the employee's name and salary.
# Then create a child class named Developer that inherits from Employee.
# The Developer class should have an additional attribute:
# language
# Override the display() method in Developer to display:
# Developer Details
# Name     : Siva
# Salary   : 30000
# Language : Python
# Create one Developer object using user input and display its details.
# Example
# Input
# Enter Developer Name: Siva
# Enter Salary: 30000
# Enter Programming Language: Python
# Output
# Developer Details
# Name     : Siva
# Salary   : 30000
# Language : Python
# ⚠️ Conditions
# ✅ Use a parent class Employee
# ✅ Use a child class Developer
# ✅ Use inheritance
# ✅ Use super().__init__()
# ✅ Override display()
# ✅ Take input from the user
# ❌ Don't duplicate name and salary initialization in Developer.__init__()
# ❌ Don't use global variables

class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def display(self):
        print(f"Name     : {self.__name}")
        print(f"Salary   : {self.__salary}")

class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.__language = language

    def display(self):
        print("Developer Details")
        super().display()
        print(f"Language : {self.__language}")

name = input("Enter Developer Name: ")
salary = int(input("Enter Salary: "))
language = input("Enter Programming Language: ")

obj = Developer(name, salary, language)
obj.display()


