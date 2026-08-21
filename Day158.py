# 🔹 Question 1 – List Interview: Find the Second Largest Unique Number
# Write a Python program to find the second largest unique number in a list.
# Example 1
# Input:
# Enter Numbers: 10 20 30 40 50
# Output:
# Second Largest: 40
# Example 2
# Input:
# Enter Numbers: 10 20 30 30 20
# Output:
# Second Largest: 20
# Program Flow
# Take space-separated integers from the user.
# Store them in a list.
# Find the largest and second largest unique numbers manually.
# Display the second largest number.
# ⚠️ Conditions
# ✅ Take input from the user
# ✅ Use a list
# ✅ Use loops
# ✅ Handle duplicate numbers
# ❌ Don't use sort()
# ❌ Don't use sorted()
# ❌ Don't use max()
# ❌ Don't convert the list into a set
# ❌ Don't import any libraries
# 💡 Hint: Think about maintaining two variables:
# largest
# second_largest

numbers = list(map(int, input("Enter Numbers: ").split()))

largest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i

second = None
for i in numbers:
    if i != largest:
        if second is None or i > second:
            second = i

print(f"Second Largest: {second}")


