# 🔹 Question 1 – reduce(): Find the Product of All Numbers
# Write a Python program to find the product of all numbers in a list using reduce().
# Program Flow
# Take space-separated integers from the user.
# Convert them into a list.
# Use reduce() to multiply all the numbers.
# Display the final product.
# Example
# Input
# Enter Numbers: 2 3 4 5
# Output
# Product: 120
# ⚠️ Conditions
# ✅ Take input from the user
# ✅ Import reduce from functools
# ✅ Use reduce()
# ✅ Use a lambda function
# ❌ Don't use a loop to calculate the product
# ❌ Don't create a separate function using def

from functools import reduce

numbers = list(map(int,input("Enter Numbers: ").split()))
res = reduce(lambda x, y: x * y, numbers)
print(f"Product: {res}")


