# 🔹 Question 1 – OOP: Class + Method
# Create a class called BankAccount.
# It should have:
# account_holder
# balance
# Create a method:
# deposit(amount)
# The method should add the deposited amount to the balance.
# Example:
# account = BankAccount("Siva", 5000)
# account.deposit(2000)
# print(account.balance)
# Expected Output:
# 7000
# ⚠️ Conditions:
# Use a class
# Use __init__()
# Use self
# Create a deposit() method
# Don't directly change balance outside the class

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount

account = BankAccount("Siva", 5000)
account.deposit(2000)
print(account.balance)


# 🔹 Question 2 – Exception Handling
# Write a program that divides two numbers.
# Handle the situation where the user tries to divide by zero.
# Example:
# a = 10
# b = 0
# Expected output:
# Cannot divide by zero
# For normal input:
# a = 10
# b = 2
# Expected output:
# 5.0
# ⚠️ Conditions:
# Use try
# Use except
# Handle ZeroDivisionError
# Don't let the program crash

try:
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    print(a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")