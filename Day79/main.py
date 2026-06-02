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


