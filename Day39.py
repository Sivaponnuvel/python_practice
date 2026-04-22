# 🔥 Question 1
# Write a Python program to:
# 👉 Take username and password from user
# 👉 Validate:
# Username length must be at least 5
# Password length must be at least 6
# 👉 If invalid → print error and ask again using loop
# 👉 If valid → print:
# "Login Successful"

while True:
    try:
        username = input("Enter username: ")
        password = input("Enter your password: ")
        if len(username) < 5:
            raise ValueError("Username must be at least 5 characters")
        if len(password) < 6:
            raise ValueError("Password too short")
    except ValueError as e:
        print(f"Error: {e}")
        print("Try again...\n")
    else:
        print("Login Successful ✅")
        break


# 🔥 Question 2
# Write a Python program to:
# 👉 Take password from user
# 👉 Conditions:
# Must be at least 6 characters
# Must contain at least one number
# 👉 Give user only 3 attempts
# 👉 If all 3 attempts fail → print:
# "Account locked"
# 👉 If correct → print:
# "Access granted"

attempts = 3
while attempts > 0:
    try:
        password = input("Enter your password: ")
        if len(password) < 6:
            raise ValueError("Password too short")
        if not any(i.isdigit() for i in password):
            raise ValueError("Password  must contain a number")
    except ValueError as e:
        attempts -= 1
        print(f"Error: {e}")
        print(f"Attempts left: {attempts}\n")
    else:
        print("Access granted ✅")
        break
if attempts == 0:
    print("Account locked ❌")