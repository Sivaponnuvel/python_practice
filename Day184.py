# 🔹 Question 1 – Count Vowels in a String
# Write a Python program to count the number of vowels in a given string.
# Requirements:
# Get a string from the user.
# Count a, e, i, o, u.
# Both uppercase and lowercase vowels should be counted.
# Print the total vowel count.
# Example Input:
# Enter a string: Python Full Stack Developer
# Expected Output:
# Total vowels: 7
# Conditions:
# Use a loop.
# Do not use any external library.
# A, E, I, O, U should also be treated as vowels.

def countVowel(string):
    count = 0
    for i in string:
        if i in "aeiouAEIOU":
            count += 1
    return count

string = input("Enter a string: ")
print(f"Total vowels: {countVowel(string)}")


# 🔹 Question 2 – Remove Duplicates from a List
# Write a Python program to remove duplicate values from a list while maintaining the original order.
# Example Input:
# Enter numbers: 10 20 10 30 20 40 30
# Expected Output:
# List after removing duplicates: [10, 20, 30, 40]
# Conditions:
# Get the numbers from the user.
# Remove duplicate values.
# Maintain the original order.
# Do not simply use set() for the solution.

numbers = list(map(int, input("Enter numbers: ").split()))
nums = []
for i in numbers:
    if i not in nums:
        nums.append(i)
print(f"List after removing duplicates: {nums}")