# 🔹 Question 1 – OOP: Bank Account with Exception Handling
# Write a Python program to create a BankAccount class and handle invalid transactions using exception handling.
# Program Flow
# Create a class named BankAccount.
# Create a constructor __init__() to initialize:
# account_holder
# balance
# Create these methods:
# deposit(amount) → Add the amount to the balance.
# withdraw(amount) → Withdraw the amount only if sufficient balance is available.
# display() → Display account holder and balance.
# Exception Conditions
# If the deposit amount is 0 or negative, raise:
# ValueError
# If the withdrawal amount is greater than the balance, raise:
# ValueError
# If the withdrawal amount is 0 or negative, raise:
# ValueError
# Use try-except while performing deposit and withdrawal.
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
# If the user enters:
# Enter Withdraw Amount: 10000
# Output:
# Error: Insufficient Balance ❌
# ⚠️ Conditions
# ✅ Use a class
# ✅ Use __init__()
# ✅ Use deposit()
# ✅ Use withdraw()
# ✅ Use display()
# ✅ Use try-except
# ✅ Use raise ValueError
# ✅ Don't modify balance directly outside the class
# ❌ Don't use global variables
# ❌ Don't use if outside the class to validate transactions

class BankAccount:
    def __init__(self, account_holder, balance):
        self.__account_holder = account_holder
        self.__balance = balance

    def deposit(self, dep_amount):
        if dep_amount <= 0:
                raise ValueError("Error: Insufficient Deposit Amount ❌")
        self.__balance += dep_amount

    def withdraw(self, with_amount):
        if with_amount <= 0:
            raise ValueError("Error: Insufficient Withdraw Amount ❌")
        if with_amount > self.__balance:
            raise ValueError ("Error: Insufficient Balance ❌")
        self.__balance -= with_amount

    def display(self):
        print(f"Holder  : {self.__account_holder}")
        print(f"Balance : {self.__balance}")

account_holder = input("Enter Account Holder: ")
balance = int(input("Enter Initial Balance: "))
obj = BankAccount(account_holder, balance)

print("Account Details")
obj.display()

try:
    dep_amount = int(input("Enter Deposit Amount: "))
    obj.deposit(dep_amount)
except ValueError as e:
    print(e)

try:
    with_amount = int(input("Enter Withdraw Amount: "))
    obj.withdraw(with_amount)
    print("After Transactions")
    obj.display()
except ValueError as e:
    print(e)


# 🔹 Question 2 – Exception Handling: Student Marks Validation
# Write a Python program to take a student's name and marks, then validate the marks using custom exception handling.
# Program Flow
# Take the following inputs:
# Enter Student Name:
# Enter Marks:
# Marks must be between 0 and 100.
# Create a function:
# validate_marks(marks)
# Inside the function:
# If marks are less than 0, raise ValueError.
# If marks are greater than 100, raise ValueError.
# Otherwise return the marks.
# Use try-except to handle invalid marks.
# Example 1
# Input
# Enter Student Name: Siva
# Enter Marks: 85
# Output
# Student Name : Siva
# Marks        : 85
# Valid Marks ✅
# Example 2
# Input
# Enter Student Name: Rahul
# Enter Marks: 120
# Output
# Invalid Marks ❌
# Marks must be between 0 and 100
# Example 3
# Input
# Enter Student Name: Priya
# Enter Marks: abc
# Output
# Invalid Input ❌
# ⚠️ Conditions
# ✅ Take input from the user
# ✅ Create validate_marks(marks)
# ✅ Use try-except
# ✅ Use ValueError
# ✅ Use raise ValueError
# ✅ Handle non-integer input
# ❌ Don't use external libraries
# ❌ Don't use if to handle the exception outside validate_marks()

def validate_marks(marks):
    if marks < 0 or marks > 100:
        raise ValueError("Invalid Marks ❌ \nMarks must be between 0 and 100")
    return marks

try:
    stu_name = input("Enter Student Name: ")
    stu_mark = int(input("Enter Marks: "))

    marks = validate_marks(stu_mark)

    print(f"Student Name : {stu_name}")
    print(f"Marks        : {marks}")
    print("Valid Marks ✅")

except ValueError as e:
    if "invalid literal" in str(e):
        print("Invalid Input ❌")
    else:
        print(e)