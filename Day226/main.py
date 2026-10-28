# 🔹 Question 1 – String Coding Problem
# Topic: Strings, Loops and Conditional Statements
# Write a Python program to find the first non-repeating character in a given string.
# Example 1:
# string = "swiss"
# Expected output:
# First Non-Repeating Character: w
# Example 2:
# string = "aabbccdde"
# Expected output:
# First Non-Repeating Character: e
# Example 3:
# string = "aabbcc"
# Expected output:
# No non-repeating character found
# Requirements
# 1. Get a string from user input.
# 2. Find the first character that appears exactly once.
# 3. Preserve the original order of characters.
# 4. Display the first non-repeating character.
# 5. Handle the case where every character is repeated.
# 6. Your program should work for different input strings.
# Conditions
# - Use loops and conditional statements.
# - You may use a dictionary.
# - Do not use collections.Counter.
# - Do not use count().
# - Do not use external libraries.
# - Do not hardcode the output.
# - Treat uppercase and lowercase letters as different characters.

string = input("Enter a string: ")

found  = False

for i in string:
    count = 0
    
    for j in string:
        if i == j:
            count += 1
    if count == 1:
        found = True
        break

if found:
    print(f"First Non-Repeating Character: {i}")
else:
    print("No non-repeating character found")


