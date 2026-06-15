# Question 1 – Interview Style (Strings + Dictionary)
# Write a Python program to:
# 👉 Take a sentence from user
# Example:
# python is easy and python is powerful
# 👉 Create a dictionary where:
# Key = word
# Value = position(s) where the word appears
# Example Output:
# {
#     "python": [1, 5],
#     "is": [2, 6],
#     "easy": [3],
#     "and": [4],
#     "powerful": [7]
# }
# Conditions
# ❌ Don't use collections module
# ✅ Use dictionary
# ✅ Use loops

user = input("Enter Sentence: ").split()
dictionary = {}
position = 1
for i in user:
    if i not in dictionary:
        dictionary[i] = [position]
    else:
        dictionary[i].append(position)
    position += 1
print(dictionary)


