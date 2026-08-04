# 🔹 Question 1 – OOP: Bank Account Class
# Write a Python program to create a BankAccount class.
# Program Flow
# Create a class named BankAccount.
# Create a constructor (__init__) to initialize:
# account_holder
# balance
# Create the following methods:
# deposit(amount) → Add the amount to the balance.
# withdraw(amount) → Subtract the amount from the balance only if sufficient balance is available.
# display() → Display the account holder's name and current balance.
# Create one object using user input.
# Display the account details.
# Ask the user for a deposit amount and update the balance.
# Ask the user for a withdrawal amount and update the balance.
# Display the final account details.
# Example
# Input
# Enter Account Holder: Siva
# Enter Initial Balance: 5000
# Enter Deposit Amount: 2000
# Enter Withdraw Amount: 3000
# Output
# Account Details
# Holder  : Siva
# Balance : 5000
# After Transactions
# Holder  : Siva
# Balance : 4000
# If the withdrawal amount is greater than the balance:
# Insufficient Balance ❌
# ⚠️ Conditions
# ✅ Use a class
# ✅ Use __init__()
# ✅ Create deposit(), withdraw(), and display() methods
# ✅ Take input from the user
# ❌ Don't modify the balance directly outside the class
# ❌ Don't use global variables


class BankAccount:

    def __init__(self, account_holder, balance):
        self.__account_holder = account_holder
        self.__balance = balance

    def deposit(self, dep_amount):
        self.__balance += dep_amount

    def withdraw(self, with_amount):
        if self.__balance < with_amount:
            print("Insufficient Balance ❌")
        else:
            self.__balance -= with_amount

    def display(self):
        print(f"Holder  : {self.__account_holder}")
        print(f"Balance : {self.__balance}")

account_holder = input("Enter Account Holder: ")
balance = int(input("Enter Initial Balance: "))
obj = BankAccount(account_holder, balance)

print("Account Details")
obj.display()

dep_amount = int(input("Enter Deposit Amount: "))
obj.deposit(dep_amount)

with_amount = int(input("Enter Withdraw Amount: "))
obj.withdraw(with_amount)

print("After Transactions")
obj.display()


