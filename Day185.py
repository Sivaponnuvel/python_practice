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


# 🔹 Question 2 – Recursion: Sum of Numbers
# Write a Python program using recursion to calculate the sum of numbers from 1 to n.
# Example Input:
# Enter a number: 5
# Expected Output:
# Sum: 15
# Because:
# 1 + 2 + 3 + 4 + 5 = 15
# Conditions:
# Create a recursive function.
# The function should accept n.
# Use a base condition to stop the recursion.
# Do not use a for or while loop.
# Do not use Python's built-in sum().
# Example 2:
# Enter a number: 10
# Expected:
# Sum: 55

def sum_of_num(n):
    if n == 0:
        return 0
    else:
        return n + sum_of_num(n - 1)

number = int(input("Enter a number: "))
print(f"Sum: {sum_of_num(number)}")