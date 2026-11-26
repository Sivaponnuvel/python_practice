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


# Question 2 – Inheritance and Method Overriding
# Interview Topics: Inheritance, Parent Class, Child Class, Method Overriding, super().
# Create a parent class named Employee and a child class named Developer.
# Requirements:
# 1. Create a parent class named Employee.
# 2. Create a constructor that accepts name and salary.
# 3. Create a method named display_details() to display employee details.
# 4. Create a child class named Developer that inherits from Employee.
# 5. Add an additional constructor parameter named programming_language.
# 6. Use super() to call the parent constructor.
# 7. Override the display_details() method in the child class.
# 8. Display the employee name, salary and programming language.
# 9. Create an object of the Developer class and call display_details().
# Expected Output:
# Employee Name: Kumar
# Salary: 40000
# Programming Language: Python

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Salary: {self.salary}")

class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def display_details(self):
        super().display_details()
        print(f"Programming Language: {self.language}")

obj1 = Developer("Kumar", 40000, "Python")

obj1.display_details()