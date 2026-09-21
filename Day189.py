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


# 🔹 Question 2 – Lambda + filter()
# Write a Python program to find all the numbers greater than 50 from a given list using lambda and filter().
# Example Input:
# Enter numbers: 25 60 45 80 30 100
# Expected Output:
# Numbers greater than 50: [60, 80, 100]
# Conditions:
# Get numbers from the user.
# Use filter().
# Use a lambda function as the filtering condition.
# Do not use a normal for loop for filtering.
# Convert the final result into a list.

nums = list(map(int, input("Enter numbers: ").split()))

n = list(filter(lambda x: x > 50, nums))

print(f"Numbers greater than 50: {n}")