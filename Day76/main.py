# 🔹 Question 1 – Custom Exception for ATM Withdrawal
# Write a Python program to:
# 👉 Create a custom exception class:
# InsufficientBalanceError
# 👉 Create a class:
# ATM
# 👉 Constructor should take:
# balance
# 👉 Create method:
# withdraw(amount)
# 👉 Rules:
# If withdraw amount is greater than balance:
# Insufficient Balance ❌
# using custom exception
# Otherwise subtract amount and print updated balance
# 👉 Take withdrawal amount from user
# 👉 Handle exception using try-except
# Example Output:
# Enter Balance: 5000
# Enter Withdraw Amount: 2000
# Remaining Balance: 3000
# OR
# Enter Balance: 5000
# Enter Withdraw Amount: 7000
# Insufficient Balance ❌

class InsufficientBalanceError(Exception):
    pass

class ATM:
    def __init__(self, balance):
        self.balance = balance
    def withdraw(self,amount):
        if amount > self.balance:
            raise InsufficientBalanceError("Insufficient Balance ❌")
        else:
            self.balance -= amount
            print(f"Remaining Balance: {self.balance}")
balance = int(input("Enter Balance: "))
atm = ATM(balance)

try:
    amount = int(input("Enter Withdraw Amount: "))
    atm.withdraw(amount)
except InsufficientBalanceError as e:
    print(e)


# 🔹 Question 2 – Module Based String Utility System
# Write a Python program using custom modules:
# 👉 Create file:
# string_utils.py
# 👉 Inside file create functions:
# reverse_text(text)
# count_vowels(text)
# 👉 reverse_text() should manually reverse string using loops
# ❌ Do not use slicing [::-1]
# 👉 count_vowels() should count vowels manually using loops
# 👉 Create another file:
# main.py
# 👉 Import functions from module
# 👉 Take string input from user
# 👉 Print:
# Reversed text
# Total vowels
# Example Output:
# Enter text: FastAPI
# Reversed: IPAtsaF
# Vowels Count: 3

import string_utils as s

text = input("Enter text: ")
print(f"Reversed: {s.reverse_text(text)}")
print(f"Vowels Count: {s.count_vowels(text)}")