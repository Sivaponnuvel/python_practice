# 🔹 Question 1 – Decorator: Login Attempt Tracker
# Write a Python program to:
# 👉 Create a decorator:
# track_login
# 👉 Every time the decorated function is called:
# Print:
# Login Attempt #1
# then
# Login Attempt #2
# and so on...
# Create function:
# login(username, password)
# Rules:
# If username == "admin" and password == "1234"
# Print:
# Login Successful ✅
# Otherwise print:
# Invalid Credentials ❌
# Apply decorator:
# @track_login
# def login(username, password):
#     ...
# Program Flow
# Take username and password from user.
# Call the function 3 times using the same inputs.
# Example Output
# Enter Username: admin
# Enter Password: 1234
# Login Attempt #1
# Login Successful ✅
# Login Attempt #2
# Login Successful ✅
# Login Attempt #3
# Login Successful ✅
# Example Output 2
# Enter Username: siva
# Enter Password: 1111
# Login Attempt #1
# Invalid Credentials ❌
# Login Attempt #2
# Invalid Credentials ❌
# Login Attempt #3
# Invalid Credentials ❌
# ⚠️ Conditions
# ✅ Decorator must work with function arguments
# ✅ Use a closure variable to store attempt count
# ❌ Don't use global variables
# ❌ Don't use classes

def track_login(func):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Login Attempt #{count}")
        return func(*args, **kwargs)
    return wrapper

@track_login
def login(username, password):
    if username == "admin" and password == "1234":
        print("Login Successful ✅")
    else:
        print("Invalid Credentials ❌")

username = input("Enter Username: ")
password = input("Enter Password: ")
for _ in range(3):
    login(username, password)


