# Question 1: Check Whether a String Is a Palindrome 
# Interview Topic: Strings, Loops, Conditional Statements
# Write a Python function named is_palindrome(text) to check whether a given string is a palindrome.
# A palindrome reads the same forward and backward.
# Requirements:
# 1. Create a function named is_palindrome(text).
# 2. Ignore uppercase and lowercase differences.
# 3. Ignore spaces.
# 4. Return True if the string is a palindrome.
# 5. Otherwise, return False.
# Example 1:
# Input:
# text = "Madam"
# Expected Output:
# True
# Example 2:
# Input:
# text = "Python"
# Expected Output:
# False
# Example 3:
# Input:
# text = "nurses run"
# Expected Output:
# True

def is_palindrome(text):
    text = text.lower()
    text = text.replace(" ", "")

    rev = ""
    for i in text:
        rev = i + rev

    if rev == text:
        return True
    else:
        return False


text = input("Enter a text: ")
print(is_palindrome(text))


