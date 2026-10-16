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



