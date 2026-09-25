# 🔹 Question 1 – Dictionary: Find the Student with Highest Marks
# Create a Python program using a dictionary to store student names and their marks.
# Use the following data:
# students = {
#     "Arun": 85,
#     "Bala": 72,
#     "Kumar": 90,
#     "Siva": 78
# }
# Find the student who has the highest marks.
# Expected Output
# Student with highest marks: Kumar
# Marks: 90
# ⚠️ Conditions
# ✅ Use a dictionary
# ✅ Use a loop
# ✅ Find the highest mark using logic
# ✅ Display the student name
# ✅ Display the highest mark
# ❌ Don't use max()
# ❌ Don't use libraries
# ❌ Don't hardcode "Kumar" or 90

students = {
    "Arun": 85,
    "Bala": 72,
    "Kumar": 90,
    "Siva": 78
}

highest_mark = students["Arun"]
highest_name = "Arun"

for key, value in students.items():
    if value > highest_mark:
        highest_mark = value
        highest_name = key

print(f"Student with highest marks: {highest_name}")
print(f"Marks: {highest_mark}")


# 🔹 Question 2 – Palindrome Number
# Write a Python program to check whether a given number is a palindrome number.
# A palindrome number remains the same when its digits are reversed.
# Examples
# 121 → Palindrome
# 1221 → Palindrome
# 123 → Not Palindrome
# Input
# Enter a number: 121
# Expected Output
# 121 is a Palindrome Number ✅
# For:
# Enter a number: 123
# Expected:
# 123 is Not a Palindrome Number ❌
# ⚠️ Conditions
# ✅ Use input()
# ✅ Convert the input to an integer
# ✅ Use a while loop
# ✅ Reverse the number using arithmetic logic
# ✅ Compare the original number with the reversed number
# ❌ Don't convert the number into a string
# ❌ Don't use slicing like [::-1]
# ❌ Don't use str()
# ❌ Don't use libraries

number = int(input("Enter a number: "))

original = number
rev = 0

while number > 0:
    digit  = number % 10
    rev = rev * 10 + digit
    number = number // 10

if original == rev:
    print(f"{original} is a Palindrome Number ✅")
else:
    print(f"{original} is Not a Palindrome Number ❌")