# Question 1: Find the First Repeated Word in a String
# Interview Topic: Strings, Lists, Sets, and Loops
# Write a Python function that finds the first word that appears more than once in a given sentence.
# Requirements
# 1. Create a function named first_repeated_word(sentence).
# 2. Treat uppercase and lowercase words as the same.
# 3. Return the first word whose second occurrence is encountered.
# 4. If no word is repeated, return None.
# 5. Ignore basic punctuation such as commas and full stops.
# Example 1
# Input:
# sentence = "Python is easy and Python is powerful"
# Expected Output:
# python
# Example 2
# Input:
# sentence = "Django makes web development easier"
# Expected Output:
# None
# Example 3
# Input:
# sentence = "Code well, test well, deploy well."
# Expected Output:
# well

def first_repeated_word(sentence):
    sentence = sentence.lower()
    for ch in ",.":
        sentence = sentence.replace(ch, "")

    words = sentence.split()

    seen = set()

    for i in words:
        if i in seen:
            return i
        seen.add(i)
    
    return None

sentence = input("Enter the sentence: ")
print(first_repeated_word(sentence))


