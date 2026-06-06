# 🔹 Question 1 – Modules & Packages: Math Utility Package
# Create the following structure:
# Day83/
# │
# ├── main.py
# │
# └── utilities/
#     ├── __init__.py
#     └── math_utils.py
# Inside math_utils.py
# Create functions:
# square(number)
# cube(number)
# factorial(number)
# Rules
# ✅ square() → return square of number
# ✅ cube() → return cube of number
# ✅ factorial() → calculate factorial using loop
# ❌ Do not use recursion
# ❌ Do not use math.factorial()
# Inside main.py
# 👉 Import functions from package
# 👉 Take number from user
# 👉 Print:
# Enter Number: 5
# Square: 25
# Cube: 125
# Factorial: 120
# ⚠️ Conditions:
# ✅ Use custom package
# ✅ Use custom module
# ✅ Use imports properly

from utilities import math_utils

number = int(input("Enter Number: "))

print(f"Square: {math_utils.square(number)}")
print(f"Cube: {math_utils.cube(number)}")
print(f"Factorial: {math_utils.factorial(number)}")


# 🔹 Question 2 – OOP: Shopping Cart System
# Create a class:
# ShoppingCart
# Constructor
# Should create an empty list:
# self.items = []
# Methods
# add_item(item_name)
# Add item into cart
# Example:
# cart.add_item("Laptop")
# remove_item(item_name)
# Remove item if exists
# Otherwise print:
# Item Not Found ❌
# view_cart()
# Print all items
# Example:
# --- Cart Items ---
# Laptop
# Mouse
# Keyboard
# If cart is empty:
# Cart is Empty ❌
# Program Flow
# 👉 Create object
# 👉 Add 3 items using user input
# 👉 View cart
# 👉 Ask item name to remove
# 👉
# Remove item
# 👉 
# View cart again
# Example Output
# Enter Item: Laptop
# Enter Item: Mouse
# Enter Item: Keyboard
# --- Cart Items ---
# Laptop
# Mouse
# Keyboard
# Enter Item To Remove: Mouse
# Item Removed ✅
# --- Cart Items ---
# Laptop
# Keyboard
# ⚠️ Conditions:
# ✅ Use class
# ✅ Use methods
# ✅ Use list inside class
# ✅ No dictionaries needed

class ShoppingCart:
    def __init__(self):
        self.items = []
    def add_item(self, item_name):
        self.items.append(item_name)
    def remove_item(self, item_name):
        if item_name in self.items:
            self.items.remove(item_name)
            print("Item Removed ✅")
        else:
            print("Item Not Found ❌")
    def view_cart(self):
        if not self.items:
            print("Cart is Empty ❌")
            return
        print("--- Cart Items ---")
        for i in self.items:
            print(i)
cart = ShoppingCart()
for i in range(3):
    item = input("Enter Item: ")
    cart.add_item(item)

cart.view_cart()

remove = input("Enter Item to Remove: ")
cart.remove_item(remove)

cart.view_cart()