# Question 1: Find the Factorial of a Number
# Interview Topic: Functions, Loops, Conditional Statements
# Write a Python function named factorial(n) to calculate the factorial of a given number.
# Requirements:
# 1. Create a function named factorial(n).
# 2. Calculate factorial using a loop.
# 3. Do not use math.factorial().
# 4. If the input is 0, return 1.
# 5. If the input is negative, return "Invalid input".
# Example 1:
# Input:
# n = 5
# Expected Output:
# 120
# Example 2:
# Input:
# n = 0
# Expected Output:
# 1
# Example 3:
# Input:
# n = -3
# Expected Output:
# Invalid input

def factorial(n):
    if n < 0:
        return "Invalid input"
    
    fact = 1

    for i in range(1, n + 1):
        fact *= i
    
    return fact

n = int(input("Enter number: "))
print(factorial(n))


# Question 2: Count Vowels and Consonants in a String
# Interview Topic: Strings, Loops, Conditional Statements
# Write a Python function named count_vowels_consonants(text) to count the number of vowels and consonants in a given string.
# Requirements:
# 1. Create a function named count_vowels_consonants(text).
# 2. Count vowels (a, e, i, o, u).
# 3. Count consonants (other English alphabet letters).
# 4. Ignore uppercase and lowercase differences.
# 5. Ignore spaces, numbers, and special characters.
# 6. Return both counts in a dictionary.
# Example 1:
# Input:
# text = "Python Developer"
# Expected Output:
# {    "vowels": 5,    "consonants": 10}
# Example 2:
# Input:
# text = "Hello123!"
# Expected Output:
# {    "vowels": 2,    "consonants": 3}
# Example 3:
# Input:
# text = "12345"
# Expected Output:
# {    "vowels": 0,    "consonants": 0}

def count_vowels_consonants(text):
    text = text.lower()

    result = {"vowels": 0, "consonants": 0}

    for i in text:
        if i in "aeiou":
            result["vowels"] += 1
        elif i.isalpha():
            result["consonants"] += 1

    return result

text = input("Enter a text: ")
print(count_vowels_consonants(text))