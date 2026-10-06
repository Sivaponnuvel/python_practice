# 🔹 Question 1 – reduce() – Calculate Total Order Amount
# Create a Python program for an Order Management System.
# Requirements
# Get 5 product prices from the user.
# Use reduce() from the functools module to calculate the total order amount.
# Display all product prices.
# Display the total order amount.
# Example Output
# Enter 5 product prices:
# 100
# 250
# 150
# 300
# 200
# Product Prices: [100, 250, 150, 300, 200]
# Total Order Amount: 1000
# Conditions
# ✅ Must use reduce()
# ✅ Must import reduce from functools
# ✅ Must use lambda
# ❌ Do not use sum()
# ❌ Do not use a normal for loop to calculate the total

from functools import reduce

prices = list(map(int, input("Enter 5 product prices: ").split()))

total = reduce(lambda x, y: x + y, prices)

print(f"Product Prices: {prices}")
print(f"Total Order Amount: {total}")


