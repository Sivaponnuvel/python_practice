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



