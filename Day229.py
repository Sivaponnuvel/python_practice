# 🔹 Question 1 – Lambda, map() and filter() Coding Problem
# Topic: Lambda Functions, map(), filter() and Lists
# Write a Python program to filter even numbers from a list and calculate their squares using lambda, filter(), and map().
# Example 1
# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# Expected output:
# Even Numbers: [2, 4, 6, 8]
# Squared Even Numbers: [4, 16, 36, 64]
# Example 2
# nums = [10, 15, 20, 25, 30]
# Expected output:
# Even Numbers: [10, 20, 30]
# Squared Even Numbers: [100, 400, 900]
# Requirements
# 1. Get a list of integers from the user.
# 2. Use filter() with a lambda function to extract even numbers.
# 3. Use map() with a lambda function to square the even numbers.
# 4. Convert both results into lists.
# 5. Display the even numbers and their squares.
# 6. Preserve the original order of the even numbers.
# 7. Handle an empty list or a list containing no even numbers.
# Conditions
# - Must use lambda.
# - Must use both filter() and map().
# - Do not use explicit for or while loops.
# - Do not use list comprehensions.
# - Do not import libraries.
# - Do not hardcode the output.

nums = list(map(int, input("Enter numbers: ").split()))

even_nums = list(filter(lambda x : x % 2 == 0, nums))

squared_even_nums = list(map(lambda x : x ** 2, even_nums))

if not even_nums:
    print("No even numbers found.")
else:
    print(f"Even Numbers: {even_nums}")
    print(f"Squared Even Numbers: {squared_even_nums}")


