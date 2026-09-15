# 🔹 Question 1 – Module + Class + return
# Create a module named:
# employee.py
# Inside the module, create a class:
# Employee
# The class should have:
# name
# salary
# Create a method:
# get_details()
# The method should return the employee's details.
# Then create:
# main.py
# Import the Employee class and create an object.
# Program Flow
# Input:
# Enter employee name: Siva
# Enter salary: 25000
# Expected Output:
# Employee Name: Siva
# Salary: 25000
# ⚠️ Conditions
# ✅ Create employee.py
# ✅ Create Employee class
# ✅ Use __init__()
# ✅ Store name and salary
# ✅ Create get_details()
# ✅ Use return inside get_details()
# ✅ Import Employee into main.py
# ✅ Create an object
# ✅ Use input()
# ❌ Don't print employee details inside get_details()
# ❌ Don't create the class directly inside main.py
# ❌ Don't use libraries
# 💡 Interview focus: Understand the difference between:
# return
# and
# print()

from employee import Employee

name = input("Enter employee name: ")
salary = int(input("Enter salary: "))

obj = Employee(name, salary)
print(obj.get_details())


