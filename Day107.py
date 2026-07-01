# 🔹 Question 1 – Exception Handling: ATM Withdrawal System
# Write a Python program to create a simple ATM withdrawal system.
# Create a custom exception:
# InsufficientBalanceError
# Create a function:
# withdraw(balance, amount)
# Rules
# If amount <= 0
# Raise:
# Invalid Withdrawal Amount ❌
# If amount > balance
# Raise:
# Insufficient Balance ❌
# Otherwise:
# Deduct the amount from the balance.
# Return the remaining balance.
# Program Flow
# Take input from the user:
# Enter Balance: 5000
# Enter Withdrawal Amount: 1500
# Output:
# Withdrawal Successful ✅
# Remaining Balance: 3500
# Example 2
# Enter Balance: 3000
# Enter Withdrawal Amount: 5000
# Insufficient Balance ❌
# Example 3
# Enter Balance: 5000
# Enter Withdrawal Amount: -100
# Invalid Withdrawal Amount ❌
# ⚠️ Conditions
# ✅ Create a custom exception.
# ✅ Use raise.
# ✅ Use try-except.
# ✅ Create a separate function.
# ❌ Don't use global variables.
# ❌ Don't print inside the function (return the balance on success).

class InvalidAmountError(Exception):
    pass
class InsufficientBalanceError(Exception):
    pass

def withdraw(balance, amount):
    if amount <= 0:
        raise InvalidAmountError("Invalid Withdrawal Amount ❌")
    elif amount > balance:
        raise InsufficientBalanceError("Insufficient Balance ❌")
    balance -= amount
    return balance

try:
    balance = int(input("Enter Balance: "))
    amount = int(input("Enter Withdrawal Amount: "))
    remaining = withdraw(balance, amount)
    print("Withdrawal Successful ✅")
    print(f"Remaining Balance: {remaining}")
except InsufficientBalanceError as e:
    print(e)
except InvalidAmountError as e:
    print(e)


# 🔹 Question 2 – Interview Style: Find the First Non-Repeating Character
# Write a Python program to find the first non-repeating character in a string.
# Example 1
# Input:
# Enter String: swiss
# Output:
# First Non-Repeating Character: w
# Explanation:
# s → repeated
# w → appears once ✅
# i → appears once
# The answer is w because it is the first character that appears only once.
# Example 2
# Input:
# Enter String: aabbcc
# Output:
# No Non-Repeating Character ❌
# Example 3
# Input:
# Enter String: success
# Output:
# First Non-Repeating Character: u
# ⚠️ Conditions
# ✅ Use loops.
# ✅ Use a dictionary to count character frequencies.
# ✅ Find the first character with a count of 1.
# ❌ Don't use collections.Counter.
# ❌ Don't use set().
# ❌ Don't use list comprehensions.

def first_non_repeating(string):
    freq = {}

    for i in string:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    for i in string:
        if freq[i] == 1:
            print(f"First Non-Repeating Character: {i}")
            return
    print("No Non-Repeating Character ❌")

string = input("Enter String: ")
first_non_repeating(string)