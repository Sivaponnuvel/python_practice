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


# 🔹 Question 2 – extend()
# You have two lists of students:
# class_a = ["Arun", "Bala", "Kumar"]
# class_b = ["Ravi", "Siva", "Vijay"]
# Combine all students into class_a using extend().
# Expected output
# All Students: ['Arun', 'Bala', 'Kumar', 'Ravi', 'Siva', 'Vijay']
# ⚠️ Conditions
# ✅ Must use extend()
# ❌ Do not use append()
# ✅ Display the final class_a

class_a = ["Arun", "Bala", "Kumar"]
class_b = ["Ravi", "Siva", "Vijay"]

class_a.extend(class_b)

print(f"All Students: {class_a}")