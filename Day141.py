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


# 🔹 Question 2 – String Interview Question: Longest Substring Without Repeating Characters
# Write a Python program to find the length of the longest substring without repeating characters.
# Program Flow
# Take a string from the user.
# Find the longest substring that contains no repeated characters.
# Display only the length.
# Example 1
# Input
# Enter String: abcabcbb
# Output
# Length: 3
# Explanation: "abc" is the longest substring without repeating characters.
# Example 2
# Input
# Enter String: bbbbb
# Output
# Length: 1
# Example 3
# Input
# Enter String: pwwkew
# Output
# Length: 3
# Explanation: "wke" is the longest substring without repeating characters.
# ⚠️ Conditions
# ✅ Take input from the user
# ✅ Use loops
# ✅ Use a dictionary
# ✅ Return/display only the length
# ❌ Don't use sets as the main solution
# ❌ Don't import any libraries

user = input("Enter String: ")

char_index = {}
start = 0 
max_length = 0

for end in range(len(user)):
    if user[end] in char_index and char_index[user[end]] >= start:
        start = char_index[user[end]] + 1

    char_index[user[end]] = end

    length = end - start + 1

    if length > max_length:
        max_length = length

print(f"Length: {max_length}")