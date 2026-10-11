# 🟢 Question 1 – List Comprehension
# Topic: Filtering and transforming data
# Imagine you're working on an e-commerce application. You receive a list of product prices:
# prices = [1200, 500, 2500, 800, 3000, 150]
# Write a Python program using list comprehension to:
# 1. Select only prices greater than or equal to 1000.
# 2. Apply a 10% discount to those selected prices.
# 3. Store the discounted prices in a new list.
# 4. Print both the selected prices and the discounted prices.
# Expected output:
# Selected Prices: [1200, 2500, 3000]
# Discounted Prices: [1080.0, 2250.0, 2700.0]
# Rules:
# - Use list comprehension.
# - Do not use a regular for loop to build the new lists.
# - Do not use external libraries.

prices = [1200, 500, 2500, 800, 3000, 150]

new_price = [i for i in prices if i >= 1000 ]
discount_price = [round(i * 0.90, 2) for i in prices if i >= 1000 ]

print(f"Selected Prices: {new_price}")
print(f"Discounted Prices: {discount_price}")


# 🟢 Question 2 – OOP Inheritance and super()
# Topic: Inheritance in Python
# Create a parent class named User with:
# - name
# - email
# - A method display_user() that prints the name and email.
# Create a child class named Developer that inherits from User, with an additional attribute:
# - programming_language
# Requirements:
# 1. Use super() to call the parent class constructor.
# 2. Override display_user() in the child class.
# 3. Display the user's name, email, and programming language.
# 4. Create a Developer object using user input and call display_user().
# Example input:
# Enter name: Siva
# Enter email: siva@example.com
# Enter programming language: Python
# Expected output:
# Name: Siva
# Email: siva@example.com
# Programming Language: Python
# Rules:
# - Use two classes: User and Developer.
# - Use inheritance and super().
# - Do not use dictionaries to store the user details.

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def display_user(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")

class Developer(User):
    def __init__(self, name, email, language):
        super().__init__(name, email)
        self.language = language

    def display_user(self):
        super().display_user()
        print(f"Programming Language: {self.language}")

name = input("Enter name: ")
email = input("Enter email: ")
language = input("Enter programming language: ")

obj = Developer(name, email, language)

obj.display_user()