# Question 1 – String Coding Problem
# Topic: Strings and Loops
# Write a Python program to check whether a given string is a palindrome.
# A palindrome is a string that reads the same forward and backward.
# Example 1:
# Enter a string: madam
# Palindrome
# Example 2:
# Enter a string: python
# Not a palindrome
# Requirements:
# 1. Get a string from user input.
# 2. Reverse the string using a loop. Do not use slicing ([::-1]).
# 3. Compare the original string with the reversed string.
# 4. Print Palindrome if both are equal; otherwise, print Not a palindrome.
# Conditions:
# - Use a loop to reverse the string.
# - Do not use built-in reverse methods.
# - Make your comparison case-sensitive. For example, Madam is not a palindrome under this rule.

string = input("Enter a string: ").lower()

rev_string = ""

for i in string:
    rev_string = i + rev_string

if string == rev_string:
    print("Palindrome")
else:
    print("Not a palindrome")


