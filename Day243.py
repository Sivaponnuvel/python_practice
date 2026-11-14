# Question 1: Move All Zeros to the End of a List
# Interview Topics: Lists, Loops, Conditional Statements
# Write a Python function named move_zeros(numbers) to move all zeros to the end of a list while maintaining the relative order of non-zero elements.
# Requirements:
# 1. Create a function named move_zeros(numbers).
# 2. Move all zeros to the end of the list.
# 3. Maintain the original order of non-zero elements.
# 4. Do not use sort(), sorted(), or filter().
# 5. Return a new list.
# 6. Do not modify the original list.
# Examples:
# Example 1:
# Input:numbers = [0, 1, 0, 3, 12]Output:[1, 3, 12, 0, 0]
# Example 2:
# Input:numbers = [0, 0, 1, 2, 3]Output:[1, 2, 3, 0, 0]
# Example 3:
# Input:numbers = [1, 2, 3]Output:[1, 2, 3]
# Example 4:
# Input:numbers = [0, 0, 0]Output:[0, 0, 0]

def move_zeros(numbers):
    non_zeros = []
    zero_count = 0

    for i in numbers:
        if i == 0:
            zero_count += 1
        else:
            non_zeros.append(i)

    return non_zeros + [0] * zero_count

numbers = list(map(int, input("Enter numbers: ").split()))
print(move_zeros(numbers))


