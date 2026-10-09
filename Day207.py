# 🔹 Question 1 – Dictionary: Find Product with Lowest Price
# Create a Python program using a dictionary to store product names and their prices.
# Input data
# products = {    "Laptop": 55000,    "Mouse": 800,    "Keyboard": 1500,    "Monitor": 12000}
# Find the product with the lowest price.
# Expected Output
# Product with lowest price: Mouse
# Price: 800
# ⚠️ Conditions
# - ✅ Use a dictionary
# - ✅ Use a for loop
# - ✅ Use .items()
# - ✅ Find the lowest price using logic
# - ✅ Display the product name
# - ✅ Display the price
# - ❌ Don't use min()
# - ❌ Don't use libraries
# - ❌ Don't hardcode "Mouse" or 800

products = {}

for i in range(4):
    product_name = input("Enter Product Name: ")
    product_price = int(input("Enter Product Price: "))
    products[product_name] = product_price

lowest_product = ""
lowest_price = None

for key, value in products.items():
    if lowest_price is None or value < lowest_price:
        lowest_price = value
        lowest_product = key

print(f"Product with lowest price: {lowest_product}")
print(f"Price: {lowest_price}")


# 🔹 Question 2 – Exception Handling: Safe Number Division
# Create a Python program that takes two numbers from the user and divides the first number by the second number.
# You must handle invalid input and division by zero using exception handling.
# Example 1
# Enter first number: 100
# Enter second number: 5
# Expected Output
# Result: 20.0
# Example 2
# Enter first number: 100
# Enter second number: 0
# Expected Output
# Cannot divide by zero ❌
# Example 3
# Enter first number: abc
# Expected Output
# Invalid input ❌ Please enter numbers only.
# ⚠️ Conditions
# - ✅ Use try
# - ✅ Use except
# - ✅ Handle ValueError
# - ✅ Handle ZeroDivisionError
# - ✅ Take values using input()
# - ✅ Convert the input into numbers
# - ❌ Don't use libraries
# - ❌ Don't simply check the value with if instead of exception handling
# - ❌ Don't allow the program to crash

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    result = num1 / num2
    print(f"Result: {result}")

except ZeroDivisionError:
    print("Cannot divide by zero ❌")

except ValueError:
    print("Invalid input ❌ Please enter numbers only.")