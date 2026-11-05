# Question 1: Find the Most Frequent Character in a String
# Interview Topic: Strings, Dictionaries, and Loops
# Write a Python function named most_frequent_char(text) that finds the character appearing most frequently in a string.
# Requirements
# 1. Count the frequency of each character.
# 2. Ignore spaces.
# 3. Treat uppercase and lowercase characters as the same.
# 4. Return the character with the highest frequency.
# 5. If multiple characters have the same highest frequency, return the character that appears first in the original string.
# 6. If the input contains only spaces or is empty, return None.
# Example 1
# Input:
# text = "programming"
# Expected Output:
# r
# Example 2
# Input:
# text = "Hello World"
# Expected Output:
# l
# Example 3
# Input:
# text = "aabb"
# Expected Output:
# a

def most_frequent_char(text):
    text = text.lower()

    freq = {}

    for i in text:
        if i != " ":
            freq[i] = freq.get(i, 0) + 1

    if not freq:
        return None

    for i in text:
        if i != " " and freq[i] == max(freq.values()):
            return i 

text = input("Enter a text: ")
print(most_frequent_char(text))


