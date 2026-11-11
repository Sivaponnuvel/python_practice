# Question 1: Check Whether a String Is a Palindrome
# Interview Topics: Strings, Functions, Conditional Statements
# Write a Python function named is_palindrome(text) to check whether a given string is a palindrome.
# Requirements:
# 1. Create a function named is_palindrome(text).
# 2. Check whether the string reads the same forward and backward.
# 3. Ignore uppercase and lowercase differences.
# 4. Do not use any external libraries.
# 5. Return True if it is a palindrome; otherwise, return False.
# Examples:
# Example 1:
# Input:text = "madam"Output:True
# Example 2:
# Input:text = "Python"Output:False
# Example 3:
# Input:text = "Level"Output:True

def is_palindrome(text):
    text = text.lower()
    rev = ""

    for i in text:
        rev = i + rev

    return rev == text

text = input("Enter text: ")
print(is_palindrome(text))


# Question 2: Remove Duplicates from a List
# Interview Topics: Lists, Loops, Conditional Statements
# Write a Python function named remove_duplicates(numbers) to remove duplicate elements from a list while preserving the original order.
# Requirements:
# 1. Create a function named remove_duplicates(numbers).
# 2. Remove duplicate elements using a loop.
# 3. Do not use set() or any external libraries.
# 4. Preserve the original order of elements.
# 5. Return a new list without duplicates.
# 6. Do not modify the original list.
# Examples:
# Example 1:
# Input:numbers = [1, 2, 2, 3, 1, 4, 3]Output:[1, 2, 3, 4]
# Example 2:
# Input:numbers = [5, 5, 5, 5]Output:[5]
# Example 3:
# Input:numbers = [1, 2, 3, 4]Output:[1, 2, 3, 4]
# Example 4:
# Input:numbers = []Output:[]

def remove_duplicates(numbers):
    freq = []

    for i in numbers:
        if i not in freq:
            freq.append(i)

    return freq

numbers = list(map(int, input("Enter numbers: ").split()))
print(remove_duplicates(numbers))