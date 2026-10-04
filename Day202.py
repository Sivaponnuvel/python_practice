# 🔹 Question 1 – OOPs: Inheritance + Method Overriding
# Create a Python program for an Employee Salary Management System.
# Requirements
# Create a parent class Employee with:
# name
# basic_salary
# Method:
# - calculate_salary() → return the basic salary.
# Create a child class Developer that inherits from Employee.
# Additional attribute:
# - bonus
# Override the calculate_salary() method in Developer to return:
# basic_salary + bonus
# Create a Developer object using user input and display:
# Example Output
# Enter employee name: Siva
# Enter basic salary: 30000
# Enter bonus: 5000
# Employee Name: Siva
# Basic Salary: 30000
# Bonus: 5000
# Total Salary: 35000
# ⚠️ Conditions
# ✅ Must use inheritance.
# ✅ Must use super().__init__().
# ✅ Must override calculate_salary().
# ✅ Must use self.
# ✅ Must create an object.
# ❌ Do not calculate total salary directly outside the class.

class Employee:
    def __init__(self, name, basic_salary):
        self.name = name
        self.basic_salary = basic_salary

    def calculate_salary(self):
        return self.basic_salary

class Developer(Employee):
    def __init__(self, name, basic_salary, bonus):
        super().__init__(name, basic_salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.basic_salary + self.bonus 
    
name = input("Enter employee name: ")
basic_salary = int(input("Enter basic salary: "))
bonus = int(input("Enter bonus: "))

obj = Developer(name, basic_salary, bonus)

print(f"Employee Name: {obj.name}")
print(f"Basic Salary: {obj.basic_salary}")
print(f"Bonus: {obj.bonus}")
print(f"Total: {obj.calculate_salary()}")


# 🔹 Question 2 – Django Models: Product Inventory
# Create a Django-style Product model using a normal Python class.
# Requirements
# Create a class Product with:
# name
# price
# quantity
# Methods:
# total_value() → return price × quantity
# display_product() → display product details and total inventory value.
# Create 3 Product objects using user input.
# Then identify and display the product with the highest inventory value.
# Example Output
# Product Name: Laptop
# Price: 50000
# Quantity: 2
# Inventory Value: 100000
# Product Name: Mouse
# Price: 500
# Quantity: 10
# Inventory Value: 5000
# Product Name: Keyboard
# Price: 1500
# Quantity: 5
# Inventory Value: 7500
# Highest Inventory Value Product: Laptop
# Value: 100000
# ⚠️ Conditions
# ✅ Must use a Product class.
# ✅ Must use __init__().
# ✅ Must use instance attributes.
# ✅ Must create 3 objects.
# ✅ Must use a method to calculate inventory value.
# ✅ Must identify the object with the highest inventory value.
# ❌ Do not use a dictionary instead of a class.

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

    def display_product(self):
        print(f"Product Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Quantity: {self.quantity}")
        print(f"Inventory Value: {self.total_value()}")
        print()
        
products = []

for i in range(3):
    print(f"Enter Product {i+1} Details")
    name = input("Entet product name: ")
    price = int(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    obj = Product(name, price, quantity)
    products.append(obj)

print("Product Details:")
for product in products:
    product.display_product()

highest_product = products[0]

for product in products:
    if product.total_value() > highest_product.total_value():
        highest_product = product

print("Highest Inventory Value Product:", highest_product.name)
print("Value:", highest_product.total_value())