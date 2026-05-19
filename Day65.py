# 🔹 Question 1 – Character Frequency Counter
# Write a Python program to:
# 👉 Take a string input from user
# 👉 Count how many times each character appears
# 👉 Store result in dictionary
# Example Input:
# programming
# Example Output:
# {
#     'p': 1,
#     'r': 2,
#     'o': 1,
#     'g': 2,
#     'a': 1,
#     'm': 2,
#     'i': 1,
#     'n': 1
# }
# ⚠️ Conditions:
# ❌ Do not use count()
# ✅ Use loops and dictionary only

user = input("Enter the word: ")
freq = {}
for i in user:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)


# 🔹 Question 2 – Number Pattern Analyzer
# Write a Python program to:
# 👉 Take numbers from user separated by space
# Example:
# 10 15 20 33 40 55
# 👉 Store numbers in list
# 👉 Print:
# All even numbers
# All odd numbers
# Sum of even numbers
# Sum of odd numbers
# Example Output:
# Even Numbers: [10, 20, 40]
# Odd Numbers: [15, 33, 55]
# Even Sum: 70
# Odd Sum: 103
# ⚠️ Conditions:
# ✅ Use loops
# ❌ Do not use sum()
# ❌ Do not use list comprehension

numbers = list(map(int,input("Enter the numbers separated by space: ").split()))
even_numbers = []
odd_numbers = []
for i in numbers:
    if i % 2 == 0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)
even_sum = 0
odd_sum = 0
for i in even_numbers:
    even_sum += i
for i in odd_numbers:
    odd_sum += i
print(f"Even Numbers: {even_numbers}")
print(f"Odd Numbers: {odd_numbers}")
print(f"Even Sum: {even_sum}")
print(f"Odd Sum: {odd_sum}")