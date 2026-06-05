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


# 🔹 Question 2 – Functions: Number Statistics System
# Write a Python program to:
# 👉 Create a function:
# analyze_numbers(numbers)
# 👉 Function should calculate:
# Total Sum
# Average
# Largest Number
# Smallest Number
# 👉 Return result as dictionary
# Example:
# {
#     "sum": 150,
#     "average": 30.0,
#     "largest": 50,
#     "smallest": 10
# }
# 👉 Take 5 numbers from user
# 👉 Store inside a list
# 👉 Call function
# 👉 Print all returned values
# Example Output:
# Enter Number: 10
# Enter Number: 20
# Enter Number: 30
# Enter Number: 40
# Enter Number: 50
# Sum: 150
# Average: 30.0
# Largest: 50
# Smallest: 10
# ⚠️ Conditions:
# ✅ Use functions
# ✅ Return dictionary
# ✅ Use loops
# ❌ Do not use sum()
# ❌ Do not use max()
# ❌ Do not use min()

def analyze_numbers(numbers):
    # Total sum
    sum_num = 0
    for i in numbers:
        sum_num += i
    # Average
    avg = sum_num / len(numbers)
    # Largest
    largest_num = numbers[0]
    for i in numbers:
        if i > largest_num:
            largest_num = i
    # Smallest
    smallest_num = numbers[0]
    for i in numbers:
        if i < smallest_num:
            smallest_num = i
    return {"sum": sum_num, "average": avg, "largest": largest_num, "smallest": smallest_num}

numbers = []
for i in range(5):
    number = int(input("Enter Number: "))
    numbers.append(number)

result = analyze_numbers(numbers)

for key, value in result.items():
    print(f"{key.capitalize()}: {value}")