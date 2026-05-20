# 🔹 Question 1 – Word Reverse Without Using Reverse Functions
# Write a Python program to:
# 👉 Take a sentence from user
# Example:
# Python is easy
# 👉 Reverse each word separately
# Example Output:
# nohtyP si ysae
# ⚠️ Conditions:
# ❌ Do not use slicing [::-1]
# ❌ Do not use reversed()
# ✅ Use loops only

user = input("Enter the sentence: ").split()
reverse_word = ""
for i in user:
    a = ""
    for j in range(len(i)-1,-1,-1):
        a += i[j]
    reverse_word += a + " "
print(reverse_word)



# 🔹 Question 2 – Longest Word Finder
# Write a Python program to:
# 👉 Take a sentence from user
# Example:
# I am learning FastAPI backend
# 👉 Find the longest word manually
# 👉 Print:
# Longest word
# Length of longest word
# Example Output:
# Longest Word: learning
# Length: 8
# ⚠️ Conditions:
# ❌ Do not use max()
# ✅ Use loops and conditions only

sentence = input("Enter the sentence: ").split()
longest_word = ""
longest_length = 0
for i in sentence:
    word_length = 0
    for j in i:
        word_length += 1
    if word_length > longest_length:
        longest_length = word_length
        longest_word = i
print(f"Longest Word: {longest_word}")
print(f"Length: {longest_length}")