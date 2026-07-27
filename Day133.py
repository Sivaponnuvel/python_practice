# 🔹 Question 1 – Functions (**kwargs): Display Employee Details
# Write a Python program using **kwargs to display employee details.
# Program Flow
# Create a function named employee_details(**kwargs).
# Accept any number of keyword arguments.
# Display each key and its corresponding value.
# Example
# Call
# employee_details(
#     id=101,
#     name="Siva",
#     age=21,
#     department="Backend",
#     salary=25000
# )
# Output
# id : 101
# name : Siva
# age : 21
# department : Backend
# salary : 25000
# ⚠️ Conditions
# ✅ Use **kwargs
# ✅ Use a loop
# ✅ Display all key-value pairs
# ❌ Don't access individual keys like kwargs["id"]
# ❌ Don't import any libraries

def employee_details(**kwargs):
    for key, values in kwargs.items():
        print(f"{key} : {values}")

employee_details(
    id=101,
    name="Siva",
    age=21,
    department="Backend",
    salary=25000
)


# 🔹 Question 2 – Intermediate OOP: Employee Class with Salary Hike
# Write a Python program to create an Employee class.
# Program Flow
# Create a class named Employee.
# Create a constructor (__init__) with:
# id
# name
# salary
# Create a method display() to display employee details.
# Create another method increment(amount) that increases the salary by the given amount.
# Create one object using user input.
# Display the details before the increment.
# Take the increment amount from the user.
# Increase the salary.
# Display the updated details.
# Example
# Input
# Enter Employee ID: 101
# Enter Employee Name: Siva
# Enter Salary: 25000
# Enter Increment Amount: 3000
# Output
# Employee Details
# ID     : 101
# Name   : Siva
# Salary : 25000
# After Increment
# ID     : 101
# Name   : Siva
# Salary : 28000
# ⚠️ Conditions
# ✅ Use a class
# ✅ Use __init__()
# ✅ Use display()
# ✅ Create an increment() method
# ✅ Take input from the user
# ❌ Don't modify the salary directly outside the class
# ❌ Don't use global variables

class Employee:

    def __init__(self, id, name, salary):
        self.__id = id
        self.__name = name
        self.__salary = salary

    def display(self):
        print(f"ID     : {self.__id}")
        print(f"Name   : {self.__name}")
        print(f"Salary : {self.__salary}")

    def increment(self, amount):
        self.__salary += amount

emp_id = int(input("Enter Employee ID: "))
emp_name = input("Enter Employee Name: ")
emp_salary = int(input("Enter Salary: "))
emp = Employee(emp_id, emp_name, emp_salary)

print("Employee Details")
emp.display()
emp_increment_salary = int(input("Enter Increment Amount: "))
emp.increment(emp_increment_salary)
print("After Increment")
emp.display()