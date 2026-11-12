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


# Question 2: Check Whether Two Strings Are Anagrams
# Interview Topics: Strings, Loops, Dictionaries, Conditional Statements
# Write a Python function named are_anagrams(str1, str2) to check whether two strings are anagrams.
# Two strings are anagrams if they contain the same characters with the same frequencies, regardless of their order.
# Requirements:
# 1. Create a function named are_anagrams(str1, str2).
# 2. Ignore uppercase and lowercase differences.
# 3. Compare character frequencies.
# 4. Do not use sorted() or sort().
# 5. Do not use external libraries.
# 6. Return True if both strings are anagrams; otherwise, return False.
# Examples:
# Example 1:
# Input:str1 = "listen"str2 = "silent"Output:True
# Example 2:
# Input:str1 = "hello"str2 = "world"Output:False
# Example 3:
# Input:str1 = "Triangle"str2 = "Integral"Output:True
# Example 4:
# Input:str1 = "aabb"str2 = "abab"Output:True

def are_anagrams(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    if len(str1) != len(str2):
        return False

    char_count = {}

    for i in str1:
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1

    for i in str2:
        if i not in char_count:
            return False

        char_count[i] -= 1

        if char_count[i] < 0:
            return False

    for i in char_count.values():
        if i != 0:
            return False

    return True

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
print(are_anagrams(str1, str2))