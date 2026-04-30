# 🔹 Question 1
# Write a Python program to:
# 👉 Create a dictionary:
# course
# duration
# 👉 Store it in a file data.json using JSON
# 👉 Read the file
# 👉 Print the data
# 🧠 Example Output:
# {'course': 'Python', 'duration': '3 months'}

import json
a = {'course': 'Python', 'duration': '3 months'}
with open("D:/Python/Own try/practice/Day46/data.json","w") as file:
    json.dump(a, file)
with open("D:/Python/Own try/practice/Day46/data.json", "r") as file:
    read = json.load(file)
print(read)


