# 🔹 Question 1 – Modules: Create a Utility Module
# Create your own Python module named number_utils.py.
# File 1: number_utils.py
# Create these three functions:
# is_even(number)
# is_prime(number)
# factorial(number)
# Function Requirements
# is_even(number)
# Return True if the number is even.
# Otherwise return False.
# is_prime(number)
# Return True if the number is prime.
# Otherwise return False.
# Use a loop to check the number.
# factorial(number)
# Calculate the factorial using a loop.
# Return the result.
# File 2: main.py
# Program Flow:
# Import your number_utils module.
# Take an integer from the user.
# Call all three functions.
# Display their results.
# Example
# Input
# Enter Number: 5
# Output
# Even      : False
# Prime     : True
# Factorial : 120
# ⚠️ Conditions
# ✅ Create your own module number_utils.py
# ✅ Create all three functions inside the module
# ✅ Import the module into main.py
# ✅ Use the functions from the module
# ✅ Take input from the user
# ✅ factorial() must use a loop
# ❌ Don't write the functions again inside main.py
# ❌ Don't import any external libraries

from number_utils import is_even, is_prime, factorial

number = int(input("Enter Number: "))
print(f"Even      : {is_even(number)}")
print(f"Prime     : {is_prime(number)}")
print(f"Factorial : {factorial(number)}")


# 🔹 Question 2 – Packages: Create and Use Your Own Package
# Create a Python package named operations.
# Your project structure should be:
# Day147/
# │
# ├── main.py
# │
# └── operations/
#     ├── __init__.py
#     └── calculator.py
# File: operations/calculator.py
# Create these functions:
# add(a, b)
# subtract(a, b)
# multiply(a, b)
# Each function should return its result.
# File: main.py
# Import the calculator module from the operations package.
# Take two integers from the user.
# Use the three functions.
# Display the results.
# Example
# Input
# Enter First Number: 20
# Enter Second Number: 5
# Output
# Addition       : 25
# Subtraction    : 15
# Multiplication : 100
# ⚠️ Conditions
# ✅ Create an operations package
# ✅ Create __init__.py
# ✅ Create calculator.py inside the package
# ✅ Define the three functions inside calculator.py
# ✅ Import calculator from the operations package
# ✅ Take input from the user
# ✅ Use the package functions
# ❌ Don't put the functions inside main.py
# ❌ Don't import any external libraries

from operations import calculator

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

print(f"Addition       : {calculator.add(a, b)}")
print(f"Subtraction    : {calculator.subtract(a, b)}")
print(f"Multiplication : {calculator.multiply(a, b)}")