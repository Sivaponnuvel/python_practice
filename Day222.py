# 🔹 Question 1 – List Coding Problem
# Topic: Lists, Loops and Conditional Statements
# Write a Python program to find all duplicate elements in a list without using a set.
# Example:
# nums = [10, 20, 30, 20, 40, 10, 50, 20]
# Expected output:
# Duplicate Elements: [10, 20]
# Requirements:
# 1. Get a list of integers from the user.
# 2. Find all elements that appear more than once.
# 3. Display each duplicate element only once.
# 4. Preserve the order in which each duplicate first appears in the original list.
# Conditions:
# - Use loops and conditional statements.
# - Do not use set() or set operations.
# - Do not use count().
# - Do not use sorting.
# - Do not import libraries.
# - Do not hardcode the output.
# Example 2:
# nums = [1, 2, 3, 4]
# Expected output:
# Duplicate Elements: []

nums = list(map(int, input("Enter a numbers: ").split()))

duplicates = []

for i in range(len(nums)):
    found = False

    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]:
            found = True
            break

    if found and nums[i] not in duplicates:
        duplicates.append(nums[i])

print(f"Duplicate Elements: {duplicates}")


# 🔹 Question 2 – Python Function Coding Problem
# Topic: Functions, Default Arguments and Conditional Statements
# Write a function named calculate_total() that calculates the total price after applying a discount.
# Requirements:
# 1. Accept price as a required argument.
# 2. Accept discount as an optional argument with a default value of 10 (percentage).
# 3. Calculate the discount amount.
# 4. Return the final price after the discount.
# 5. Display the returned result for both function calls below.
# Example calls:
# print(calculate_total(1000))print(calculate_total(2000, 20))
# Expected output:
# 900.0
# 1600.0
# Conditions:
# - Use a function with a default argument.
# - Use return to send the calculated result back.
# - Reject negative prices and discounts outside the range 0 to 100 by displaying an appropriate error message.
# - Do not import libraries.
# - Do not hardcode the output.

def calculate_total(price, discount=10):

    if price < 0:
        return "Error: Price cannot be negative."

    if discount < 0 or discount > 100:
        return "Error: Discount must be between 0 and 100."

    discount_amount = price * discount / 100
    return price - discount_amount

print(calculate_total(1000))
print(calculate_total(2000, 20))