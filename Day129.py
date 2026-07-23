# 🔹 Question 1 – String Methods: Count Vowels and Consonants
# Write a Python program to count the number of vowels and consonants in a string.
# Program Flow
# Take a string from the user.
# Count the total number of vowels.
# Count the total number of consonants.
# Ignore spaces.
# Display both counts.
# Example
# Input
# Enter a String: Python Programming
# Output
# Vowels     : 4
# Consonants : 13
# ⚠️ Conditions
# ✅ Take input from the user
# ✅ Use string methods (lower(), isalpha())
# ✅ Use a loop
# ✅ Ignore spaces and special characters
# ❌ Don't import any libraries
# ❌ Don't use regular expressions

string = input("Enter a String: ").lower()
count_vowel = 0
count_consonant = 0

for i in string:
    if i in "aeiou":
        count_vowel += 1
    elif i.isalpha():
        count_consonant += 1

print(f"Vowels     : {count_vowel}")
print(f"Consonants : {count_consonant}")


# 🔹 Question 2 – Intermediate Interview Question: First Non-Repeating Character
# Write a Python program to find the first non-repeating character in a string.
# Program Flow
# Take a string from the user.
# Find the first character that appears only once.
# Display that character.
# If every character repeats, display:
# No Non-Repeating Character ❌
# Example 1
# Input
# Enter a String: swiss
# Output
# First Non-Repeating Character: w
# Example 2
# Input
# Enter a String: aabbcc
# Output
# No Non-Repeating Character ❌
# ⚠️ Conditions
# ✅ Take input from the user
# ✅ Use a dictionary
# ✅ Use a loop
# ✅ Preserve the original order
# ❌ Don't use collections.Counter
# ❌ Don't import any libraries

def first_non_repeating(user):
    count = {}
    for i in user:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    found = False
    for i in user:
        if count[i] == 1:
            print(f"First Non-Repeating Character: {i}")
            found = True
            return
    if not found:
        print("No Non-Repeating Character ❌")

user = input("Enter a String: ")
first_non_repeating(user)