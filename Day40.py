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


