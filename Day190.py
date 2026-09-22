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


# 🔹 Question 2 – 2D List: Calculate Row Sums
# Given a 2D list, calculate the sum of each row.
# Example:
# matrix = [
#     [10, 20, 30],
#     [5, 15, 25],
#     [2, 4, 6]
# ]
# Expected Output:
# Row 1 sum: 60
# Row 2 sum: 45
# Row 3 sum: 12
# Conditions:
# Use nested for loops.
# Calculate each row's sum separately.
# Do not use sum().
# Print the result for each row.

matrix = [
    [10, 20, 30],
    [5, 15, 25],
    [2, 4, 6]
]

row_num = 1

for i in matrix:
    row_sum = 0

    for j in i:
        row_sum += j

    print(f"Row {row_num} Sum: {row_sum}")
    row_num += 1