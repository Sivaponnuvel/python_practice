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


# 🔹 Question 2 – Exception Handling + Multiple Exceptions
# Write a Python program to:
# 👉 Take two numbers from user
# 👉 Take an index number from user
# 👉 Store the two numbers inside a list
# Example:
# [10, 20]
# 👉 Print:
# Division Result = first_number / second_number
# 👉 Then print:
# Value at given index
# Handle Exceptions:
# ✅ If second number is 0:
# Cannot divide by zero ❌
# ✅ If user enters invalid number:
# Invalid Number ❌
# ✅ If index is out of range:
# Index Out of Range ❌
# Example Output:
# Enter First Number: 10
# Enter Second Number: 2
# Enter Index: 1
# Division Result: 5.0
# Value: 20
# OR
# Enter First Number: 10
# Enter Second Number: 0
# Cannot divide by zero ❌
# OR
# Enter First Number: 10
# Enter Second Number: 2
# Enter Index: 5
# Index Out of Range ❌
# ⚠️ Conditions:
# ✅ Use one try block
# ✅ Handle multiple exceptions separately
# ✅ Use list indexing

numbers = []
try:    
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    numbers.append(a)
    numbers.append(b)
    index = int(input("Enter Index: "))
    result = a / b
    value = numbers[index]    
except ZeroDivisionError:
    print("Cannot divide by zero ❌")
except ValueError:
    print("Invalid Number ❌")
except IndexError:
    print("Index Out of Range ❌")
else:
    print(f"Division Result: {result}")
    print(f"Value: {value}")