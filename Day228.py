# 🔹 Question 1 – Decorator Coding Problem
# Topic: Functions, Decorators, Nested Functions and *args, **kwargs
# Write a Python program to create a decorator that checks whether a user is logged in before allowing access to a function.
# Example 1:
# @login_requireddef view_dashboard(username):    print(f"Welcome to Dashboard, {username}")view_dashboard("Arun", is_logged_in=True)
# Expected output:
# Welcome to Dashboard, Arun
# Example 2:
# view_dashboard("Arun", is_logged_in=False)
# Expected output:
# Access Denied: Please login first
# Requirements
# 1. Create a decorator named login_required.
# 2. Create a nested function named wrapper.
# 3. Use *args and **kwargs in the wrapper.
# 4. Check the is_logged_in keyword argument.
# 5. If is_logged_in is True, execute the original function.
# 6. If is_logged_in is False, display Access Denied: Please login first.
# 7. Create a function named view_dashboard(username) and apply the decorator.
# 8. Test the function with both logged-in and logged-out users.
# Conditions
# - Use the @login_required decorator syntax.
# - Use nested functions.
# - Use *args and **kwargs.
# - Treat a missing is_logged_in argument as False.
# - The original view_dashboard() function must accept only username.
# - Do not import libraries.
# - Do not hardcode the entire output outside the functions.

def login_required(func):
    def wrapper(*args, **kwargs):
        is_logged_in = kwargs.get("is_logged_in", False)

        if is_logged_in:
            return func(*args)
        else:
            print("Access Denied: Please login first")

    return wrapper

@login_required
def view_dashboard(username):
    print(f"Welcome to Dashboard, {username}")

view_dashboard("Arun", is_logged_in=True)
view_dashboard("Arun", is_logged_in=False)


