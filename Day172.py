# 🔹 Question 1 – Decorator: Execution Time Message
# Write a Python program using a decorator to display messages before and after a function executes.
# Create a decorator:
# log_execution
# Apply it to a function:
# greet(name)
# Program Flow
# Take the user's name as input.
# When greet() is called, the decorator should display:
# Function execution started
# Hello, Siva!
# Function execution completed
# Example
# Input:
# Enter your name: Siva
# Output:
# Function execution started
# Hello, Siva!
# Function execution completed
# ⚠️ Conditions
# ✅ Create a decorator function
# ✅ Create a wrapper function
# ✅ Use @log_execution
# ✅ Use *args
# ✅ Call the original function inside the wrapper
# ✅ Use input()
# ❌ Don't manually print the decorator messages inside greet()
# ❌ Don't use any libraries

def log_execution(func):
    def wrapper(*args):
        print("Function execution started")
        func(*args)
        print("Function execution completed")
    return wrapper

@log_execution
def greet(name):
    print(f"Hello, {name}!")

name = input("Enter your name: ")
greet(name)


