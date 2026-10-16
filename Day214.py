# Question 1 – Custom Exceptions
# Topic: Exception Handling
# Imagine you're developing an e-commerce application that validates customer orders. Create a custom exception named InvalidQuantityError.
# Your program should:
# 1. Create a custom exception class named InvalidQuantityError.
# 2. Create a function named validate_quantity(quantity).
# 3. If quantity is less than or equal to 0, raise InvalidQuantityError with the message "Quantity must be greater than zero!".
# 4. If the quantity is valid, return "Order quantity accepted!".
# 5. Get the quantity from user input.
# 6. Handle the custom exception using try and except.
# 7. Print the appropriate message.
# Example 1:
# Enter quantity: 3
# Order quantity accepted!
# Example 2:
# Enter quantity: 0
# Quantity must be greater than zero!
# Conditions:
# - You must create your own exception class.
# - Use raise to trigger the exception.
# - Use try and except to handle it.
# - Do not use external libraries.

class InvalidQuantityError(Exception):
    pass

def validate_quantity(quantity):
    if quantity <= 0:
        raise InvalidQuantityError("Quantity must be greater than zero!")
    return "Order quantity accepted!"

try:
    quantity = int(input("Enter quantity: "))
    print(validate_quantity(quantity))

except InvalidQuantityError as e:
    print(e)


# Question 2 – zip() and enumerate()
# Topic: Processing Product Data
# Imagine you're building a product inventory report. You have two lists containing product names and their prices.
# Write a Python program that:
# 1. Creates these two lists:
# products = ["Laptop", "Mouse", "Keyboard", "Monitor"]prices = [50000, 500, 1500, 12000]
# 2. Uses zip() to combine each product with its corresponding price.
# 3. Uses enumerate() to assign a serial number starting from 1.
# 4. Prints each product's serial number, name, and price.
# 5. Calculates and prints the total price of all products.
# Expected output:
# Product Inventory:
# 1. Laptop - ₹50000
# 2. Mouse - ₹500
# 3. Keyboard - ₹1500
# 4. Monitor - ₹12000
# Total Inventory Value: ₹64000
# Conditions:
# - Use both zip() and enumerate().
# - Start the serial number at 1.
# - Calculate the total using a loop.
# - Do not hardcode the total.
# - Do not use external libraries.

products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
prices = [50000, 500, 1500, 12000]

combine  = zip(products, prices)

print("Product Inventory:")

total = 0

for index, (key, value) in enumerate(combine, start=1):
    print(f"{index}. {key} - ₹{value}")
    total += value

print(f"Total Inventory Value: ₹{total}")