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


# 🔹 Question 2 – Advanced Decorator: Decorator with *args and **kwargs
# Write a Python program to create a decorator that checks whether all arguments passed to a function are positive numbers.
# Create a decorator named:
# positive_numbers
# The decorator should use:
# *args
# **kwargs
# Program Flow
# Create a function:
# calculate_sum(a, b, c)
# which returns the sum of the three numbers.
# Apply the decorator:
# @positive_numbers
# Before executing the function:
# Check all arguments.
# If any argument is 0 or negative, raise:
# ValueError: All numbers must be positive ❌
# Otherwise execute the function normally.
# Example 1
# Input
# Enter First Number: 10
# Enter Second Number: 20
# Enter Third Number: 30
# Output
# Result: 60
# Example 2
# Input
# Enter First Number: 10
# Enter Second Number: -5
# Enter Third Number: 20
# Output
# Error: All numbers must be positive ❌
# ⚠️ Conditions
# ✅ Create a decorator positive_numbers
# ✅ Use an inner wrapper()
# ✅ Use *args and **kwargs
# ✅ Check the arguments inside the decorator
# ✅ Use raise ValueError
# ✅ Use @positive_numbers
# ✅ Return the original function's result
# ✅ Use try-except when calling the decorated function
# ❌ Don't validate the numbers inside calculate_sum()
# ❌ Don't modify calculate_sum() to perform validation
# ❌ Don't import any libraries

def positive_numbers(func):
    def wrapper(*args, **kwargs):
        for i in args:
            if i <= 0:
                raise ValueError("All numbers must be positive ❌")
        for i in kwargs.values():
            if i <= 0:
                raise ValueError("All numbers must be positive ❌")
        return func(*args, **kwargs)
    return wrapper

@positive_numbers
def calculate_sum(a, b, c):
    return a + b + c

try:
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    c = int(input("Enter Third Number: "))
    print(f"Result: {calculate_sum(a, b, c)}")

except ValueError as e:
    print(f"Error: {e}")