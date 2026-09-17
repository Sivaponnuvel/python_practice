# 🔹 Question 1 – Count Frequency of Characters in a String
# Write a Python program to count how many times each character appears in a given string.
# Example Input:
# Enter a string: hello
# Expected Output:
# Character frequency:
# h: 1
# e: 1
# l: 2
# o: 1
# Conditions:
# Get the string from the user.
# Count the frequency of each character.
# Maintain the order in which characters first appear.
# Use a dictionary.
# Do not use collections.Counter.
# Spaces can be ignored.
# Example 2:
# Enter a string: python
# Expected:
# Character frequency:
# p: 1
# y: 1
# t: 1
# h: 1
# o: 1
# n: 1

string = input("Enter a string: ")
freq = {}
for i in string:
    if i != " ":
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

print("Character frequency:")
for key, value in freq.items():
    print(f"{key}: {value}")


