class BankAccount:
    def __init__(self,balance):
        self.__balance = balance
    def deposit(self,deposit_amount):
        if deposit_amount <= 0:
            raise ValueError("Minimum deposit amount is RS.01") 
        else:
            self.__balance += deposit_amount
            return f"Deposited {deposit_amount} --> Balance {self.__balance}"
    def withdraw(self,withdraw_amount):
        if withdraw_amount > self.__balance:
            raise ValueError("Insufficient balance ❌")
        else:
            self.__balance -= withdraw_amount
            return f"withdrawn {withdraw_amount} --> Balance {self.__balance}"
    def get_balance(self):
        return self.__balance