# 🔹 Question 1 – Recursion: Find Sum of Digits
# Write a Python program to find the sum of digits of a number using recursion.
# Program Flow
# Create a function named sum_of_digits(number).
# Take an integer from the user.
# Use recursion to calculate the sum of all digits.
# Return the final sum.
# Example 1
# Input:
# Enter Number: 12345
# Output:
# Sum of Digits: 15
# Example 2
# Input:
# Enter Number: 987
# Output:
# Sum of Digits: 24
# ⚠️ Conditions
# ✅ Use a recursive function
# ✅ Use % and //
# ✅ Take input from the user
# ✅ Return the result
# ❌ Don't use loops
# ❌ Don't convert the number to a string
# ❌ Don't use sum()
# ❌ Don't import any libraries
# 💡 Hint:
# if number == 0:
#     return 0
# Then think about:
# number % 10
# number // 10

def sum_of_digits(number):
    if number == 0:
        return 0
    else:
        return (number % 10) + sum_of_digits(number // 10)

number = int(input("Enter Number: "))
print(f"Sum of Digits: {sum_of_digits(number)}")


# 🔹 Question 2 – Dictionary Interview: Merge Two Dictionaries and Add Common Values
# Write a Python program to merge two dictionaries.
# If the same key exists in both dictionaries, add their values.
# Example
# dict1 = {
#     "apple": 10,
#     "banana": 20,
#     "orange": 15
# }
# dict2 = {
#     "banana": 5,
#     "orange": 10,
#     "grapes": 25
# }
# Expected Output
# apple : 10
# banana : 25
# orange : 25
# grapes : 25
# Program Flow
# Take the number of items for the first dictionary from the user.
# Take each key and value from the user.
# Create the first dictionary.
# Do the same for the second dictionary.
# Merge both dictionaries.
# If a key already exists, add the values.
# Preserve the order of first occurrence.
# Display the final merged dictionary.
# Example Input
# How Many Items in Dictionary 1: 2
# Enter Key: apple
# Enter Value: 10
# Enter Key: banana
# Enter Value: 20
# How Many Items in Dictionary 2: 2
# Enter Key: banana
# Enter Value: 5
# Enter Key: grapes
# Enter Value: 25
# Output
# apple : 10
# banana : 25
# grapes : 25
# ⚠️ Conditions
# ✅ Take input from the user
# ✅ Use two dictionaries
# ✅ Use loops
# ✅ Merge manually
# ✅ Add values for common keys
# ✅ Preserve first occurrence order
# ❌ Don't use dictionary unpacking ({**dict1, **dict2})
# ❌ Don't use update()
# ❌ Don't use Counter
# ❌ Don't import any libraries
# 💡 Hint: Create an empty dictionary:
# merged = {}
# First add dict1, then loop through dict2 and check whether the key already exists.

dict1={}
dict2={}

items1 = int(input("How Many Items in Dictionary 1: "))
for i in range(items1):
    key = input("Enter Key: ")
    value = int(input("Enter Value: "))
    dict1[key] = value

items2 = int(input("How Many Items in Dictionary 2: "))
for i in range(items2):
    key = input("Enter Key: ")
    value = int(input("Enter Value: "))
    dict2[key] = value

merged = {}

for key, value in dict1.items():
    merged[key] = value

for key, value in dict2.items():
    if key in merged:
        merged[key] += value
    else:
        merged[key] = value

for key, value in merged.items():
    print(f"{key} : {value}")