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


