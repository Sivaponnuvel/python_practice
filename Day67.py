# 🔹 Question 1 – Basic Decorator Practice
# Write a Python program to:
# 👉 Create a decorator function:
# display_message(func)
# 👉 Inside decorator:
# Before calling function print:
# Function Started
# After calling function print:
# Function Ended
# 👉 Create another function:
# hello()
# 👉 Inside hello() print:
# Hello Python
# 👉 Apply decorator using:
# @display_message
# Example Output:
# Function Started
# Hello Python
# Function Ended

def display_message(func):
    def wrapper():
        print("Function Started")
        func()
        print("Function Ended")
    return wrapper

@display_message
def hello():
    print("Hello python")

hello()


