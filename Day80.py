# 🔹 Question 1 – Decorator + Function Arguments
# Write a Python program to:
# 👉 Create a decorator:
# log_function(func)
# 👉 Inside decorator:
# Before function call print:
# Function Execution Started
# After function call print:
# Function Execution Finished
# 👉 Create function:
# calculate_total(price, quantity)
# 👉 Function should return:
# price * quantity
# 👉 Apply decorator using:
# @log_function
# 👉 Take input from user
# 👉 Print final result
# Example Output:
# Enter Price: 100
# Enter Quantity: 5
# Function Execution Started
# Function Execution Finished
# Total Amount: 500
# ⚠️ Conditions:
# ✅ Decorator should work with arguments
# ✅ Function should return value

def log_function(func):
    def wrapper(price, quantity):
        print("Function Execution Started")
        result = func(price, quantity)
        print("Function Execution Finished")
        return result
    return wrapper

@log_function
def calculate_total(price, quantity):
    return price * quantity
price = int(input("Enter Price: "))
quantity = int(input("Enter Quantity: "))
print(f"Total Amount: {calculate_total(price, quantity)}")


