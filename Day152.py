# 🔹 Question 1 – Exception Handling: Safe List Index Access
# Write a Python program to access an element from a list using a user-provided index.
# Program Flow
# Create a list:
# numbers = [10, 20, 30, 40, 50]
# Ask the user to enter an index.
# Display the value at that index.
# Handle:
# Invalid integer input → ValueError
# Index outside the list → IndexError
# Example 1
# Enter Index: 2
# Output:
# Value: 30
# Example 2
# Enter Index: 10
# Output:
# Index Out of Range ❌
# Example 3
# Enter Index: abc
# Output:
# Invalid Input ❌
# ⚠️ Conditions
# ✅ Use try
# ✅ Use except ValueError
# ✅ Use except IndexError
# ✅ Take input from the user
# ✅ Use list indexing
# ❌ Don't use if to check whether the index exists
# ❌ Don't use any libraries

numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter Index: "))
    print(f"Value: {numbers[index]}")

except ValueError:
    print("Invalid Input")
except IndexError:
    print("Index Out of Range")


