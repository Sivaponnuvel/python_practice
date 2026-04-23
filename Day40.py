# 🔥 Question 1
# Write a Python program to:
# 👉 Create a function validate_username(username)
# 👉 Conditions:
# Length must be at least 5
# 👉 If invalid → raise error
# 👉 If valid → return True
# 👉 Take username from user
# 👉 Call the function
# 👉 Handle error using try-except
# 👉 Print:
# "Valid username"
# OR error message

def validate_username(username):
    if len(username) < 5:
        raise ValueError("Invalid username: must be at least 5 characters")
    return True
username = input("Enter your name : ")
try:
    if validate_username(username):
        print("Valid username")
except ValueError as e:
    print(e)


# 🔥 Question 2
# Write a Python program to:
# 👉 Create a function validate_password(password)
# 👉 Conditions:
# Must be at least 6 characters
# Must contain at least one number
# 👉 If invalid → raise error
# 👉 If valid → return True
# 👉 Give user 3 attempts
# 👉 Use loop + try-except
# 👉 If valid → print:
# "Access granted"
# 👉 If 3 attempts fail → print:
# "Account locked"

def validate_password(password):
    if len(password) < 6:
        raise ValueError("Password too short")
    if not any(i.isdigit() for i in password):
        raise ValueError("Password must contain a number")
    return True
attempts = 3
while attempts > 0:
    password = input("Enter password : ")
    try:
        if validate_password(password):
            print("Access granted ✅")
            break
    except ValueError as e:
        attempts -= 1
        print(f"Error: {e}")
        print(f"Attempts left: {attempts}\n")
if attempts == 0:
    print("Account locked ❌")