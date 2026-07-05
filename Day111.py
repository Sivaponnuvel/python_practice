# 🔹 Question 1 – Decorator: Access Permission Checker
# Create a decorator:
# check_access
# It should check whether the user has permission before executing a function.
# Rules
# The decorator should receive the function arguments.
# Create the function:
# delete_file(username, is_admin)
# If is_admin is True:
# Access Granted ✅
# File Deleted Successfully
# Otherwise:
# Access Denied ❌
# The original function should execute only if access is granted.
# Program Flow
# Example 1
# Enter Username: Siva
# Is Admin (yes/no): yes
# Output:
# Access Granted ✅
# File Deleted Successfully
# Example 2
# Enter Username: Ram
# Is Admin (yes/no): no
# Output:
# Access Denied ❌
# ⚠️ Conditions
# ✅ Use a decorator
# ✅ Pass function arguments through the decorator
# ✅ Call the original function only when access is allowed
# ❌ Don't use global variables
# ❌ Don't check permission inside delete_file()

def check_access(func):
    def wrapper(username, is_admin):
        if is_admin:
            print("Access Granted ✅")
            func(username, is_admin)
        else:
            print("Access Denied ❌")
    return wrapper

@check_access
def delete_file(username, is_admin):
    print("File Deleted Successfully")

username = input("Enter Username: ")
admin = input("Is Admin (yes/no): ").lower()

is_admin = admin == "yes"

delete_file(username, is_admin)


