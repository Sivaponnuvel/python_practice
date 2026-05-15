# 🔹 Question 1 – User Management System
# Write a Python program to:
# 👉 Create an empty list:
# users = []
# 👉 Create 3 functions:
# add_user(users, name, age)
# view_users(users)
# find_user(users, search_name)
# 👉 Function Details:
# ✅ add_user(users, name, age)
# Store user as dictionary inside list
# Example:
# {"name": "Siva", "age": 23}
# ✅ view_users(users)
# Print all users like:
# Siva - 23
# Ram - 21
# ✅ find_user(users, search_name)
# Search user by name
# If found → print user details
# Otherwise:
# User not found ❌
# 👉 Take details for 3 users from user input
# 👉 Call all functions properly
# Example Output:
# All Users:
# Siva - 23
# Ram - 21
# Search User: Siva
# Name: Siva
# Age: 23

users = []
# add user
def add_user(users, name, age):
    user = {"name": name, "age": age}
    users.append(user)
# view user
def view_users(users):
    print("All Users:")
    for user in users:
        print(f"{user['name']} - {user['age']}")
# find user
def find_user(users, search_name):
    for user in users:
        if user['name'].lower() == search_name.lower():
            print(f"Name: {user['name']}")
            print(f"Age: {user['age']}")
            return
    print("User not found ❌")
    
for i in range(3):
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    add_user(users,name,age)
view_users(users)
search_name = input("Search User: ")
find_user(users,search_name)


# 🔹 Question 2 – Advanced Password Validation
# Write a Python program to:
# 👉 Create a function:
# validate_password(password)
# Rules:
# password length should be greater than or equal to 8
# password should contain at least one number
# 👉 If invalid:
# raise ValueError
# 👉 Otherwise return:
# {"password": password}
# 👉 Take password from user
# 👉 Handle errors using try-except
# Example Output:
# Enter password: siva1234
# {'password': 'siva1234'}
# OR
# Error: Password must contain at least one number ❌

def validate_password(password):
    if len(password) < 8:
        raise ValueError("Password too short")
    elif not any(i.isdigit() for i in password):
        raise ValueError("Password must contain at least one number ❌")
    return {'password': password}
try:
    password = input("Enter your password: ")
    print(validate_password(password))
except ValueError as e:
    print(f"Error: {e}")