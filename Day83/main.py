# 🔹 Question 1 – Modules & Packages: Math Utility Package
# Create the following structure:
# Day83/
# │
# ├── main.py
# │
# └── utilities/
#     ├── __init__.py
#     └── math_utils.py
# Inside math_utils.py
# Create functions:
# square(number)
# cube(number)
# factorial(number)
# Rules
# ✅ square() → return square of number
# ✅ cube() → return cube of number
# ✅ factorial() → calculate factorial using loop
# ❌ Do not use recursion
# ❌ Do not use math.factorial()
# Inside main.py
# 👉 Import functions from package
# 👉 Take number from user
# 👉 Print:
# Enter Number: 5
# Square: 25
# Cube: 125
# Factorial: 120
# ⚠️ Conditions:
# ✅ Use custom package
# ✅ Use custom module
# ✅ Use imports properly

from utilities import math_utils

number = int(input("Enter Number: "))

print(f"Square: {math_utils.square(number)}")
print(f"Cube: {math_utils.cube(number)}")
print(f"Factorial: {math_utils.factorial(number)}")


