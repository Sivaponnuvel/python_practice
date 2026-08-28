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


