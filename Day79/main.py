# 🔹 Question 1 – OOP + JSON Employee Record System
# Write a Python program to:
# 👉 Create a class:
# Employee
# 👉 Constructor should take:
# emp_id
# name
# department
# 👉 Create method:
# to_dict()
# 👉 Return employee data as dictionary
# Example:
# {
#     "id": 101,
#     "name": "Siva",
#     "department": "IT"
# }
# 👉 Take details for 3 employees
# 👉 Create Employee objects
# 👉 Store all employee records into:
# employees.json
# 👉 Use:
# json.dump()
# 👉 After saving, read the file and display all employee records
# Example Output:
# Employee Records:
# ID: 101
# Name: Siva
# Department: IT
# ID: 102
# Name: Ram
# Department: HR
# ⚠️ Conditions:
# ✅ Use OOP
# ✅ Use JSON
# ✅ Use File Handling

import json
class Employee:
    def __init__(self, emp_id, name, department):
        self.__emp_id = emp_id
        self.__name = name
        self.__department = department
    def to_dict(self):
        return {"id": self.__emp_id, "name": self.__name, "department": self.__department}
employees = []
for i in range(3):
    emp_id = int(input("Enter Id: "))
    name = input("Enter Name: ")
    department = input("Enter Department: ")
    emp = Employee(emp_id, name, department)
    employees.append(emp.to_dict())
with open("D:/Backend/Python/Own try/practice/Day79/employees.json", "w") as file:
    json.dump(employees, file, indent = 4)
with open("D:/Backend/Python/Own try/practice/Day79/employees.json", "r") as file:
    read = json.load(file)
print("Employee Records:")
for i in read:
    print(f"ID: {i['id']}")
    print(f"Name: {i['name']}")
    print(f"Department: {i['department']}")


# 🔹 Question 2 – Custom Exception + Modules
# Write a Python program using custom modules.
# 👉 Create file:
# bank_utils.py
# 👉 Create custom exception:
# InvalidAmountError
# 👉 Create function:
# withdraw(balance, amount)
# Rules:
# ✅ If amount <= 0
# Raise:
# InvalidAmountError
# ✅ If amount > balance
# Print:
# Insufficient Balance ❌
# ✅ Otherwise return remaining balance
# 👉 Create another file:
# main.py
# 👉 Import from module
# 👉 Take:
# balance
# withdraw amount
# 👉 Handle exception using:
# try-except
# Example Output:
# Enter Balance: 5000
# Enter Amount: 2000
# Remaining Balance: 3000
# OR
# Enter Balance: 5000
# Enter Amount: -100
# Invalid Amount ❌
# OR
# Enter Balance: 5000
# Enter Amount: 7000
# Insufficient Balance ❌

import bank_utils as b

try:
    balance = int(input("Enter Balance: "))
    amount = int(input("Enter Amount: "))
    result = b.withdraw(balance, amount)
    if result is not None:
        print(f"Remaining Balance: {result}")
except b.InvalidAmountError as e:
    print(e)