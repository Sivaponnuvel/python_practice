# 🔹 Question 1 – Custom Iterator Coding Problem
# Topic: Classes, Iterators, __iter__() and __next__()
# Write a Python program to create a custom iterator that generates numbers divisible by 3 from 1 to a given number n.
# Example 1
# Input:
# n = 15
# Expected output:
# Numbers Divisible by 3: 3 6 9 12 15
# Example 2
# Input:
# n = 10
# Expected output:
# Numbers Divisible by 3: 3 6 9
# Example 3
# Input:
# n = 2
# Expected output:
# Numbers Divisible by 3:
# Requirements
# 1. Get an integer n from the user.
# 2. Create a class named DivisibleByThree.
# 3. Implement the __init__(self, n) method.
# 4. Implement the __iter__(self) method.
# 5. Implement the __next__(self) method.
# 6. Generate numbers divisible by 3 between 1 and n, inclusive.
# 7. Raise StopIteration when no more numbers are available.
# 8. Use a for loop to iterate over the custom iterator.
# 9. Display the numbers in increasing order.
# 10. If n < 3, display only Numbers Divisible by 3:.
# Conditions
# - Must use a class-based custom iterator.
# - Must implement both __iter__() and __next__().
# - Must raise StopIteration appropriately.
# - Do not use yield.
# - Do not create a list to store the generated numbers.
# - Do not import libraries.
# - Do not hardcode the output.

class DivisibleByThree:
    def __init__(self, n):
        self.n = n
        self.current  = 3

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            num = self.current
            self.current += 3
            return num
        else:
            raise StopIteration

n = int(input("Enter n: "))

print("Numbers Divisible by 3:", end=" ")
for num in DivisibleByThree(n):
    print(num, end=" ")


# 🔹 Question 2 – Dictionary Comprehension Coding Problem
# Topic: Dictionaries, Dictionary Comprehension, Strings and Conditional Statements
# Write a Python program to count the frequency of each vowel in a given string using dictionary comprehension.
# Count only vowels that appear in the string, ignoring uppercase and lowercase differences.
# Example 1
# Input:
# text = "Programming Education"
# Expected output:
# Vowel Frequency: {'a': 2, 'e': 1, 'i': 2, 'o': 2, 'u': 1}
# Example 2
# Input:
# text = "HELLO WORLD"
# Expected output:
# Vowel Frequency: {'e': 1, 'o': 2}
# Example 3
# Input:
# text = "Python"
# Expected output:
# Vowel Frequency: {'o': 1}
# Requirements
# 1. Get a string from the user.
# 2. Convert the string to lowercase for case-insensitive counting.
# 3. Use dictionary comprehension to create the frequency dictionary.
# 4. Count only the vowels a, e, i, o, u.
# 5. Include only vowels that appear at least once.
# 6. Display the dictionary with vowel keys in alphabetical order.
# 7. Handle an empty string or a string without vowels by displaying an empty dictionary.
# Conditions
# - Must use dictionary comprehension.
# - Must use count() to calculate each vowel's frequency.
# - Do not use collections.Counter.
# - Do not use explicit for or while loops for counting.
# - Do not import libraries.
# - Do not hardcode the final output.
# - Your solution should work for different strings.

string = input("Enter string: ").lower()

freq = {vowel: string.count(vowel) for vowel in "aeiou" if string.count(vowel) > 0}

print(f"Vowel Frequency: {freq}")