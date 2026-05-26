# 🔹 Question 1 – Access Role Decorator
# Write a Python program to:
# 👉 Create a decorator:
# admin_only(func)
# 👉 Inside decorator:
# Take role from user
# Rules:
# If role is not "admin":
# Only admin can access ❌
# Otherwise call original function
# 👉 Create function:
# delete_user()
# 👉 Inside function print:
# User Deleted Successfully ✅
# 👉 Apply decorator using:
# @admin_only
# Example Output:
# Enter role: admin
# User Deleted Successfully ✅
# OR
# Enter role: user
# Only admin can access ❌

def admin_only(func):
    def wrapper():
        role = input("Enter role: ")
        if role == "admin":
            return func()
        else:
            print("Only admin can access ❌")
    return wrapper

@admin_only
def delete_user():
    print("User Deleted Successfully ✅")
delete_user()


# 🔹 Question 2 – Decorator Chain Practice
# Write a Python program to:
# 👉 Create 2 decorators:
# star_decorator(func)
# hash_decorator(func)
# 👉 star_decorator should print:
# **********
# before and after function execution
# 👉 hash_decorator should print:
# ##########
# before and after function execution
# 👉 Create function:
# show_message()
# 👉 Inside function print:
# Decorator Chaining
# 👉 Apply both decorators
# Example Output:
# **********
# ##########
# Decorator Chaining
# ##########
# **********

def star_decorator(func):
    def wrapper():
        print("**********")
        func()
        print("**********")
    return wrapper
def hash_decorator(func):
    def wrapper():
        print("##########")
        func()
        print("##########")
    return wrapper

@star_decorator
@hash_decorator
def show_message():
    print("Decorator Chaining")
show_message()