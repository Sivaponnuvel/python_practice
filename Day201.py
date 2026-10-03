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


# 🔹 Question 2 – sort()
# Create a Python program to manage student marks.
# Start with:
# marks = [78, 92, 65, 88, 55, 95]
# Sort the marks in ascending order using sort().
# Then display the sorted list and the highest mark.
# Expected Output
# Sorted Marks: [55, 65, 78, 88, 92, 95]
# Highest Mark: 95
# ⚠️ Conditions
# ✅ Must use sort()
# ✅ Sort in ascending order
# ✅ Display the sorted list
# ✅ Display the highest mark
# ❌ Don't use sorted()

marks = [78, 92, 65, 88, 55, 95]

marks.sort()

print(f"Sorted Marks: {marks}")
print(f"Highest Marks: {marks[-1]}")