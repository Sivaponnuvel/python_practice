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


