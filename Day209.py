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


