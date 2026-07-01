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


