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


