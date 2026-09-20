# 🔹 Question 1 – Encapsulation
# Create a BankAccount class that demonstrates encapsulation.
# Requirements:
# Create a class BankAccount.
# Store:
# account_holder
# balance
# Make balance a private variable using __balance.
# Create a method deposit(amount) to add money.
# Create a method get_balance() to return the current balance.
# The balance should not be directly accessible outside the class.
# Example Input:
# Enter account holder: Siva
# Enter deposit amount: 5000
# Expected Output:
# Account Holder: Siva
# Balance: 5000
# Then:
# Enter deposit amount: 2000
# Expected:
# Updated Balance: 7000
# Conditions:
# Use __balance.
# Use methods to access/update the balance.
# Do not directly modify __balance outside the class.

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account_holder = input("Enter account holder: ")
balance = int(input("Enter deposit amount: "))
obj = BankAccount(account_holder, balance)

print(f"Account Holder: {obj.account_holder}")
print(f"Balance: {obj.get_balance()}")

amount = int(input("Enter deposit amount: "))
obj.deposit(amount)

print(f"Updated Balance: {obj.get_balance()}")


# 🔹 Question 2 – Inheritance
# Create a simple Employee → Developer inheritance program.
# Requirements:
# Create a parent class:
# Employee
# with:
# name
# salary
# display_employee() method
# Create a child class:
# Developer
# with:
# programming_language
# The Developer class should inherit the properties and method from Employee.
# Example Input:
# Enter name: Siva
# Enter salary: 30000
# Enter programming language: Python
# Expected Output:
# Employee Name: Siva
# Salary: 30000
# Programming Language: Python
# Conditions:
# Use inheritance.
# Use super().__init__() in the child class.
# The child class should use the parent's display_employee() method.
# Add a separate method to display the programming language.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_employee(self):
        print(f"Employee Name: {self.name}")
        print(f"Salary: {self.salary}")

class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def display_language(self):
        print(f"Programming Language: {self.language}")
    
name = input("Enter name: ")
salary = int(input("Enter salary: "))
language = input("Enter programming language: ")
emp = Developer(name, salary, language)

emp.display_employee()
emp.display_language()