# 🔹 Question 1 – Interview Question: Count Character Frequency
# Write a Python program to count the frequency of each character in a string.
# Program Flow
# Take a string from the user.
# Count how many times each character appears.
# Display each character and its count.
# Example
# Input
# Enter a String: programming
# Output
# p : 1
# r : 2
# o : 1
# g : 2
# a : 1
# m : 2
# i : 1
# n : 1
# ⚠️ Conditions
# ✅ Take input from the user
# ✅ Use a dictionary
# ✅ Use a loop
# ✅ Preserve the order of first occurrence
# ❌ Don't use collections.Counter
# ❌ Don't import any libraries

def frequency(string):
    freq = {}
    for i in string:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq
string = input("Enter a String: ")
char_count = frequency(string)
for char, count in char_count.items():
    print(f"{char} : {count}")

