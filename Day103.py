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


# 🔹 Question 2 – Lambda Functions: Product Price Sorting
# Write a Python program to:
# Create the following list:
# products = [
#     ("Laptop", 55000),
#     ("Mouse", 700),
#     ("Keyboard", 1500),
#     ("Monitor", 12000),
#     ("Headset", 2500)
# ]
# Display a menu:
# 1. Sort Price (Low to High)
# 2. Sort Price (High to Low)
# Take choice from user.
# If user enters:
# 1
# Sort using:
# lambda
# Output:
# Products Sorted (Low to High)
# Mouse - 700
# Keyboard - 1500
# Headset - 2500
# Monitor - 12000
# Laptop - 55000
# If user enters:
# 2
# Output:
# Products Sorted (High to Low)
# Laptop - 55000
# Monitor - 12000
# Headset - 2500
# Keyboard - 1500
# Mouse - 700
# If user enters any other value:
# Invalid Choice ❌
# ⚠️ Conditions
# ✅ Use sorted()
# ✅ Use lambda
# ✅ Don't create a separate sorting function
# ✅ Display results using a loop
# ❌ Don't use list.sort()
# ❌ Don't manually compare prices using loops

products = [
    ("Laptop", 55000),
    ("Mouse", 700),
    ("Keyboard", 1500),
    ("Monitor", 12000),
    ("Headset", 2500)
]

print("1. Sort Price (Low to High)")
print("2. Sort Price (High to Low)")

choice = int(input("Enter your choice: "))

if choice == 1:
    sorted_products = sorted(products, key=lambda product: product[1])
    print("Products Sorted (Low to High)")
    for name, price in sorted_products:
        print(f"{name} - {price}")
elif choice == 2:
    sorted_products = sorted(products, key=lambda product: product[1], reverse=True)
    print("Products Sorted (High to Low)")
    for name, price in sorted_products:
        print(f"{name} - {price}")
else:
    print("Invalid Choice ❌")