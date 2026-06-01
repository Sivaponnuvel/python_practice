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


# 🔹 Question 2 – Exception Handling + File Logging
# Write a Python program to:
# 👉 Create a file:
# error_log.txt
# 👉 Take two numbers from user
# 👉 Perform division
# 👉 Rules:
# If division successful:
# Append into file:
# Division Successful
# If division by zero:
# Append into file:
# Cannot divide by zero
# If invalid number entered:
# Append into file:
# Invalid Number
# 👉 Use:
# try-except
# 👉 Finally print:
# Operation Logged ✅
# Example Output:
# Enter a: 10
# Enter b: 2
# Result: 5.0
# Operation Logged ✅
# OR
# Enter a: 10
# Enter b: 0
# Cannot divide by zero ❌
# Operation Logged ✅

file_path = "D:/Backend/Python/Own try/practice/Day78/error_log.txt"
try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    result = a / b
except ZeroDivisionError:
    print("Cannot divide by zero ❌")
    with open(file_path,"a") as file:
        file.write("Cannot divide by zero \n")
except ValueError:
    print("Invalid Number ❌")
    with open(file_path,"a") as file:
        file.write("Invalid Number \n")
else:
    print(f"Result: {result}")
    with open(file_path,"a") as file:
        file.write("Division Successful \n")
finally:
    print("Operation Logged ✅")