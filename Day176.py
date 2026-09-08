# 🔹 Question 1 – Decorator: Authentication Check
# Write a Python program using a decorator to check whether a user is logged in before allowing a function to execute.
# Create a decorator:
# check_login
# Apply it to:
# dashboard(username)
# Program Flow
# Take the login status from the user.
# Input:
# Enter username: Siva
# Enter login status (yes/no): yes
# Output:
# Login successful ✅
# Welcome to Dashboard, Siva
# If the user is not logged in:
# Input:
# Enter username: Siva
# Enter login status (yes/no): no
# Output:
# Please login first ❌
# ⚠️ Conditions
# ✅ Create a decorator function
# ✅ Create a wrapper function
# ✅ Use @check_login
# ✅ Use *args
# ✅ Check login status inside the decorator
# ✅ Call dashboard() only when logged in
# ❌ Don't put the login-checking logic inside dashboard()
# ❌ Don't use any libraries

def check_login(func):
    def wrapper(*args):
        status = input("Enter login status (yes/no): ").lower()
        if status == "yes":
            print("Login successful ✅")
            return func(*args)
        else:
            print("Please login first ❌")
    return wrapper
        
@check_login
def dashboard(username):
    print(f"Welcome to Dashboard, {username}")
    
username = input("Enter username: ")
dashboard(username)


# 🔹 Question 2 – OOP Next Level: Inheritance
# Create a parent class and a child class using inheritance.
# Create parent class:
# Employee
# It should have:
# name
# salary
# Create a method:
# display_employee()
# Create child class:
# Developer
# It should inherit from Employee and have an additional attribute:
# programming_language
# Create a method:
# display_developer()
# Program Flow
# Take the details from the user.
# Input:
# Enter Employee Name: Siva
# Enter Salary: 30000
# Enter Programming Language: Python
# Output:
# Employee Name: Siva
# Salary: 30000
# Programming Language: Python
# ⚠️ Conditions
# ✅ Create a parent class Employee
# ✅ Create a child class Developer
# ✅ Use inheritance
# ✅ Use super().__init__()
# ✅ Use self
# ✅ Use __init__()
# ✅ Create methods in both classes
# ✅ Take input from the user
# ❌ Don't duplicate name and salary initialization in Developer
# ❌ Don't import any libraries

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_employee(self):
        print(f"Employee Name: {self.name}")
        print(f"Salary: {self.salary}")

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def display_developer(self):
        self.display_employee()
        print(f"Programming Language: {self.programming_language}")

name = input("Enter Employee Name: ")
salary = int(input("Enter Salary: "))
programming_language = input("Enter Programming Language: ")

obj = Developer(name, salary, programming_language)

obj.display_developer()