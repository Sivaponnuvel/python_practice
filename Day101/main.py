# 🔹 Question 1 – JSON: Employee Search System
# Create a JSON file:
# employees.json
# Store initial data:
# [
#     {"id": 101, "name": "Siva", "department": "IT"},
#     {"id": 102, "name": "Ram", "department": "HR"},
#     {"id": 103, "name": "Arun", "department": "Finance"}
# ]
# Create Functions
# view_employees()
# Display all employees.
# Output:
# --- Employees ---
# ID: 101
# Name: Siva
# Department: IT
# search_employee(emp_id)
# Search employee using ID.
# If found:
# Employee Found ✅
# ID: 102
# Name: Ram
# Department: HR
# Otherwise:
# Employee Not Found ❌
# Program Flow
# Display all employees
# Enter Employee ID: 102
# Employee Found ✅
# ID: 102
# Name: Ram
# Department: HR
# ⚠️ Conditions
# ✅ Use json.load()
# ✅ Use functions
# ✅ Use file handling
# ✅ Search manually using loop
# ❌ Don't use list comprehension
# ❌ Don't use external libraries

import json
filename = "D:/Backend/Python/Own try/practice/Day101/employees.json"

def view_employees():
    with open(filename,"r") as file:
        read = json.load(file)
        print("--- Employees ---")
        for i in read:
            print(f"ID: {i['id']}")
            print(f"Name: {i['name']}")
            print(f"Department: {i['department']}")

def search_employee(emp_id):
    with open(filename,"r") as file:
        read = json.load(file)
        for i in read:
            if emp_id == i['id']:
                print("Employee Found ✅")
                print(f"ID: {i['id']}")
                print(f"Name: {i['name']}")
                print(f"Department: {i['department']}")
                return True
        print("Employee Not Found ❌")

view_employees()
emp_id = int(input("Enter Employee ID: "))
search_employee(emp_id)


# 🔹 Question 2 – Custom Exception: Email Validation
# Create custom exception:
# InvalidEmailError
# Create function:
# validate_email(email)
# Rules
# Valid email must contain:
# @
# and
# .com
# If invalid:
# Raise:
# Invalid Email ❌
# If valid:
# Return:
# Email Verified ✅
# Example 1
# Enter Email: siva@gmail.com
# Email Verified ✅
# Example 2
# Enter Email: sivagmail.com
# Invalid Email ❌
# Example 3
# Enter Email: siva@yahoo
# Invalid Email ❌
# ⚠️ Conditions
# ✅ Create custom exception
# ✅ Use raise
# ✅ Use try-except
# ✅ Create separate validation function
# ❌ Don't use regex
# ❌ Don't use external libraries

class InvalidEmailError(Exception):
    pass

def validate_email(email):
    if "@" not in email:
        raise InvalidEmailError("Invalid Email ❌")
    elif ".com" not in email:
        raise InvalidEmailError("Invalid Email ❌")
    else:
        return "Email Verified ✅"
    
try:
    email = input("Enter Email: ")
    print(validate_email(email))
except InvalidEmailError as e:
    print(e)