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


# Question 2 – Find the Longest String in a List Using reduce()
# Interview Topics: reduce(), Lambda Functions, Strings, Lists, Conditional Expressions.
# Given a list of strings, find the longest string using reduce().
# Requirements:
# 1. Get the number of strings from the user.
# 2. Get string values using input().
# 3. Store the strings in a list.
# 4. Import reduce from functools.
# 5. Use reduce() with a lambda function.
# 6. Do not use max() or loops to find the longest string.
# 7. If two strings have the same length, return the first string.
# 8. Display the longest string.
# Expected Output 1:
# Enter how many strings: 5
# Enter string 1: Python
# Enter string 2: Java
# Enter string 3: JavaScript
# Enter string 4: C
# Enter string 5: Django
# Original List: ['Python', 'Java', 'JavaScript', 'C', 'Django']
# Longest String: JavaScript
# Expected Output 2:
# Enter how many strings: 4
# Enter string 1: Apple
# Enter string 2: Mango
# Enter string 3: Orange
# Enter string 4: Grape
# Original List: ['Apple', 'Mango', 'Orange', 'Grape']
# Longest String: Orange

strings = []

user = int(input("Enter how many strings: "))

for i in range(user):
    string = input(f"Enter string {i + 1}: ")
    strings.append(string)

output = reduce(lambda x, y: x if len(x) > len(y) else y, strings)

print(f"Original List: {strings}")
print(f"Longest String: {output}")