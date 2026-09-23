# 🔹 Question 1 – Decorator: Login Validation
# Create a decorator called check_login that checks whether a user is logged in before allowing access to a dashboard.
# Requirements:
# Create a decorator check_login.
# Ask the user for login status: yes or no.
# If the status is yes, allow the function to execute.
# If the status is no, display an error message.
# Create a function dashboard(username).
# Use @check_login.
# Example:
# Enter login status (yes/no): yes
# Enter username: Siva
# Expected Output:
# Login successful ✅
# Welcome to dashboard, Siva
# If the user enters:
# Enter login status (yes/no): no
# Expected:
# Please login first ❌
# Conditions:
# Must use a decorator.
# Use *args in the wrapper.
# dashboard() should not execute when the user is not logged in.

def check_login(func):
    def wrapper(*args):
        status = input("Enter login status (yes/no): ").lower()
        if status == "yes":
            print("Login successful ✅")
            print(func(*args))
        else:
            print("Please login first ❌")
    return wrapper

@check_login
def dashboard(username):
    return f"Welcome to dashboard, {username}"

username = input("Enter username: ")
dashboard(username)


