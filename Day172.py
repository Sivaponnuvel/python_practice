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


# 🔹 Question 2 – Exception Handling: Safe Calculator
# Write a Python program to create a simple calculator that performs:
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# Program Flow
# Take two numbers from the user:
# Enter first number: 20
# Enter second number: 5
# Then display:
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# Enter your choice: 4
# Expected Output
# Result: 4.0
# Handle These Errors
# Invalid number:
# Enter first number: abc
# Output:
# Invalid Input ❌
# Please enter numbers only.
# Division by zero:
# Enter first number: 20
# Enter second number: 0
# Enter your choice: 4
# Output:
# Cannot divide by zero ❌
# Invalid choice:
# Enter your choice: 7
# Output:
# Invalid Choice ❌
# Please select 1-4.
# ⚠️ Conditions
# ✅ Use input()
# ✅ Use try
# ✅ Use except ValueError
# ✅ Handle ZeroDivisionError
# ✅ Use if/elif/else
# ✅ Perform all four operations
# ❌ Don't use eval()
# ❌ Don't import any libraries
# ❌ Don't let the program crash


try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print(f"Result: {num1 + num2}")
    elif choice == 2:
        print(f"Result: {num1 - num2}")
    elif choice == 3:
       print(f"Result: {num1 * num2}")
    elif choice == 4:
        print(f"Result: {num1 / num2}")
    else:
        print("Invalid Choice ❌")
        print("Please select 1-4.")

except ValueError:
    print("Invalid Input ❌")
    print("Please enter numbers only.")

except ZeroDivisionError:
    print("Cannot divide by zero ❌")