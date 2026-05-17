# 🔹 Question 1 – Mini Employee Management System
# Write a Python program to:
# 👉 Create an empty list:
# employees = []
# 👉 Create 4 functions:
# add_employee(employees, emp_id, name, salary)
# view_employees(employees)
# search_employee(employees, search_id)
# highest_salary(employees)
# 👉 Function Details:
# ✅ add_employee()
# Store employee as dictionary inside list
# Example:
# {
#     "id": 101,
#     "name": "Siva",
#     "salary": 25000
# }
# ✅ view_employees()
# Print all employee details
# ✅ search_employee()
# Search employee using employee id
# If found → print employee details
# Otherwise:
# Employee not found ❌
# ✅ highest_salary()
# Find employee with highest salary
# Print employee name and salary
# 👉 Take details for 3 employees from user input
# 👉 Call all functions properly
# Example Output:
# All Employees:
# ID: 101, Name: Siva, Salary: 45000
# ID: 102, Name: Ram, Salary: 30000
# ID: 103, Name: Arun, Salary: 25000
# Employee Found:
# ID: 102, Name: Ram, Salary: 30000
# Highest Salary:
# Siva - 45000

employees = []
# add employee
def add_employee(employees, emp_id, name, salary):
    employee = {"id": emp_id, "name": name, "salary": salary}
    employees.append(employee)
# view employee
def view_employees(employees):
    print("All Employees: ")
    for i in employees:
        print(f"ID: {i['id']}, Name: {i['name']}, Salary: {i['salary']}")
# found the employee
def search_employee(employees, search_id):
    for i in employees:
        if i['id'] == search_id:
            print("Employee Found:")
            print(f"ID: {i['id']}, Name: {i['name']}, Salary: {i['salary']}")
            return
    print("Employee not found ❌")
# Find the Highest Salary
def highest_salary(employees):
    print("Highest Salary:")
    high_salary = employees[0]
    for i in employees:
        if i['salary'] > high_salary['salary']:
            high_salary = i
    print(f"{high_salary['name']} - {high_salary['salary']}")

for i in range(3):
    emp_id = int(input("Enter Employee Id: "))
    name = input("Enter Employee Name: ")
    salary = int(input("Enter Employee salary: "))
    add_employee(employees,emp_id,name,salary)

view_employees(employees)
search_id = int(input("Enter Employee Id: "))
search_employee(employees,search_id)
highest_salary(employees)


