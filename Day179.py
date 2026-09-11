# 🔹 Question 1 – Reverse a Sentence
# Write a Python program to reverse the order of words in a sentence.
# Input:
# Enter a sentence: Python is easy
# Expected Output:
# Reversed sentence: easy is Python
# ⚠️ Conditions
# ✅ Use input()
# ✅ Store the sentence in a variable
# ✅ Reverse the word order
# ✅ Use a loop
# ❌ Don't use libraries
# ❌ Don't use a predefined sentence
# ❌ Don't use reversed()
# ❌ Don't use .reverse()

def reverse_sentence(sentence):
    words = sentence.split()
    rev_sentence = ""

    for i in words:
        rev_sentence = i + " " + rev_sentence

    print(f"Reversed sentence: {rev_sentence.strip()}")

sentence = input("Enter a sentence: ")
reverse_sentence(sentence)


# 🔹 Question 2 – Palindrome String
# Write a Python program to check whether a given word is a palindrome.
# A palindrome reads the same from both directions.
# Input:
# Enter a word: madam
# Expected Output:
# madam is a Palindrome ✅
# For a non-palindrome:
# Input:
# Enter a word: python
# Expected Output:
# python is Not a Palindrome ❌
# ⚠️ Conditions
# ✅ Use input()
# ✅ Use a loop
# ✅ Compare the original word with its reversed form
# ❌ Don't use [::-1]
# ❌ Don't use reversed()
# ❌ Don't use .reverse()
# ❌ Don't use libraries
# ❌ Don't use a predefined word

def is_palindrome(word):
    rev_word = ""
    for i in word:
        rev_word = i + rev_word

    if word == rev_word:
        print(f"{word} is a Palindrome ✅")
    else:
        print(f"{word} is Not a Palindrome ❌")

word = input("Enter a word: ")
is_palindrome(word)