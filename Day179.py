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

