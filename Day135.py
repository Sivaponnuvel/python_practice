# 🔹 Question 1 – Lambda + map(): Square All Numbers
# Write a Python program to create a new list containing the square of every number using lambda and map().
# Program Flow
# Take space-separated integers from the user.
# Convert them into a list.
# Use map() with a lambda function to calculate the square of each number.
# Convert the result into a list.
# Display the squared numbers.
# Example
# Input
# Enter Numbers: 2 4 6 8
# Output
# Squared Numbers:
# 4 16 36 64
# ⚠️ Conditions
# ✅ Take input from the user
# ✅ Use lambda
# ✅ Use map()
# ✅ Convert the result into a list
# ❌ Don't use a for loop to calculate the squares
# ❌ Don't create a separate function using def

numbers = list(map(int, input("Enter Numbers: ").split()))

squared_numbers = list(map(lambda x: x**2, numbers))

print("Squared Numbers:")
print(*squared_numbers)


# 🔹 Question 2 – Intermediate Interview Question: Longest Word in a Sentence
# Write a Python program to find the longest word in a sentence.
# If multiple words have the same maximum length, display the first one.
# Program Flow
# Take a sentence from the user.
# Split the sentence into words.
# Find the longest word.
# Display the longest word and its length.
# Example 1
# Input
# Enter a Sentence: Python is an amazing programming language
# Output
# Longest Word : programming
# Length       : 11
# Example 2
# Input
# Enter a Sentence: I love coding
# Output
# Longest Word : coding
# Length       : 6
# ⚠️ Conditions
# ✅ Take input from the user
# ✅ Use split()
# ✅ Use a loop
# ✅ Display the first longest word if there is a tie
# ❌ Don't use max()
# ❌ Don't sort the words
# ❌ Don't import any libraries

sentence = input("Enter a Sentence: ").split()
longest_word = sentence[0]
for i in sentence:
    if len(i) >= len(longest_word):
        longest_word = i

print(f"Longest Word : {longest_word}")
print(f"Length       : {len(longest_word)}")