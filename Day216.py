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


# Question 2 – Dictionary Coding Problem
# Topic: Dictionaries and Conditional Statements
# Imagine you're developing a student marks management system. Write a Python program to find the student who scored the highest marks.
# Use this dictionary:
# students = {    "Arun": 85,    "Priya": 92,    "Kumar": 78,    "Divya": 95,    "Ravi": 88}
# Expected output:
# Top Student: Divya
# Highest Marks: 95
# Requirements:
# 1. Iterate through the dictionary using a loop.
# 2. Find the student with the highest marks.
# 3. Print the student's name and marks.
# 4. Do not hardcode the result.
# Conditions:
# - Use a loop to find the maximum.
# - Do not use max() or sort the dictionary.
# - Your solution should work if the marks change.

students = {
    "Arun": 85,
    "Priya": 92,
    "Kumar": 78,
    "Divya": 95,
    "Ravi": 88
}

top_mark = None
top_student  = ""

for name, mark in students.items():
    if top_mark is None or top_mark < mark:
        top_mark = mark
        top_student = name

print(f"Top Student: {top_student}")
print(f"Highest Marks: {top_mark}")