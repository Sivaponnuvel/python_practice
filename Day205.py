# 🔹 Question 1 – List Comprehension: Product Price Processing
# Create a Python program for a Shopping Cart.
# Requirements
# - Get 5 product prices from the user.
# - Using list comprehension, create a new list containing:
#   - Only prices greater than or equal to ₹1,000
#   - Add 10% GST to those prices.
# - Display the original prices.
# - Display the updated prices including GST.
# - Use round() to keep the price to 2 decimal places.
# Example
# Enter 5 product prices:
# 500 1200 2500 800 3000
# Original Prices: [500, 1200, 2500, 800, 3000]
# Prices >= 1000 with GST:
# [1320.0, 2750.0, 3300.0]
# Conditions
# - ✅ Must use list comprehension
# - ✅ Must filter prices >= 1000
# - ✅ Must add 10% GST
# - ✅ Must use round()
# - ❌ Do not use filter()
# - ❌ Do not use a normal for loop

prices = list(map(int, input("Enter 5 product prices: ").split()))

new_price = [round(i * 1.10, 2) for i in prices if i >= 1000]

print(f"Original Prices: {prices}")
print("Prices >= 1000 with GST:")
print(new_price)


# 🔹 Question 2 – Nested Loops: Student Marks Analysis
# Create a Python program to analyze marks of 3 students, where each student has 3 subject marks.
# Requirements
# Store the marks in a 2D list:
# marks = [[80, 75, 90], [65, 70, 85], [90, 95, 88]]
# Using nested loops:
# 1. Display each student's marks.
# 2. Calculate each student's total.
# 3. Calculate each student's average.
# 4. Display the student number, total, and average.
# 5. Find and display the highest total among the 3 students.
# Expected Output
# Student 1 Marks: [80, 75, 90]
# Total: 245
# Average: 81.67
# Student 2 Marks: [65, 70, 85]
# Total: 220
# Average: 73.33
# Student 3 Marks: [90, 95, 88]
# Total: 273
# Average: 91.0
# Highest Total: 273
# Conditions
# - ✅ Must use a 2D list
# - ✅ Must use nested loops
# - ✅ Must calculate total using a loop
# - ✅ Must calculate average
# - ✅ Must find the highest total
# - ❌ Do not use sum() for calculating totals

marks = [ [80, 75, 90], [65, 70, 85], [90, 95, 88] ]

highest_total = 0

for i in range(len(marks)):
    print(f"Student {i + 1} Marks: {marks[i]}")

    total = 0

    for mark in marks[i]:
        total += mark

    print(f"Total: {total}")
    print(f"Average: {total / len(marks[i])}")

    if total > highest_total:
        highest_total = total

print(f"Highest Total: {highest_total}")