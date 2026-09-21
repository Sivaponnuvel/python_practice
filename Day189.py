# 🔹 Question 1 – List Comprehension
# Write a Python program to create a new list containing the squares of only the even numbers from a given list.
# Example Input:
# Enter numbers: 1 2 3 4 5 6
# Expected Output:
# Even numbers squares: [4, 16, 36]
# Conditions:
# Get numbers from the user.
# Use list comprehension.
# Do not use a normal for loop to create the result.
# Only even numbers should be included.
# Square each selected number.

numbers = list(map(int, input("Enter numbers: ").split()))

squares = [i ** 2 for i in numbers if i % 2 == 0]

print(f"Even numbers squares: {squares}")


