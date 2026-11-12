# Question 1: Find the Second Largest Distinct Number in a List
# Interview Topics: Lists, Loops, Conditional Statements
# Write a Python function named second_largest(numbers) to find the second largest distinct number in a list.
# Requirements:
# 1. Create a function named second_largest(numbers).
# 2. Find the second largest distinct number using a loop.
# 3. Do not use sort(), sorted(), max(), or set().
# 4. Handle duplicate numbers correctly.
# 5. If the list contains fewer than two distinct numbers, return None.
# 6. Do not modify the original list.
# Examples:
# Example 1:
# Input:numbers = [10, 5, 20, 8, 20, 15]Output:15
# Example 2:
# Input:numbers = [5, 5, 5]Output:None
# Example 3:
# Input:numbers = [10, 20]Output:10
# Example 4:
# Input:numbers = [-5, -10, -2, -8]Output:-5

def second_largest(numbers):
    largest_num = None
    second_largest_num = None

    for i in numbers:
        if largest_num is None or i > largest_num:
            second_largest_num = largest_num
            largest_num = i
        elif (second_largest_num is None or i > second_largest_num) and i != largest_num:
            second_largest_num = i

    return second_largest_num

numbers = list(map(int, input("Enter numbers: ").split()))
print(second_largest(numbers))


