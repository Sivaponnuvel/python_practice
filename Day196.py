# 🔹 Question 1 – append()
# Write a Python program for a shopping cart.
# Start with:
# cart = ["Laptop", "Mouse"]
# Ask the user to enter one new product and add it to the cart using append().
# Expected behavior
# If the user enters:
# Keyboard
# Output:
# Updated Cart: ['Laptop', 'Mouse', 'Keyboard']
# ⚠️ Conditions
# ✅ Must use append()
# ❌ Do not use extend()
# ✅ Display the updated list

cart = ["Laptop", "Mouse"]

new_product = input("Enter one new product: ")

cart.append(new_product)

print(f"Updated Cart: {cart}")


