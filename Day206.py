# 🔹 Question 1 – List: Remove Duplicate Values
# Write a Python program to remove duplicate values from a list without using set().
# Input
# numbers = [10, 20, 10, 30, 20, 40, 30, 50]
# Expected Output
# Original List: [10, 20, 10, 30, 20, 40, 30, 50]
# List without duplicates: [10, 20, 30, 40, 50]
# ⚠️ Conditions
# - ✅ Use a list
# - ✅ Use a for loop
# - ✅ Create a new list
# - ✅ Maintain the original order
# - ❌ Don't use set()
# - ❌ Don't use libraries
# - ❌ Don't hardcode the final output
# - ❌ Don't use dict.fromkeys()

numbers = list(map(int, input("Enter a numbers: ").split()))

remove_duplicate = []

for i in numbers:
    if i not in remove_duplicate:
        remove_duplicate.append(i)

print(f"Original List: {numbers}")
print(f"List without duplicates: {remove_duplicate}")


# 🔹 Question 2 – OOP: Encapsulation – Bank Account
# Create a class:
# BankAccount
# The class should contain:
# account_holder
# balance
# Create these methods:
# deposit()
# withdraw()
# display_balance()
# Program Flow
# Take input from the user.
# Enter account holder: Siva
# Enter initial balance: 10000
# Then:
# Enter deposit amount: 5000
# Expected:
# Deposit successful ✅
# Current Balance: 15000
# Then:
# Enter withdrawal amount: 3000
# Expected:
# Withdrawal successful ✅
# Current Balance: 12000
# If withdrawal amount is greater than the balance:
# Insufficient balance ❌
# ⚠️ Conditions
# - ✅ Create a BankAccount class
# - ✅ Use __init__()
# - ✅ Use self
# - ✅ Create deposit()
# - ✅ Create withdraw()
# - ✅ Create display_balance()
# - ✅ Take values using input()
# - ✅ Update balance through methods
# - ❌ Don't modify balance directly outside the class
# - ❌ Don't use dictionaries
# - ❌ Don't import libraries

class BankAccount:
    def __init__(self, account_holder, balance):
        self.__account_holder = account_holder
        self.__balance = balance

    def deposit(self, deposit_amount):
        self.__balance += deposit_amount
        print("Deposit successful ✅")

    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.__balance:
            print("Insufficient balance ❌")
        else:
            self.__balance -= withdraw_amount
            print("Withdrawal successful ✅")

    def display_balance(self):
        print(f"Current Balance: {self.__balance}")

account_holder = input("Enter account holder: ")
balance = int(input("Enter initial balance: "))

obj = BankAccount(account_holder, balance)

deposit_amount = int(input("Enter deposit amount: "))
obj.deposit(deposit_amount)
obj.display_balance()

withdraw_amount = int(input("Enter withdrawal amount: "))
obj.withdraw(withdraw_amount)
obj.display_balance()