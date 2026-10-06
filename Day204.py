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


# 🔹 Question 2 – List Comprehension – Filter & Transform
# Create a Python program for Student Marks Processing.
# Requirements
# Get 10 student marks from the user.
# Using list comprehension, create a new list containing only marks that are greater than or equal to 50.
# For every passing mark, add 5 bonus marks.
# The final mark must not exceed 100.
# Display the original marks and updated passing marks.
# Example
# Enter 10 student marks:
# 35 60 45 80 90 30 55 75 40 95
# Original Marks: [35, 60, 45, 80, 90, 30, 55, 75, 40, 95]
# Passing Marks After Bonus:
# [65, 85, 95, 60, 80, 100]
# Conditions
# ✅ Must use list comprehension
# ✅ Must filter marks >= 50
# ✅ Must add 5 bonus marks
# ✅ Maximum mark must be 100
# ❌ Do not use filter()
# ❌ Do not use a normal for loop

marks = list(map(int, input("Enter 10 student marks: ").split()))

new_marks = [min(i + 5, 100) for i in marks if i >= 50]

print(f"Original Marks: {marks}")
print("Passing Marks After Bonus:")
print(new_marks)