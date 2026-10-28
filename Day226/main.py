# 🔹 Question 1 – String Coding Problem
# Topic: Strings, Loops and Conditional Statements
# Write a Python program to find the first non-repeating character in a given string.
# Example 1:
# string = "swiss"
# Expected output:
# First Non-Repeating Character: w
# Example 2:
# string = "aabbccdde"
# Expected output:
# First Non-Repeating Character: e
# Example 3:
# string = "aabbcc"
# Expected output:
# No non-repeating character found
# Requirements
# 1. Get a string from user input.
# 2. Find the first character that appears exactly once.
# 3. Preserve the original order of characters.
# 4. Display the first non-repeating character.
# 5. Handle the case where every character is repeated.
# 6. Your program should work for different input strings.
# Conditions
# - Use loops and conditional statements.
# - You may use a dictionary.
# - Do not use collections.Counter.
# - Do not use count().
# - Do not use external libraries.
# - Do not hardcode the output.
# - Treat uppercase and lowercase letters as different characters.

string = input("Enter a string: ")

found  = False

for i in string:
    count = 0
    
    for j in string:
        if i == j:
            count += 1
    if count == 1:
        found = True
        break

if found:
    print(f"First Non-Repeating Character: {i}")
else:
    print("No non-repeating character found")


# 🔹 Question 2 – File Handling Coding Problem
# Topic: File Handling, Functions and Exception Handling
# Write a Python program to count the number of lines, words, and characters in a text file.
# Example file: sample.txt
# Python is easy
# I am learning Python
# File handling is important
# Expected output:
# Total Lines: 3
# Total Words: 11
# Total Characters: 62
# For this question, characters include letters, spaces, punctuation, and newline characters (\n).
# Requirements
# 1. Create a text file named sample.txt.
# 2. Write the three example lines into the file.
# 3. Create a function named file_statistics(filename).
# 4. Open the file in read mode.
# 5. Count the total number of lines.
# 6. Count the total number of words.
# 7. Count the total number of characters, including newline characters.
# 8. Display all three counts.
# 9. Handle FileNotFoundError if the file does not exist.
# Conditions
# - Use with open() for file operations.
# - Use loops to count lines, words, and characters.
# - Use try-except to handle missing files.
# - Do not import external libraries.
# - Do not hardcode the calculated counts.
# - Do not use readlines().

filename = "D:/Backend/Python/Own try/python_practice/Day226/sample.txt"

with open(filename, "w")as file:
    file.write("Python is easy\n")
    file.write("I am learning Python\n")
    file.write("File handling is important")

def file_statistics(filename):
    try:
        line_count = 0
        word_count = 0
        char_count = 0 

        with open(filename)as file:
            for i in file:
                line_count += 1
                word_count += len(i.split())

                for j in i:
                    char_count += 1

        print(f"Total Lines: {line_count}")
        print(f"Total Words: {word_count}")
        print(f"Total Characters: {char_count}")

    except FileNotFoundError:
        print("Error: File not found.")

file_statistics(filename)