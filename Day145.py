# 🔹 Question 1 – Decorators: Measure Function Execution
# Write a Python program to create a decorator that displays messages before and after a function executes and returns the function's result.
# Program Flow
# Create a decorator named execution_logger.
# Before executing the function, display:
# Executing Function...
# After executing the function, display:
# Function Executed Successfully
# The decorator should return the original function's result.
# Create a function named add(a, b) that returns the sum of two numbers.
# Apply the decorator using @execution_logger.
# Take two integers from the user.
# Display the returned result.
# Example
# Input
# Enter First Number: 10
# Enter Second Number: 20
# Output
# uting Function.Exec..
# Function Executed Successfully
# Result: 30
# ⚠️ Conditions
# ✅ Create a decorator
# ✅ Use an inner wrapper(*args, **kwargs)
# ✅ Return the original function's result
# ✅ Use @execution_logger
# ❌ Don't modify the add() function except by decorating it
# ❌ Don't print the result inside the decorator

def execution_logger(func):
    def wrapper(*args, **kwargs):
        print("Executing Function...")
        result = func(*args, **kwargs)
        print("Function Executed Successfully")
        return result
    return wrapper

@execution_logger
def add(a, b):
    return a + b

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
print(f"Result: {add(a, b)}")


