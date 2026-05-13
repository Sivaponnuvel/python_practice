# 🔹 Question 1 – List of Products
# Write a Python program to:
# 👉 Create an empty list:
# products = []
# 👉 Take details for 3 products:
# name
# price
# 👉 Store each product as dictionary inside list
# Example:
# [
#     {"name": "Laptop", "price": 50000},
#     {"name": "Mouse", "price": 800}
# ]
# 👉 Print all products like:
# Laptop - 50000
# Mouse - 800
# 👉 Also print:
# Most expensive product price
# Cheapest product price
# Example Output:
# Most Expensive: 50000
# Cheapest: 800

products = []
for i in range(3):
    name = input("Enter the product name: ")
    price = int(input("Enter the product price: "))
    products.append({"name": name, "price": price})
for i in products:
    print(f"{i['name']} - {i['price']}")
expensive = 0
for i in products:
    if (i['price']) > expensive:
        expensive = i['price']
print(f"Most Expensive: {expensive}")
cheapest = products[0]['price']
for i in products:
    if (i['price']) < cheapest:
        cheapest = i['price']
print(f"Cheapest: {cheapest}")


