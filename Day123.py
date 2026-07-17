# 🔹 Question 1 – List: Remove Duplicate Numbers While Preserving Order
# Write a Python program to remove duplicate numbers from a list while keeping the original order.
# Program Flow
# Take numbers from the user as space-separated input.
# Example:
# Enter Numbers:
# 10 20 10 30 20 40 50 40
# Output:
# Unique Numbers:
# 10 20 30 40 50
# Example 2
# Enter Numbers:
# 1 1 1 1
# Output:
# Unique Numbers:
# 1
# ⚠️ Conditions
# ✅ Take input from the user
# ✅ Use a list
# ✅ Preserve the original order
# ✅ Use a loop
# ❌ Don't use set()
# ❌ Don't use list comprehensions

numbers = list(map(int,input("Enter Numbers: ").split()))
unique_num = []

for i in numbers:
    if i not in unique_num:
        unique_num.append(i)
print("Unique Numbers:")
print(*unique_num)


