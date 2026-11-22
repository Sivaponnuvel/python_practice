# Question 1 – Maximum Sum of 3 Consecutive Elements
# Interview Topics: Lists, Sliding Window, for Loop, Conditional Statements, Variables.
# Given an array of integers and a number n = 3, find the maximum sum of any 3 consecutive elements in the array.
# Requirements:
# 1. Get 5 or more integer values from the user using input().
# 2. Store the values in a list.
# 3. Set n = 3.
# 4. Find the sum of every possible group of 3 consecutive elements.
# 5. Identify the maximum sum.
# 6. Display the maximum sum and its corresponding 3 elements.
# 7. Do not use sort() or sorted().
# Expected Output:
# Enter how many numbers: 6
# Enter number 1: 2
# Enter number 2: 1
# Enter number 3: 5
# Enter number 4: 1
# Enter number 5: 3
# Enter number 6: 2
# Original List: [2, 1, 5, 1, 3, 2]
# Maximum Sum: 9
# Consecutive Elements: [5, 1, 3]

nums = int(input("Enter how many numbers: "))
numbers = []
n = 3

for i in range(nums):
    number = int(input(f"Enter number {i+1}: "))
    numbers.append(number)

max_sum = 0
consecutive_element = []

for i in range(len(numbers) - n + 1):
    consecutive_nums = numbers[i:i+n]
    current_number = sum(consecutive_nums)    

    if current_number > max_sum:
        max_sum = current_number
        consecutive_element = consecutive_nums

print(f"Original List: {numbers}")
print(f"Maximum Sum: {max_sum}")
print(f"Consecutive Elements: {consecutive_element}")


# Question 2 – Maximum Consecutive Character Count
# Interview Topics: Strings, for Loop, Conditional Statements, Character Comparison, Counter Variables.
# Given a string, find the character that appears consecutively the maximum number of times.
# Return the character and its consecutive count.
# Requirements:
# 1. Get a string from the user using input().
# 2. Find the maximum consecutive character count.
# 3. Identify the character with the maximum consecutive occurrence.
# 4. Display the character and its consecutive count.
# 5. Do not use Counter() or dictionary frequency counting.
# 6. If multiple characters have the same maximum consecutive count, return the first character that achieved that maximum.
# Expected Output:
# Enter a string: aaabbccccddeee
# Character: c
# Consecutive Count: 4
# Another example:
# Enter a string: aaabbbcc
# Character: a
# Consecutive Count: 3

string = input("Enter a string: ")

max_count = 0
current_count = 1
result = ""

for i in range(1, len(string)):
    if string[i] == string[i - 1]:
        current_count += 1
    else:
        current_count = 1

    if current_count > max_count:
        max_count = current_count
        result = string[i]

print(f"Character: {result}")
print(f"Consecutive Count: {max_count}")