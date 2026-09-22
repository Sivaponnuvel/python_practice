# 🔹 Question 1 – 2D List: Find the Largest Element
# Given a 2D list, write a Python program to find the largest element in the entire 2D list.
# Example:
# matrix = [
#     [10, 20, 5],
#     [30, 15, 25],
#     [8, 40, 12]
# ]
# Expected Output:
# Largest element: 40
# Conditions:
# Use a 2D list.
# Use nested for loops.
# Do not use max().
# Find the largest value manually.

matrix = [
    [10, 20, 5],
    [30, 15, 25],
    [8, 40, 12]
]

largest = matrix[0][0]

for i in matrix:
    for j in i:
        if j > largest:
            largest = j

print(f"Largest element: {largest}")


