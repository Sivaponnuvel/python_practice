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


