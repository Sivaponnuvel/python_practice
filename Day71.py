# 🔹 Question 1 – Authentication Decorator with Multiple Users
# Write a Python program to:
# 👉 Create a dictionary:
# users = {
#     "admin": "1234",
#     "siva": "pass",
#     "vijay": "hello"
# }
# 👉 Create a decorator:
# login_required(func)
# 👉 Inside decorator:
# Take username and password from user
# Rules:
# If username exists AND password matches → call original function
# Otherwise print:
# Invalid Credentials ❌
# 👉 Create function:
# profile()
# 👉 Inside function print:
# Login Successful ✅
# Welcome to Profile
# 👉 Apply decorator using:
# @login_required
# Example Output:
# Enter username: admin
# Enter password: 1234
# Login Successful ✅
# Welcome to Profile

users = {"admin": "1234", "siva": "pass", "vijay": "hello"}
def login_required(func):
    def wrapper():
        username = input("Enter username: ")
        password = input("Enter password: ")        
        if username in users and users[username] == password:
            return func()
        else:
            print("Invalid Credentials ❌")
    return wrapper

@login_required
def profile():
    print("Login Successful ✅")
    print("Welcome to Profile")
profile()


# 🔹 Question 2 – Result Modify Decorator
# Write a Python program to:
# 👉 Create a decorator:
# double_result(func)
# 👉 Inside decorator:
# Multiply returned value by 2
# 👉 Create function:
# get_number()
# 👉 Function should return a number from user input
# 👉 Apply decorator using:
# @double_result
# 👉 Print final result
# Example Output:
# Enter number: 10
# Final Result: 20

def double_result(func):
    def wrapper():
        print(f"Final Result: {func() * 2}")
    return wrapper

@double_result
def get_number():
    user = int(input("Enter the number: "))
    return user
get_number()