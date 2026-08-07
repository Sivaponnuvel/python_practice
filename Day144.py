# 🔹 Question 1 – Sets: Find Common Elements
# Write a Python program to find the common elements between two sets.
# Program Flow
# Take the first set of integers from the user as space-separated input.
# Take the second set of integers from the user as space-separated input.
# Convert both inputs into sets.
# Display the common elements in ascending order.
# Example 1
# Input
# Enter First Set: 1 2 3 4 5
# Enter Second Set: 3 4 5 6 7
# Output
# Common Elements:
# 3 4 5
# Example 2
# Input
# Enter First Set: 1 2
# Enter Second Set: 3 4
# Output
# No Common Elements ❌
# ⚠️ Conditions
# ✅ Take input from the user
# ✅ Convert the input into sets
# ✅ Use the set intersection operator (&) or intersection()
# ✅ Display the result in ascending order
# ❌ Don't use loops to compare every element
# ❌ Don't use list comprehensions

set_1 = set(map(int, input("Enter First Set: ").split()))
set_2 = set(map(int, input("Enter Second Set: ").split()))

common = set_1 & set_2

if common:
    print("Common Elements:")
    print(*sorted(common))
else:
    print("No Common Elements ❌")


