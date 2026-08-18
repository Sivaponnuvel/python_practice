# 🔹 Question 1 – String Methods: Count Vowels and Consonants
# Write a Python program to count the number of vowels and consonants in a string.
# Program Flow
# Take a string from the user.
# Convert the string to lowercase.
# Check each character.
# Count vowels: a, e, i, o, u
# Count consonants.
# Ignore spaces, numbers, and special characters.
# Display the counts.
# Example
# Input:
# Enter String: Python Programming
# Output:
# Vowels     : 4
# Consonants : 13
# ⚠️ Conditions
# ✅ Take input from the user
# ✅ Use a loop
# ✅ Use string methods such as lower()
# ✅ Use isalpha()
# ✅ Use in to check vowels
# ❌ Don't use regular expressions
# ❌ Don't import any libraries
# ❌ Don't use collections.Counter
# 💡 Hint
# vowels = "aeiou"
# You can check:
# if char.isalpha():
#     if char in vowels:
#         ...

user = input("Enter String: ").lower()

vowels_count = 0
consonants_count = 0
vowels = "aeiou"

for i in user:
    if i.isalpha():
        if i in vowels:
            vowels_count += 1
        else:
            consonants_count += 1

print(f"Vowels     : {vowels_count}")
print(f"Consonants : {consonants_count}")


# 🔹 Question 2 – String Interview: First Non-Repeating Character
# Write a Python program to find the first character that appears only once in a string.
# Example 1
# Input:
# Enter String: programmin
# Output:
# First Non-Repeating Character : p
# Example 2
# Input:
# Enter String: aabbcdd
# Output:
# First Non-Repeating Character : c
# Example 3
# Input:
# Enter String: aabbcc
# Output:
# No Non-Repeating Character ❌
# Program Flow
# Take a string from the user.
# Count the frequency of every character using a dictionary.
# Traverse the string again.
# Find the first character whose frequency is 1.
# Display that character.
# ⚠️ Conditions
# ✅ Take input from the user
# ✅ Use a dictionary
# ✅ Use loops
# ✅ Use string methods where appropriate
# ✅ Preserve original order
# ❌ Don't use Counter
# ❌ Don't use set() as the main solution
# ❌ Don't sort the string
# ❌ Don't use index() to solve the problem
# ❌ Don't import any libraries
# 💡 Hint
# First create something like:
# freq = {}

word = input("Enter String: ")

freq = {}

for i in word:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

found = False

for i in word:
    if freq[i] == 1:
        print(f"First Non-Repeating Character : {i}")
        found = True
        break

if not found:
    print("No Non-Repeating Character ❌")