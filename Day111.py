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


# 🔹 Question 2 – Interview Question: Rotate a List by K Positions
# Write a Python program to rotate a list to the right by k positions.
# Example:
# Enter numbers:
# 1 2 3 4 5
# Enter K: 2
# Output:
# Rotated List:
# 4 5 1 2 3
# Example 2
# Input
# 10 20 30 40 50 60
# K = 4
# Output
# 30 40 50 60 10 20
# If k is greater than the list length
# Example
# List:
# 1 2 3 4 5
# K = 8
# Output
# 3 4 5 1 2
# (Hint: Think about using the remainder when dividing by the list length.)
# ⚠️ Conditions
# ✅ Take list input from the user
# ✅ Use list slicing
# ✅ Handle k > len(list)
# ❌ Don't rotate using loops
# ❌ Don't use collections.deque
# ❌ Don't use external libraries

numbers = list(map(int, input("Enter Numbers: ").split()))
k = int(input("Enter K: "))

k %= len(numbers)

rotated = numbers[-k:]+ numbers[:-k]
print("Rotated List:")
print(*rotated)