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


# 🔹 Question 2 – Set Coding Problem
# Topic: Sets, Loops and Conditional Statements
# Write a Python program to find the common unique elements between three lists using sets.
# Example 1:
# list1 = [10, 20, 30, 40, 50]list2 = [20, 30, 50, 60, 70]list3 = [10, 20, 30, 50, 80]
# Expected output:
# Common Elements: [20, 30, 50]
# Example 2:
# list1 = [1, 2, 3, 4]list2 = [5, 6, 7]list3 = [8, 9, 10]
# Expected output:
# Common Elements: []
# Requirements
# 1. Create the three lists shown in Example 1.
# 2. Convert the lists into sets.
# 3. Find elements that exist in all three sets.
# 4. Display each common element only once.
# 5. Display the final result as a sorted list.
# 6. Your solution should work when the list values change.
# Conditions
# - Must use set().
# - Must use set intersection.
# - You may use sorted() for the final output.
# - Do not use nested loops to compare list elements.
# - Do not import external libraries.
# - Do not hardcode the output.
# - Handle the case where no common elements exist.

list1 = [10, 20, 30, 40, 50]
list2 = [20, 30, 50, 60, 70]
list3 = [10, 20, 30, 50, 80]

set1 = set(list1)
set2 = set(list2)
set3 = set(list3)

common = set1.intersection(set2, set3)

print(f"Common Elements: {sorted(common)}")