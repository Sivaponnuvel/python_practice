# 🔹 Question 1 – Count Vowels in a String
# Write a Python program to count the number of vowels in a given string.
# Requirements:
# Get a string from the user.
# Count a, e, i, o, u.
# Both uppercase and lowercase vowels should be counted.
# Print the total vowel count.
# Example Input:
# Enter a string: Python Full Stack Developer
# Expected Output:
# Total vowels: 7
# Conditions:
# Use a loop.
# Do not use any external library.
# A, E, I, O, U should also be treated as vowels.

def countVowel(string):
    count = 0
    for i in string:
        if i in "aeiouAEIOU":
            count += 1
    return count

string = input("Enter a string: ")
print(f"Total vowels: {countVowel(string)}")


