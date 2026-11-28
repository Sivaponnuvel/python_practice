# Question 1 – Find the Product of All Elements in a List
# Interview Topics: reduce(), Lambda Functions, Lists, Arithmetic Operators.
# Given a list of integers, calculate the product of all elements using reduce().
# Requirements:
# 1. Get the number of elements from the user.
# 2. Get integer values using input().
# 3. Store the values in a list.
# 4. Import reduce from functools.
# 5. Use reduce() with a lambda function.
# 6. Do not use for or while loops to calculate the product.
# 7. Display the final product.
# Expected Output:
# Enter how many numbers: 5
# Enter number 1: 2
# Enter number 2: 3
# Enter number 3: 4
# Enter number 4: 5
# Enter number 5: 2
# Original List: [2, 3, 4, 5, 2]
# Product of All Elements: 240

from functools import reduce

numbers = []

n = int(input("Enter how many numbers: "))

for i in range(n):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)

result = reduce(lambda x, y: x * y, numbers)

print(f"Original List: {numbers}")
print(f"Product of All Elements: {result}")


