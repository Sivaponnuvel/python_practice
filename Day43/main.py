# 🔹 Question 1
# Write a Python program to:
# 👉 Create a module named bank.py
# 👉 Inside create a class BankAccount
# Class details:
# private variable: __balance
# constructor → initial balance
# Methods:
# deposit(amount)
# withdraw(amount)
# get_balance()
# Rules:
# If withdraw > balance → raise error
# If deposit <= 0 → raise error
# 👉 In another file main.py:
# Import the module
# Create object
# Take user input (deposit & withdraw)
# Handle errors using try-except
# Print final balance

import bank as b
obj = b.BankAccount(1000)
try:
    deposit = int(input("Enter your deposit amount: "))
    print(obj.deposit(deposit))
    withdraw = int(input("Enter your withdraw amount: "))
    print(obj.withdraw(withdraw))
except ValueError as e:
    print(e)
else:
    print(f"Final Balance : {obj.get_balance()}")


