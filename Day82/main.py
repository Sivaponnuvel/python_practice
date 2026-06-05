# 🔹 Question 1 – File Handling: Word Frequency Logger
# Write a Python program to:
# 👉 Create a text file:
# notes.txt
# 👉 Take a sentence from user
# Example:
# python fastapi python backend
# 👉 Save the sentence into:
# notes.txt
# 👉 Read the file content
# 👉 Count how many times each word appears
# 👉 Store result in a dictionary
# Example Output:
# {
#     "python": 2,
#     "fastapi": 1,
#     "backend": 1
# }
# 👉 Write the frequency result into another file:
# report.txt
# Example content of report.txt:
# python : 2
# fastapi : 1
# backend : 1
# ⚠️ Conditions:
# ✅ Use file handling
# ✅ Use loops
# ❌ Do not use count()
# ❌ Do not use collections.Counter

user = input("Enter Sentence: ")
with open("D:/Backend/Python/Own try/practice/Day82/notes.txt","w")as file:
    file.write(user)
with open("D:/Backend/Python/Own try/practice/Day82/notes.txt","r")as file:
    read = file.read()
words = read.lower().split()
freq = {}
for i in words:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)
with open("D:/Backend/Python/Own try/practice/Day82/report.txt", "w")as file:
    for key,value in freq.items():
        file.write(f"{key} : {value}\n")
print("Report saved to report.txt")


