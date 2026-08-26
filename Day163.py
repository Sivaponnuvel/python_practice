# 🔹 Question 1 – OOP: Class Method and Static Method
# Create a class named Employee.
# Program Flow
# Create a class variable:
# company = "SS Tech"
# Create a constructor __init__() with:
# name
# salary
# Create a class method:
# change_company(cls, new_company)
# This method should update the class variable company.
# Create a static method:
# is_valid_salary(salary)
# It should:
# Return True if salary is greater than 0
# Return False otherwise
# Input
# Enter Employee Name: Siva
# Enter Salary: 30000
# Enter New Company Name: SVS Technologies
# Expected Output
# Employee Details
# Name    : Siva
# Salary  : 30000
# Company : SS Tech
# Salary Valid : True
# After Company Update
# Company : SVS Technologies
# ⚠️ Conditions
# ✅ Use a class variable
# ✅ Use @classmethod
# ✅ Use @staticmethod
# ✅ Use cls inside the class method
# ✅ Take input from the user
# ❌ Don't update the company directly outside the class
# ❌ Don't create a separate class for validation
# 💡 Hint
# @classmethod
# def change_company(cls, new_company):
#     cls.company = new_company

class Employee:
    company = "SS Tech"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

    @staticmethod
    def is_valid_salary(salary):
        return salary > 0


try:
    name = input("Enter Employee Name: ")
    salary = int(input("Enter Salary: "))
    new_company = input("Enter New Company Name: ")

    emp = Employee(name, salary)

    print("Employee Details")
    print(f"Name    : {emp.name}")
    print(f"Salary  : {emp.salary}")
    print(f"Company : {Employee.company}")
    print(f"Salary Valid : {Employee.is_valid_salary(emp.salary)}")

    emp.change_company(new_company)

    print("After Company Update")
    print(f"Company : {Employee.company}")

except ValueError:
    print("Invalid Salary ❌")


