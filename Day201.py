# 🔹 Question 1 – pop()
# Create a Shopping Cart program.
# Start with:
# cart = ["Laptop", "Mouse", "Keyboard", "Monitor"]
# Ask the user which item index should be removed using pop().
# Example
# Enter index to remove: 2
# Removed Item: Keyboard
# Updated Cart: ['Laptop', 'Mouse', 'Monitor']
# ⚠️ Conditions
# ✅ Must use pop()
# ✅ Use the index entered by the user
# ✅ Display the removed item
# ✅ Display the updated list
# ❌ Don't use remove()

cart = ["Laptop", "Mouse", "Keyboard", "Monitor"]

remove_item = int(input("Enter index to remove: "))

removed_item = cart.pop(remove_item)

print(f"Removed Item: {removed_item}")
print(f"updated Cart: {cart}")


