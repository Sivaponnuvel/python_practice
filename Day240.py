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


