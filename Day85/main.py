# 🔹 Question 1 – Exception Handling: Login System
# Write a Python program to:
# 👉 Create a custom exception:
# InvalidLoginError
# 👉 Create a function:
# login(username, password)
# Rules:
# ✅ Valid credentials:
# username = "admin"
# password = "1234"
# ✅ If username is incorrect:
# Raise:
# Invalid Username ❌
# ✅ If password is incorrect:
# Raise:
# Invalid Password ❌
# ✅ If both are correct:
# Print:
# Login Successful ✅
# 👉 Take username and password from user
# 👉 Handle exceptions using try-except
# Example Output
# Enter Username: admin
# Enter Password: 1234
# Login Successful ✅
# OR
# Enter Username: siva
# Enter Password: 1234
# Invalid Username ❌
# ⚠️ Conditions:
# ✅ Create custom exception class
# ✅ Use raise
# ✅ Use try-except

class InvalidLoginError(Exception):
    pass

def login(username, password):
    if username != "admin":
        raise InvalidLoginError("Invalid Username ❌")
    elif password != "1234":
        raise InvalidLoginError("Invalid Password ❌")
    
try:
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    login(username, password)
    print("Login Successful ✅")
except InvalidLoginError as e:
    print(e)


