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


