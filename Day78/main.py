# 🔹 Question 1 – Employee Data Analyzer (Functions + Dictionary)
# Write a Python program to
# 👉 Take details for 5 employees:
# name
# salary
# 👉 Store them inside a list of dictionaries
# Example:
# [
#     {"name": "Siva", "salary": 25000},
#     {"name": "Ram", "salary": 30000}
# ]
# 👉 Create functions:
# view_employees(employees)
# highest_salary(employees)
# salary_above_25000(employees)
# 👉 Function Details:
# ✅ view_employees()
# Print all employee details
# ✅ highest_salary()
# Find employee with highest salary manually
# ❌ Do not use max()
# ✅ salary_above_25000()
# Print employees whose salary is greater than 25000
# Example Output:
# All Employees:
# Siva - 25000
# Ram - 30000
# Highest Salary:
# Ram - 30000
# Employees Above 25000:
# Ram - 30000
# ⚠️ Conditions:
# ✅ Use loops
# ✅ Use functions
# ❌ Do not use max()

def view_employees(employees):
    print("All Employees:")
    for i in employees:
        print(f"{i['name']} - {i['salary']}")
def highest_salary(employees):
    print("Highest Salary:")
    high_salary = employees[0]
    for i in employees:
        if high_salary['salary'] < i['salary']:
            high_salary = i
    print(f"{high_salary['name']} - {high_salary['salary']}")
def salary_above_25000(employees):
    print("Employees Above 25000:")
    found = False
    for i in employees:
        if 25000 < i['salary']:
            print(f"{i['name']} - {i['salary']}")
            found = True
    if not found:
        print("No employees above 25000")

employees = []
for i in range(5):
    name = input("Enter Name: ")
    salary = int(input("Enter Salary: "))
    employee = {"name": name, "salary": salary}
    employees.append(employee)

view_employees(employees)
highest_salary(employees)
salary_above_25000(employees)


