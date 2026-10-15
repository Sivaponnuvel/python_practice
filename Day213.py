# 🟢 Question 1 – Generators and yield
# Topic: Memory-efficient iteration
# Imagine you're building an application that processes order IDs. Create a generator function named generate_order_ids(n).
# Your program should:
# 1. Generate order IDs from 1 to n.
# 2. Use yield to return each ID one at a time.
# 3. Get n from user input.
# 4. Iterate through the generator and print each order ID.
# 5. Print the total number of IDs generated.
# Example input:
# Enter number of orders: 5
# Expected output:
# Order IDs:
# 1
# 2
# 3
# 4
# 5
# Total Orders: 5
# Rules:
# - Use a generator function with yield.
# - Do not return a list of IDs.
# - Do not use external libraries.

def generate_order_ids(n):
    for i in range(1, n + 1):
        yield i

number = int(input("Enter number of orders: "))

print("Order IDs:")

for num in generate_order_ids(number):
    print(num)

print(f"Total Orders: {number}")


# 🟢 Question 2 – @property and Encapsulation
# Topic: OOP — controlled access to attributes
# Create a class named Product that manages product prices safely.
# Your class should have:
# - name
# - A private attribute __price
# - A price property to retrieve the price
# - A setter for price that accepts only values greater than 0
# Requirements:
# 1. Initialize the product name and price in __init__().
# 2. Use @property to read the price.
# 3. Use @price.setter to validate updates.
# 4. If the price is zero or negative, print Invalid price! and do not update the price.
# 5. Create a product object using user input.
# 6. Display its initial price.
# 7. Ask for a new price, update it, and display the final price.
# Example input:
# Enter product name: Laptop
# Enter initial price: 50000
# Enter new price: -100
# Expected output:
# Product: Laptop
# Initial Price: 50000.0
# Invalid price!
# Final Price: 50000.0
# Rules:
# - Use @property and @price.setter.
# - Store the price in __price.
# - Do not modify __price directly outside the class.
# - Do not use external libraries.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value
        else:
            print("Invalid price!")

name = input("Enter product name: ")
initial_price = float(input("Enter initial price: "))

obj = Product(name, initial_price)

print(f"Product: {obj.name}")
print(f"Initial Price: {obj.price}")

new_price = float(input("Enter new price: "))
obj.price = new_price

print(f"Final Price: {obj.price}")