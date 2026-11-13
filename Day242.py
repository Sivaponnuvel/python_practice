# Question 1: Find the Missing Number in a List
# Interview Topics: Lists, Loops, Arithmetic Operators
# Write a Python function named find_missing_number(numbers) to find the missing number in a list containing integers from 1 to n.
# Requirements:
# 1. Create a function named find_missing_number(numbers).
# 2. The list contains numbers from 1 to n, with exactly one number missing.
# 3. Find the missing number using a mathematical formula.
# 4. Do not use set(), sort(), or sorted().
# 5. Do not modify the original list.
# 6. Return the missing number.
# Examples:
# Example 1:
# Input:numbers = [1, 2, 4, 5, 6]Output:3
# Example 2:
# Input:numbers = [1, 3]Output:2
# Example 3:
# Input:numbers = [2, 3, 4, 5, 6]Output:1
# Example 4:
# Input:numbers = [1, 2, 3, 4]Output:5

def find_missing_number(numbers):
    n = len(numbers) + 1

    excepted_sum = (n * (n + 1)) // 2
    actual_sum = 0

    for i in numbers:
        actual_sum += i

    return excepted_sum - actual_sum

numbers = list(map(int, input("Enter numbers: ").split()))
print(find_missing_number(numbers))


