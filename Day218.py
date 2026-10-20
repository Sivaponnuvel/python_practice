# 🔹 Question 1 – String Coding Problem
# Topic: Strings, Loops and Conditional Statements
# Write a Python program to count the frequency of each character in a given string.
# Example:
# string = "programming"
# Expected output:
# p: 1
# r: 2
# o: 1
# g: 2
# a: 1
# m: 2
# i: 1
# n: 1
# Requirements:
# 1. Get a string from user input.
# 2. Count how many times each character appears.
# 3. Display each character and its frequency.
# 4. Display each character only once in the output.
# Conditions:
# - Use a dictionary to store character frequencies.
# - Use a loop and conditional statements.
# - Do not use collections.Counter.
# - Do not use external libraries.
# - Do not hardcode the output.
# - Preserve the order of each character's first appearance.

string = input("Enter a string: ")

freq = {}

for i in string:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

for key, value in freq.items():
    print(f"{key}: {value}")


