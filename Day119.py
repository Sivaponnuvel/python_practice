# 🔹 Question 1 – Interview Question: Palindrome String Checker
# Write a Python program to check whether a given string is a palindrome.
# A palindrome reads the same forwards and backwards.
# Example 1
# Enter String: madam
# Palindrome ✅
# Example 2
# Enter String: level
# Palindrome ✅
# Example 3
# Enter String: python
# Not a Palindrome ❌
# Conditions
# ✅ Take input from the user.
# ✅ Ignore uppercase/lowercase differences.
# ✅ Use string slicing ([::-1]).
# ❌ Don't use loops to reverse the string.
# ❌ Don't use any built-in palindrome functions.

string = input("Enter String: ")
string = string.lower()
palin = string[::-1]

if string == palin:
    print("Palindrome ✅")
else:
    print("Not a Palindrome ❌")


