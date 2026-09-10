# 🔹 Question 1 – Reverse a Word
# Write a Python program to reverse a word entered by the user.
# Program Flow
# Input:
# Enter a word: Python
# Expected Output:
# Reversed word: nohtyP
# ⚠️ Conditions
# ✅ Use input()
# ✅ Store the word in a variable
# ✅ Reverse the word
# ✅ Display the reversed word
# ❌ Don't use libraries
# ❌ Don't use a predefined word
# ❌ Don't use a function such as reverse()

def rev_word(word):
    rev = ""
    for i in word:
        rev = i + rev
    return rev

word = input("Enter a word: ")
print(f"Reversed word: {rev_word(word)}")


