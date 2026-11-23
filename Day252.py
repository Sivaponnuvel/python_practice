# Question 1 – Find the Missing Number in a List
# Interview Topics: Lists, Loops, Mathematical Operations, Conditional Logic.
# You are given a list containing numbers from 1 to n, but one number is missing. Find the missing number.
# Requirements:
# 1. Get the value of n from the user.
# 2. Get n-1 integer values from the user.
# 3. Store the values in a list.
# 4. Find the missing number without using sort() or sorted().
# 5. Display the missing number.
# 6. Use your own logic.
# Expected Output:
# Enter n: 5
# Enter number 1: 1
# Enter number 2: 2
# Enter number 3: 4
# Enter number 4: 5
# Original List: [1, 2, 4, 5]
# Missing Number: 3

n = int(input("Enter n: "))
numbers = []

for i in range(n-1):
    number = int(input(f"Enter number {i+1}: "))
    numbers.append(number)

num = len(numbers) + 1
excepted_sum = num * (num + 1) // 2
actual_sum = sum(numbers)

missing_number = excepted_sum - actual_sum

print(f"Original List: {numbers}")
print(f"Missing Number: {missing_number}")


