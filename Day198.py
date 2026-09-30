# 🔹 Question 1 – OOPs: Class & Object
# Create a Python program for a Bank Account using a class.
# Create a class named BankAccount with:
# account_holder
# account_number
# balance
# Create a method:
# display_account()
# that displays all account details.
# Take the values from the user and create an object.
# Example Output
# Enter account holder: Siva
# Enter account number: 12345
# Enter balance: 25000
# Account Holder: Siva
# Account Number: 12345
# Balance: 25000
# ⚠️ Conditions
# ✅ Must use a class
# ✅ Must use __init__()
# ✅ Must create an object
# ✅ Must use self
# ✅ Must create and call display_account()
# ❌ Don't use a dictionary instead of a class

class BankAccount:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def display_account(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")

account_holder = input("Enter account holder: ")
account_number = int(input("Enter account number: "))
balance = int(input("Enter balance: "))

account = BankAccount(account_holder, account_number, balance)

account.display_account()


# 🔹 Question 2 – Exception Handling: try-except
# Create a division program that safely handles invalid input.
# Ask the user for two numbers and divide the first number by the second.
# Your program must handle:
# ZeroDivisionError – when the second number is 0
# ValueError – when the user enters something that cannot be converted to an integer
# Example 1
# Enter first number: 10
# Enter second number: 2
# Result: 5.0
# Example 2
# Enter first number: 10
# Enter second number: 0
# Cannot divide by zero.
# Example 3
# Enter first number: abc
# Enter second number: 2
# Please enter valid numbers.
# ⚠️ Conditions
# ✅ Must use try
# ✅ Must use except
# ✅ Handle ValueError
# ✅ Handle ZeroDivisionError
# ❌ Don't use if to replace exception handling

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print(f"Result: {num1 / num2}")

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError:
    print("Cannot divide by zero.")