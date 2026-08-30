# 🔹 Question 1 – OOP: Employee Salary Calculator
# Write a Python program using a class to calculate an employee's final salary.
# Program Flow
# Create a class named Employee.
# The class should have:
# name
# basic_salary
# Create a method:
# calculate_salary()
# The method should calculate the final salary using:
# HRA = 20% of basic salary
# DA  = 10% of basic salary
# Final Salary = Basic Salary + HRA + DA
# Take the employee details from the user.
# Example
# Input:
# Enter Employee Name: Siva
# Enter Basic Salary: 25000
# Output:
# Employee Name: Siva
# Basic Salary: 25000.0
# HRA: 5000.0
# DA: 2500.0
# Final Salary: 32500.0
# Invalid Input
# If the user enters a non-numeric salary:
# Enter Basic Salary: abc
# Output:
# Invalid Salary ❌
# Please enter a valid number.
# ⚠️ Conditions
# ✅ Use a class
# ✅ Use __init__()
# ✅ Use self
# ✅ Create calculate_salary()
# ✅ Use input()
# ✅ Use try
# ✅ Use except ValueError
# ✅ Use floating-point calculation
# ❌ Don't calculate the salary outside the class
# ❌ Don't import any libraries

class Employee:
    def __init__(self, name, basic_salary):
        self.name = name
        self.basic_salary = basic_salary

    def calculate_salary(self):
        self.HRA = self.basic_salary * (20/100)
        self.DA = self.basic_salary * (10/100)
        print(f"HRA: {self.HRA}")
        print(f"DA: {self.DA}")
        print(f"Final Salary: {self.basic_salary + self.HRA + self.DA}")

try:
    name = input("Enter Employee Name: ")
    basic_salary = float(input("Enter Basic Salary: "))
    obj = Employee(name, basic_salary)
    print(f"Employee Name: {obj.name}")
    print(f"Basic Salary: {obj.basic_salary}")
    obj.calculate_salary()

except ValueError:
    print("Invalid Salary ❌")
    print("Please enter a valid number.")


# 🔹 Question 2 – Exception Handling: ATM Withdrawal
# Write a Python program to simulate a simple ATM withdrawal system.
# Program Flow
# Start with an initial balance:
# Balance = 10000
# Take the withdrawal amount from the user.
# Use exception handling to make sure the program doesn't crash when invalid input is entered.
# Example 1 – Successful Withdrawal
# Input:
# Enter Withdrawal Amount: 3000
# Output:
# Withdrawal Successful ✅
# Withdrawn Amount: 3000
# Remaining Balance: 7000
# Example 2 – Insufficient Balance
# Input:
# Enter Withdrawal Amount: 15000
# Output:
# Insufficient Balance ❌
# Available Balance: 10000
# Example 3 – Invalid Input
# Input:
# Enter Withdrawal Amount: abc
# Output:
# Invalid Input ❌
# Please enter a valid number.
# Example 4 – Invalid Amount
# Input:
# Enter Withdrawal Amount: -500
# Output:
# Invalid Withdrawal Amount ❌
# Amount must be greater than 0.
# ⚠️ Conditions
# ✅ Use input()
# ✅ Use try
# ✅ Use except ValueError
# ✅ Use if/elif/else
# ✅ Check insufficient balance
# ✅ Check negative/zero amount
# ❌ Don't use isdigit()
# ❌ Don't import any libraries
# ❌ Don't allow the balance to become negative

try:
    Balance = 10000
    amount = int(input("Enter Withdrawal Amount: "))
    if amount <= 0:
        print("Invalid Withdrawal Amount ❌")
        print("Amount must be greater than 0.")
    elif amount > Balance:
        print("Insufficient Balance ❌")
    else:
        print("Withdrawal Successful ✅")
        print(f"Withdrawn Amount: {amount}")
        print(f"Remaining Balance: {Balance - amount}")

except ValueError:
    print("Invalid Input ❌")
    print("Please enter a valid number.")