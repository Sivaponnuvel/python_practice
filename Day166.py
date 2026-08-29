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


