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


