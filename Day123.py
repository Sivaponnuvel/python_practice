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


# 🔹 Question 2 – Tuple: Find the Second Smallest Number
# Write a Python program to find the second smallest unique number from a tuple.
# Program Flow
# Take numbers from the user as space-separated input.
# Convert them into a tuple.
# Example:
# Enter Numbers:
# 8 3 6 2 8 1 2
# Output:
# Second Smallest Number: 2
# Example 2
# Enter Numbers:
# 5 5 5
# Output:
# No Second Smallest Number ❌
# ⚠️ Conditions
# ✅ Convert the input into a tuple
# ✅ Use set() and sorted()
# ✅ Display the second smallest unique number
# ❌ Don't manually search using nested loops
# ❌ Don't import any libraries

nums = tuple(map(int,input("Enter Numbers: ").split()))
unique_nums = sorted(set(nums))

if len(unique_nums) >= 2:
    print(f"Second Smallest Number: {unique_nums[1]}")
else:
    print("No Second Smallest Number ❌")