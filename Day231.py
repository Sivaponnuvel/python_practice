# 🔹 Question 1 – String Coding Problem
# Topic: Strings, Dictionaries and Loops
# Write a Python program to find the first non-repeating character in a given string.
# Example 1
# Input:
# text = "programming"
# Expected output:
# First Non-Repeating Character: p
# Example 2
# Input:
# text = "aabbcddee"
# Expected output:
# First Non-Repeating Character: c
# Example 3
# Input:
# text = "aabbcc"
# Expected output:
# No non-repeating character found
# Requirements
# 1. Get a string from the user.
# 2. Find the frequency of each character.
# 3. Identify the first character whose frequency is exactly 1.
# 4. Preserve the original character order.
# 5. Display the first non-repeating character.
# 6. If no such character exists, display the appropriate message.
# Conditions
# - Use Python strings and dictionaries.
# - Do not use collections.Counter.
# - Do not sort the string.
# - Do not hardcode the output.
# - Your solution should work for different strings.

text = input("Enter text: ")

freq = {}

for i in text:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

for i in text:
    if freq[i] == 1:
        print(f"First Non-Repeating Character: {i}")
        break
else:
    print("No non-repeating character found")


