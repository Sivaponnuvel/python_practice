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


