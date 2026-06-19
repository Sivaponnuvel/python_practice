# 🔹 Question 1 – Modules: Password Utility System
# Create 2 files:
# password_utils.py
# Create functions:
# is_strong_password(password)
# mask_password(password)
# Rules
# ✅ is_strong_password(password)
# Return True if:
# Length ≥ 8
# Contains at least one digit
# Otherwise return False
# ✅ mask_password(password)
# Convert:
# mypassword123
# to:
# ***********123
# Only last 3 characters should be visible.
# main.py
# 👉 Import functions from module
# 👉 Take password from user
# 👉 Check strength
# 👉 Print masked password
# Example Output
# Enter Password: mypassword123
# Strong Password ✅
# Masked Password: ***********123
# OR
# Enter Password: abc
# Weak Password ❌
# Masked Password: ***
# Conditions
# ✅ Use custom module
# ✅ Use functions
# ❌ Don't use regex
# ❌ Don't use external libraries

import password_utils as p

password = input("Enter Password: ")

if p.is_strong_password(password):
    print("Strong Password ✅")
else:
    print("Weak Password ❌")

print(f"Masked Password: {p.mask_password(password)}")


# 🔹 Question 2 – Decorator with Arguments
# Create a decorator:
# repeat(times)
# This decorator should accept a number.
# Create function:
# greet(name)
# Print:
# Hello Siva
# Apply decorator:
# @repeat(3)
# def greet(name):
#     ...
# Example Output
# Enter Name: Siva
# Hello Siva
# Hello Siva
# Hello Siva
# Conditions
# ✅ Decorator should accept arguments
# ✅ Function should accept arguments
# ✅ Use nested functions properly
# ❌ Don't use global variables

def repeat(times):
    def decorator(func):
        def wrapper(name):
            for _ in range(times):
                func(name)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello {name}")

name = input("Enter Name: ")
greet(name)