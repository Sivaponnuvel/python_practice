# 🔹 Question 1 – Decorator: Authentication Check
# Write a Python program using a decorator to check whether a user is logged in before allowing a function to execute.
# Create a decorator:
# check_login
# Apply it to:
# dashboard(username)
# Program Flow
# Take the login status from the user.
# Input:
# Enter username: Siva
# Enter login status (yes/no): yes
# Output:
# Login successful ✅
# Welcome to Dashboard, Siva
# If the user is not logged in:
# Input:
# Enter username: Siva
# Enter login status (yes/no): no
# Output:
# Please login first ❌
# ⚠️ Conditions
# ✅ Create a decorator function
# ✅ Create a wrapper function
# ✅ Use @check_login
# ✅ Use *args
# ✅ Check login status inside the decorator
# ✅ Call dashboard() only when logged in
# ❌ Don't put the login-checking logic inside dashboard()
# ❌ Don't use any libraries

def check_login(func):
    def wrapper(*args):
        status = input("Enter login status (yes/no): ").lower()
        if status == "yes":
            print("Login successful ✅")
            return func(*args)
        else:
            print("Please login first ❌")
    return wrapper
        
@check_login
def dashboard(username):
    print(f"Welcome to Dashboard, {username}")
    
username = input("Enter username: ")
dashboard(username)


