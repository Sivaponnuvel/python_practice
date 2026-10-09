# 🔹 Question 1 – Dictionary: Find Product with Lowest Price
# Create a Python program using a dictionary to store product names and their prices.
# Input data
# products = {    "Laptop": 55000,    "Mouse": 800,    "Keyboard": 1500,    "Monitor": 12000}
# Find the product with the lowest price.
# Expected Output
# Product with lowest price: Mouse
# Price: 800
# ⚠️ Conditions
# - ✅ Use a dictionary
# - ✅ Use a for loop
# - ✅ Use .items()
# - ✅ Find the lowest price using logic
# - ✅ Display the product name
# - ✅ Display the price
# - ❌ Don't use min()
# - ❌ Don't use libraries
# - ❌ Don't hardcode "Mouse" or 800

products = {}

for i in range(4):
    product_name = input("Enter Product Name: ")
    product_price = int(input("Enter Product Price: "))
    products[product_name] = product_price

lowest_product = ""
lowest_price = None

for key, value in products.items():
    if lowest_price is None or value < lowest_price:
        lowest_price = value
        lowest_product = key

print(f"Product with lowest price: {lowest_product}")
print(f"Price: {lowest_price}")


