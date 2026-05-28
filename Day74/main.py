# 🔹 Question 1 – File Compare System
# Write a Python program to:
# 👉 Create 2 text files:
# file1.txt
# file2.txt
# 👉 Write some content inside both files manually
# 👉 Read both files
# 👉 Compare contents line by line
# 👉 Print:
# If lines are same:
# Line 1: Same ✅
# If lines are different:
# Line 2: Different ❌
# Example Output:
# Line 1: Same ✅
# Line 2: Different ❌
# Line 3: Same ✅
# ⚠️ Conditions:
# ✅ Use file handling
# ✅ Use loops
# ❌ Do not use external libraries

with open("D:/Python/Own try/practice/Day74/file1.txt")as file:
    file1 = file.readlines()
with open("D:/Python/Own try/practice/Day74/file2.txt")as file:
    file2 = file.readlines()
for i in range(len(file1)):
    if file1[i].strip() == file2[i].strip():
        print(f"Line {i+1}: Same ✅")
    else:
        print(f"Line {i+1}: Different ❌")


