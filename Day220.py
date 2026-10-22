# 🔹 Question 1 – String Coding Problem
# Topic: Strings, Loops and Conditional Statements
# Write a Python program to check whether two strings are anagrams of each other.
# Two strings are anagrams if they contain the same characters with the same frequencies, regardless of order.
# Example:
# string1 = "listen"string2 = "silent"
# Expected output:
# The strings are anagrams
# Another example:
# string1 = "hello"string2 = "world"
# Expected output:
# The strings are not anagrams
# Requirements:
# 1. Get two strings from user input.
# 2. Check whether both strings contain the same characters with the same frequencies.
# 3. Display whether they are anagrams.
# 4. Your program should work with different input strings.
# Conditions:
# - Use loops and conditional statements.
# - Do not use sorted().
# - Do not use collections.Counter.
# - Do not import external libraries.
# - Do not hardcode the result.
# - Treat uppercase and lowercase letters as different characters.

string1 = input("Enter a string1: ")
string2 = input("Enter a string2: ")

if len(string1) != len(string2):
    print("The strings are not anagrams")

else:
    is_anagram = True

    for char in string1:
        count1 = 0
        count2 = 0

        for i in string1:
            if i == char:
                count1 += 1

        for j in string2:
            if j == char:
                count2 += 1

        if count1 != count2:
            is_anagram = False
            break

    if is_anagram:
        print("The strings are anagrams")
    else:
        print("The strings are not anagrams")


