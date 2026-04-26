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


# 🔹 Question 2
# Write a Python program to:
# 👉 Create a package named auth
# Inside create:
# login.py
# validator.py
# In validator.py:
# Create functions:
# validate_username(username)
# length ≥ 5 இல்லனா error
# validate_password(password)
# length ≥ 6
# must contain number
# In login.py:
# Create function:
# login(username, password)
# Call validation functions
# If valid → return "Login Success"
# Else → raise error
# 👉 In main.py:
# Take username & password
# Call login()
# Handle errors
# Print result

from auth import login
try:
    username = input("Enter username: ")
    password = input("Enter password: ")
    result = login.login(username,password)
    print(result)
except ValueError as e:
    print(e)