# 🔹 Question 1 – Decorator: Validate Product Price
# Create a decorator called:
# validate_price
# Apply it to:
# create_product(name, price)
# The decorator should check whether the product price is valid before the function executes.
# Program Flow
# Take product details from the user.
# Input:
# Enter product name: Laptop
# Enter price: 50000
# Output:
# Product created successfully ✅
# Product: Laptop
# Price: 50000.0
# If the price is 0 or negative:
# Input:
# Enter product name: Laptop
# Enter price: -5000
# Output:
# Invalid price ❌
# Price must be greater than 0.
# ⚠️ Conditions
# ✅ Create validate_price decorator
# ✅ Create a wrapper function
# ✅ Use @validate_price
# ✅ Use *args
# ✅ Check price inside the decorator
# ✅ Call create_product() only when price is valid
# ✅ Use input()
# ❌ Don't put price validation inside create_product()
# ❌ Don't use libraries

def validate_price(func):
    def wrapper(*args):
        price1 = args[1]
        if price1 <= 0:
            print("Invalid price ❌")
            print("Price must be greater than 0.")
        else:
            print("Product created successfully ✅")
            return func(*args)            
    return wrapper

@validate_price
def create_product(name, price):
    print(f"Product: {name}")
    print(f"Price: {price}")

name = input("Enter product name: ")
price1 = int(input("Enter price: "))
create_product(name, price1)


# 🔹 Question 2 – OOP: Django Model-Style Product Class
# Create a class:
# Product
# Treat this class like a simplified Django Model.
# It should have these attributes:
# id
# name
# price
# category
# Create these methods:
# display_product()
# update_price()
# Program Flow
# Take product details from the user.
# Input:
# Enter Product ID: 101
# Enter Product Name: Keyboard
# Enter Price: 1500
# Enter Category: Electronics
# Display:
# Product ID: 101
# Product Name: Keyboard
# Price: 1500
# Category: Electronics
# Then ask:
# Enter new price: 1800
# Update the price and display:
# Price updated successfully ✅
# Product ID: 101
# Product Name: Keyboard
# Price: 1800
# Category: Electronics
# ⚠️ Conditions
# ✅ Create a Product class
# ✅ Use __init__()
# ✅ Use self
# ✅ Store id, name, price, category
# ✅ Create display_product()
# ✅ Create update_price()
# ✅ Take all values using input()
# ✅ Create an object from the class
# ✅ Update the object's price using a method
# ❌ Don't update price directly outside the class
# ❌ Don't use dictionaries
# ❌ Don't import libraries

class Product:
    def __init__(self, id, name, price, category):
        self.id = id
        self.name = name
        self.price = price
        self.category = category

    def display_product(self):
        print(f"Product ID: {self.id}")
        print(f"Product Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Category: {self.category}")

    def update_price(self, update_price):
        self.price = update_price

id = int(input("Enter Product ID: "))
name = input("Enter Product Name: ")
price = int(input("Enter Price: "))
category = input("Enter Category: ")

obj =  Product(id, name, price, category)

obj.display_product()

update_price = int(input("Enter new price: "))
obj.update_price(update_price)

print("Price updated successfully ✅")
obj.display_product()