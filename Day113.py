# 🔹 Question 1 – Interview Question: Second Largest Unique Number
# Write a Python program to find the second largest unique number in a list.
# Program Flow
# Take numbers from the user.
# Example:
# Enter Numbers:
# 10 20 30 40 50 40 50
# Output:
# Second Largest Unique Number: 40
# Example 2
# Input:
# Enter Numbers:
# 5 5 5
# Output:
# No Second Largest Number ❌
# Example 3
# Input:
# Enter Numbers:
# 8 2 9 1 9 6
# Output:
# Second Largest Unique Number: 8
# ⚠️ Conditions
# ✅ Take input from the user
# ✅ Remove duplicate values
# ✅ Use built-in functions like set() and sorted()
# ❌ Don't use loops to manually find the second largest
# ❌ Don't import any libraries

numbers = list(map(int, input("Enter Numbers: ").split()))
asc = sorted(set(numbers))

if len(asc) < 2:
    print("No Second Largest Number ❌")
else:
    print(f"Second Largest Unique Number: {asc[-2]}")


