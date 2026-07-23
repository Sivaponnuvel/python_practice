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


