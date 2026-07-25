# 🔹 Question 1 – Functions (*args): Find the Largest Number
# Write a Python program using *args to find the largest number among the given values.
# Program Flow
# Create a function named find_largest(*args).
# Accept any number of integer arguments.
# Find the largest number.
# Return the result.
# Call the function and display the output.
# Example
# Call
# find_largest(12, 45, 8, 99, 34)
# Output
# Largest Number: 99
# ⚠️ Conditions
# ✅ Use *args
# ✅ Use a loop
# ✅ Return the result
# ✅ Display the returned value
# ❌ Don't use max()
# ❌ Don't sort the values

def find_largest(*args):
    if not args:
        return None
    
    largest = args[0]
    for i in args:
        if largest < i:
            largest = i
    return largest

print(f"Largest Number: {find_largest(7, 21, 35, 77, 50)}")


# 🔹 Question 2 – Intermediate Interview Question: Find Duplicate Characters
# Write a Python program to display all characters that appear more than once in a string, along with their frequencies.
# Program Flow
# Take a string from the user.
# Count the frequency of each character.
# Display only the duplicate characters and their counts.
# Preserve the order of first occurrence.
# Example 1
# Input
# Enter a String: programming
# Output
# r : 2
# g : 2
# m : 2
# Example 2
# Input
# Enter a String: python
# Output
# No Duplicate Characters ❌
# ⚠️ Conditions
# ✅ Take input from the user
# ✅ Use a dictionary
# ✅ Use loops
# ✅ Preserve the original order
# ❌ Don't use collections.Counter
# ❌ Don't import any libraries
# ❌ Don't print the same duplicate character more than once

def find_duplicate_char(string):
    count = {}
    for i in string:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    found = False
    for char, freq in count.items():
        if freq > 1:
            print(f"{char} : {freq}")
            found = True
    if not found:
        print("No Duplicate Characters ❌")

string = input("Enter a String: ")
find_duplicate_char(string)