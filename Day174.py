# 🔹 Question 1 – Lambda + filter(): Filter Even Numbers
# Write a Python program to take numbers from the user and find all the even numbers using lambda and filter().
# Program Flow
# Take space-separated numbers from the user.
# Convert them into a list of integers.
# Use filter() with a lambda function.
# Display the even numbers.
# Example
# Input:
# Enter numbers: 10 15 22 31 40 55 68
# Output:
# Even Numbers: [10, 22, 40, 68]
# ⚠️ Conditions
# ✅ Use input()
# ✅ Use .split()
# ✅ Use map()
# ✅ Use filter()
# ✅ Use lambda
# ❌ Don't use a normal for loop to filter the numbers
# ❌ Don't use list comprehension
# ❌ Don't import any libraries

numbers = list(map(int, input("Enter Numbers: ").split()))

result = list(filter(lambda number: number % 2 == 0, numbers))

print(f"Even Numbers: {result}")


# 🔹 Question 2 – List Comprehension: Square of Odd Numbers
# Write a Python program to take numbers from the user and create a new list containing the squares of only the odd numbers.
# Example
# Input:
# Enter numbers: 2 3 4 5 6 7
# Output:
# Odd Number Squares: [9, 25, 49]
# Because:
# 3² = 9
# 5² = 25
# 7² = 49
# ⚠️ Conditions
# ✅ Use input()
# ✅ Use .split()
# ✅ Convert the values to integers
# ✅ Use list comprehension
# ✅ Use % operator
# ❌ Don't use a normal for loop
# ❌ Don't use filter()
# ❌ Don't use map()
# ❌ Don't import any libraries
# 💡 Hint
# Your list comprehension should have the basic structure:
# [expression for item in list if condition]

nums = list(map(int, input("Enter Numbers: ").split()))

squares = [n**2 for n in nums if n % 2 != 0]

print(f"Odd Number Squares: {squares}")