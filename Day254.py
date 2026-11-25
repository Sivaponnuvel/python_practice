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


