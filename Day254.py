# Question 1 – Find All Pairs Whose Sum Equals a Target
# Interview Topics: Lists, Nested Loops, Conditional Statements, Mathematical Operations.
# Given a list of integers and a target value, find all pairs of elements whose sum equals the target.
# Requirements:
# 1. Get the number of elements from the user.
# 2. Get integer values using input().
# 3. Store the values in a list.
# 4. Get a target value from the user.
# 5. Use nested for loops to find pairs.
# 6. Each pair must contain two different elements (different positions).
# 7. Do not print duplicate pairs.
# 8. Display all matching pairs.
# 9. If no pairs are found, display an appropriate message.
# Expected Output:
# Enter how many numbers: 6
# Enter number 1: 2
# Enter number 2: 4
# Enter number 3: 3
# Enter number 4: 5
# Enter number 5: 7
# Enter number 6: 1
# Enter target: 6
# Original List: [2, 4, 3, 5, 7, 1]
# Target: 6
# Pairs: (2, 4), (5, 1)

numbers = []
n = int(input("Enter how many numbers: "))

for i in range(n):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)

target = int(input("Enter target: "))

pairs = []

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            pairs.append((numbers[i], numbers[j]))

print(f"Original List: {numbers}")
print(f"Target: {target}")
if pairs:
    print(f"Pairs: {pairs}")
else:
    print("No pairs found.")


# Question 2 – Find Common Elements Between Two Lists
# Interview Topics: Lists, Nested Loops, Conditional Statements, Element Comparison.
# Given two lists of integers, find the common elements between them without using sets.
# Requirements:
# 1. Get the number of elements for the first list.
# 2. Get integer values using input().
# 3. Get the number of elements for the second list.
# 4. Get integer values using input().
# 5. Use nested for loops to compare both lists.
# 6. Find the common elements.
# 7. Do not use set() or set operations.
# 8. Do not display duplicate common elements.
# 9. If there are no common elements, display an appropriate message.
# Expected Output:
# Enter first list size: 5
# Enter number 1: 10
# Enter number 2: 20
# Enter number 3: 30
# Enter number 4: 40
# Enter number 5: 50
# Enter second list size: 4
# Enter number 1: 20
# Enter number 2: 40
# Enter number 3: 60
# Enter number 4: 80
# First List: [10, 20, 30, 40, 50]
# Second List: [20, 40, 60, 80]
# Common Elements: [20, 40]

numbers1 = []
n1 = int(input("Enter first list size: "))
for i in range(n1):
    number1 = int(input(f"Enter number {i+1}: "))
    numbers1.append(number1)

numbers2 = []
n2 = int(input("Enter second list size: "))
for i in range(n2):
    number2 = int(input(f"Enter number {i+1}: "))
    numbers2.append(number2)

common = []

for i in numbers1:
    for j in numbers2:
        if i == j and i not in common:
            common.append(i)

print(f"First List: {numbers1}")
print(f"Second List: {numbers2}")

if common:
    print(f"Common Elements: {common}")
else:
    print("No common elements found.")