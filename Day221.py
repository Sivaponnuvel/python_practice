# 🔹 Question 1 – List Coding Problem
# Topic: Lists, Loops and Conditional Statements
# Write a Python program to find the second-largest unique number in a list without using sorting.
# Example:
# nums = [10, 5, 20, 8, 20, 15]
# Expected output:
# Second Largest: 15
# Requirements:
# 1. Get a list of integers from the user.
# 2. Find the second-largest unique number.
# 3. Display the result.
# 4. Handle the case where a second-largest unique number does not exist.
# Conditions:
# - Use loops and conditional statements.
# - Do not use sort() or sorted().
# - Do not use max() or min().
# - Do not import libraries.
# - Do not hardcode the answer.
# - Duplicate values must not be treated as separate unique numbers.
# Example 2:
# nums = [7, 7, 3]
# Expected output:
# Second Largest: 3
# Example 3:
# nums = [5, 5, 5]
# Expected output:
# No second-largest unique number

nums = list(map(int, input("Enter numbers: ").split()))

largest = None
second_largest = None

for i in nums:
    if largest is None or i > largest:
        if i != largest:
            second_largest = largest
            largest = i

    elif i != largest and (second_largest is None or i > second_largest):
        second_largest = i

if second_largest is not None:
    print(f"Second Largest: {second_largest}")
else:
    print("No second-largest unique number")


# 🔹 Question 2 – OOP Coding Problem
# Topic: Inheritance, Method Overriding and Polymorphism
# Create a parent class named Payment and two child classes named CreditCardPayment and UPIPayment.
# Requirements:
# 1. Create a Payment class with a method named pay(amount) that prints Processing payment.
# 2. Create a CreditCardPayment class that inherits from Payment.
# 3. Override pay(amount) in CreditCardPayment to display the amount paid using a credit card.
# 4. Create a UPIPayment class that inherits from Payment.
# 5. Override pay(amount) in UPIPayment to display the amount paid using UPI.
# 6. Create objects for both child classes.
# 7. Call pay() using both objects with an amount of 1500.
# Expected output:
# Paid 1500 using Credit Card
# Paid 1500 using UPI
# Conditions:
# - Use proper inheritance and method overriding.
# - Use self and method parameters correctly.
# - Demonstrate polymorphism by calling the same method name on different objects.
# - Do not import libraries.
# - Do not hardcode the entire output outside the methods

class Payment:
    def pay(self, amount):
        print("Processing payment")

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")

creditcard = CreditCardPayment()
upi = UPIPayment()

creditcard.pay(1500)
upi.pay(1500)