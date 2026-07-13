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


# 🔹 Question 2 – Interview Question: Reverse Each Word in a Sentence
# Write a Python program to reverse each word in a sentence while keeping the word order the same.
# Example 1
# Enter Sentence:
# Python is awesome
# Output:
# nohtyP si emosewa
# Example 2
# Enter Sentence:
# I love coding
# Output:
# I evol gnidoc
# Example 3
# Enter Sentence:
# No Words Found ❌
# Conditions
# ✅ Take input from the user.
# ✅ Use split().
# ✅ Use a loop.
# ✅ Reverse each word using slicing ([::-1]).
# ✅ Join the words using " ".join().
# ❌ Don't reverse the entire sentence.
# ❌ Don't use reversed() or external libraries.

sentence = input("Enter Sentence: ").strip()

if sentence == "":
    print("No Words Found ❌")
else:
    words = sentence.split()
    for i in range(len(words)):
        words[i] = words[i][::-1]
    print(" ".join(words))