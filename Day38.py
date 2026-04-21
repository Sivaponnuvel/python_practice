# 🔥 Question 1
# Write a Python program to:
# 👉 Take username from user
# 👉 If username length < 5 →
# raise error: "Username must be at least 5 characters"
# 👉 Otherwise print:
# "Valid username"
# 🧠 Example Output
# Valid username
# OR
# Error: Username must be at least 5 characters

try:
    username = input("Enter your name : ")
    if len(username) < 5:
        raise ValueError("Username must be at least 5 characters")
except ValueError as e:
    print(f"Error: {e}") 
else:
    print("Valid username")


# 🔥 Question 2
# Write a Python program to:
# 👉 Take password from user
# 👉 Conditions:
# If length < 6 → raise error "Password too short"
# If no digit → raise error "Password must contain a number"
# 👉 Otherwise print:
# "Strong password"
# 👉 Handle errors using try-except
# 🧠 Example Output
# Strong password
# OR
# Error: Password too short
# OR
# Error: Password must contain a number

try:
    password = input("Enter your password : ")
    if len(password) < 6 :
        raise ValueError("Password too short")
    if not any(i.isdigit() for i in password):
        raise ValueError("Password must contain a number")
except ValueError as e:
    print(f"Error: {e}")
else:
    print("Strong password")