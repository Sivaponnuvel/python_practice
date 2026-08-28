# 🔹 Question 1 – String + Function
# Create a function:
# count_vowels(text)
# The function should accept a string and return the total number of vowels (a, e, i, o, u).
# Example:
# text = "Python Programming"
# print(count_vowels(text))
# Expected Output:
# 4
# ⚠️ Conditions:
# Use a function
# Use a for loop
# Use an if condition
# Handle both uppercase and lowercase vowels
# Return the count

def count_vowels(text):
    count = 0
    for i in text:
        if i in "AEIOUaeiou":
            count += 1
    return count

text = "Python Programming"
print(count_vowels(text))


# 🔹 Question 2 – List + Function
# Create a function:
# find_largest(numbers)
# The function should accept a list of numbers and return the largest number without using max().
# Example:
# numbers = [45, 12, 89, 34, 67]
# print(find_largest(numbers))
# Expected Output:
# 89
# ⚠️ Conditions:
# Use a function
# Use a for loop
# Use an if condition
# ❌ Don't use max()
# Return the largest number

def find_largest(numbers):
    max_num = numbers[0]
    for i in numbers:
        if i > max_num:
            max_num = i
    return max_num

numbers = [45, 12, 89, 34, 67]
print(find_largest(numbers))