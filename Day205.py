# 🔹 Question 1 – List Comprehension: Product Price Processing
# Create a Python program for a Shopping Cart.
# Requirements
# - Get 5 product prices from the user.
# - Using list comprehension, create a new list containing:
#   - Only prices greater than or equal to ₹1,000
#   - Add 10% GST to those prices.
# - Display the original prices.
# - Display the updated prices including GST.
# - Use round() to keep the price to 2 decimal places.
# Example
# Enter 5 product prices:
# 500 1200 2500 800 3000
# Original Prices: [500, 1200, 2500, 800, 3000]
# Prices >= 1000 with GST:
# [1320.0, 2750.0, 3300.0]
# Conditions
# - ✅ Must use list comprehension
# - ✅ Must filter prices >= 1000
# - ✅ Must add 10% GST
# - ✅ Must use round()
# - ❌ Do not use filter()
# - ❌ Do not use a normal for loop

prices = list(map(int, input("Enter 5 product prices: ").split()))

new_price = [round(i * 1.10, 2) for i in prices if i >= 1000]

print(f"Original Prices: {prices}")
print("Prices >= 1000 with GST:")
print(new_price)


