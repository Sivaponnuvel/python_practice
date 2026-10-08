# 🔹 Question 1 – List: Remove Duplicate Values
# Write a Python program to remove duplicate values from a list without using set().
# Input
# numbers = [10, 20, 10, 30, 20, 40, 30, 50]
# Expected Output
# Original List: [10, 20, 10, 30, 20, 40, 30, 50]
# List without duplicates: [10, 20, 30, 40, 50]
# ⚠️ Conditions
# - ✅ Use a list
# - ✅ Use a for loop
# - ✅ Create a new list
# - ✅ Maintain the original order
# - ❌ Don't use set()
# - ❌ Don't use libraries
# - ❌ Don't hardcode the final output
# - ❌ Don't use dict.fromkeys()

numbers = list(map(int, input("Enter a numbers: ").split()))

remove_duplicate = []

for i in numbers:
    if i not in remove_duplicate:
        remove_duplicate.append(i)

print(f"Original List: {numbers}")
print(f"List without duplicates: {remove_duplicate}")


