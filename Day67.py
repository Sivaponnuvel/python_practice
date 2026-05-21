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


# 🔹 Question 2 – Login Validation Decorator
# Write a Python program to:
# 👉 Create a decorator:
# login_required(func)
# 👉 Inside decorator:
# Take username from user
# Rules:
# If username is not "admin":
# Access Denied ❌
# Otherwise call original function
# 👉 Create function:
# dashboard()
# 👉 Inside dashboard() print:
# Welcome to Dashboard ✅
# 👉 Apply decorator using:
# @login_required
# Example Output:
# Enter username: admin
# Welcome to Dashboard ✅
# OR
# Enter username: siva
# Access Denied ❌

def login_required(func):
    def wrapper():
        username = input("Enter Username: ")
        if username != "admin":
            print("Access Denied ❌")
        else:
            func()
    return wrapper

@login_required
def dashboard():
    print("Welcome to Dashboard ✅")

dashboard()