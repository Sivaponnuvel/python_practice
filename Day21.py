# Question 1
# Write a Python program to:
# 👉 Create a class BankAccount
# 👉 Private variable: __balance
# 👉 Methods:
# deposit(amount)
# withdraw(amount)
# get_balance()
# 👉 Rules:
# Cannot access balance directly
# Use methods only
# Example:
# Balance: 1000
# Deposit 500 → 1500
# Withdraw 300 → 1200

class BankAccount:
    def __init__(self,balance):
        self.__balance = balance
    def deposit(self,deposit_amount):
        self.__balance += deposit_amount
        print(f"Deposited {deposit_amount} -> Balance {self.__balance}")
    def withdraw(self,withdraw_amount):
        if withdraw_amount > self.__balance:
            print("Insufficient balance ❌")
        else:
            self.__balance -= withdraw_amount
            print(f"Withdrawn {withdraw_amount} -> Balance {self.__balance}")
    def get_balance(self):
        return self.__balance
s = BankAccount(1000)
print(f"Initial Balance {s.get_balance()}")
deposit = int(input("Enter the deposit amount : "))
s.deposit(deposit)
withdraw = int(input("Enter the withdraw amount : "))
s.withdraw(withdraw)
print(f"Now current Balance is {s.get_balance()}")


