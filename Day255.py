# Question 1 – Bank Account Class
# Interview Topics: Class, Object, Constructor, Instance Variables, Instance Methods, Encapsulation Basics.
# Create a Python class named BankAccount.
# Requirements:
# 1. Create a class named BankAccount.
# 2. Create a constructor that accepts account_holder and balance.
# 3. Store these values using instance variables.
# 4. Create a method named deposit() that accepts an amount and adds it to the balance.
# 5. Create a method named withdraw() that accepts an amount and subtracts it from the balance.
# 6. Do not allow withdrawal if the amount is greater than the available balance.
# 7. Create a method named display_balance() to display account details.
# 8. Create an object and call all three methods.
# Expected Output:
# Account Holder: Arun
# Initial Balance: 10000
# Deposited: 5000
# Current Balance: 15000
# Withdrawn: 3000
# Current Balance: 12000
# Account Holder: Arun
# Final Balance: 12000

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")
        print(f"Current Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance!")
        elif amount <= 0:
            print("Enter a valid amount")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
            print(f"Current Balance: {self.balance}")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Final Balance: {self.balance}")

obj = BankAccount("Arun", 10000)

print(f"Account Holder: {obj.account_holder}")
print(f"Initial Balance: {obj.balance}")

obj.deposit(5000)

obj.withdraw(3000)

obj.display_balance()


