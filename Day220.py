# 🔹 Question 1 – String Coding Problem
# Topic: Strings, Loops and Conditional Statements
# Write a Python program to check whether two strings are anagrams of each other.
# Two strings are anagrams if they contain the same characters with the same frequencies, regardless of order.
# Example:
# string1 = "listen"string2 = "silent"
# Expected output:
# The strings are anagrams
# Another example:
# string1 = "hello"string2 = "world"
# Expected output:
# The strings are not anagrams
# Requirements:
# 1. Get two strings from user input.
# 2. Check whether both strings contain the same characters with the same frequencies.
# 3. Display whether they are anagrams.
# 4. Your program should work with different input strings.
# Conditions:
# - Use loops and conditional statements.
# - Do not use sorted().
# - Do not use collections.Counter.
# - Do not import external libraries.
# - Do not hardcode the result.
# - Treat uppercase and lowercase letters as different characters.

string1 = input("Enter a string1: ")
string2 = input("Enter a string2: ")

if len(string1) != len(string2):
    print("The strings are not anagrams")

else:
    is_anagram = True

    for char in string1:
        count1 = 0
        count2 = 0

        for i in string1:
            if i == char:
                count1 += 1

        for j in string2:
            if j == char:
                count2 += 1

        if count1 != count2:
            is_anagram = False
            break

    if is_anagram:
        print("The strings are anagrams")
    else:
        print("The strings are not anagrams")


# 🔹 Question 2 – OOP Coding Problem
# Topic: Encapsulation, Classes and Methods
# Create a class named BankAccount to manage a bank account.
# Requirements:
# 1. Create a BankAccount class.
# 2. Initialize account_holder and balance using the constructor.
# 3. Store the balance using a private attribute named __balance.
# 4. Create a deposit(amount) method that adds money to the balance.
# 5. Create a withdraw(amount) method that subtracts money only when the withdrawal amount is positive and does not exceed the balance.
# 6. Create a display_balance() method to display the current balance.
# 7. Create an object and demonstrate depositing, withdrawing, and displaying the balance.
# Example operations:
# account = BankAccount("Arun", 5000)account.deposit(1000)account.withdraw(2000)account.display_balance()
# Expected output:
# Account Holder: Arun
# Current Balance: 4000
# Conditions:
# - Use self to access instance attributes.
# - Use __balance as the private balance attribute.
# - Reject zero or negative deposit and withdrawal amounts.
# - Do not allow withdrawal when funds are insufficient.
# - Do not import libraries.
# - Do not hardcode the entire output outside the class methods.

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount")
        else:
            self.__balance += amount
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif amount > self.__balance:
            print("Insufficient funds")
        else:
             self.__balance -= amount

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: {self.__balance}")

account = BankAccount("Arun", 5000)

account.deposit(1000)
account.withdraw(2000)
account.display_balance()