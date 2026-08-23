# 🔹 Question 1 – Functions: Check Palindrome Number
# Write a Python program to check whether a number is a palindrome using a function.
# Program Flow
# Create a function named is_palindrome(number).
# Take an integer from the user.
# Reverse the number using a loop.
# Return True if the number and reversed number are the same.
# Otherwise return False.
# Display the appropriate result.
# Example 1
# Input:
# Enter Number: 121
# Output:
# Palindrome Number ✅
# Example 2
# Input:
# Enter Number: 123
# Output:
# Not a Palindrome Number ❌
# ⚠️ Conditions
# ✅ Use a function
# ✅ Function must return True or False
# ✅ Use a loop to reverse the number
# ✅ Use % and //
# ❌ Don't convert the number to a string
# ❌ Don't use slicing
# ❌ Don't import any libraries
# 💡 Hint:
# original = number
# reversed_number = 0


def is_palindrome(number):
    original = number
    reversed_number = 0
    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10
    return original == reversed_number

try:
    number = int(input("Enter Number: "))
    if is_palindrome(number):
        print("Palindrome Number ✅")
    else:
        print("Not a Palindrome Number ❌")

except ValueError:
    print("Error: Invalid input ❌")


# 🔹 Question 2 – Dictionary Interview: Find Duplicate Elements and Their Count
# Write a Python program to find all duplicate numbers in a list and display their frequency.
# Program Flow
# Take space-separated integers from the user.
# Store them in a list.
# Use a dictionary to count the frequency of each number.
# Display only the numbers that appear more than once.
# Preserve the order of first occurrence.
# Example 1
# Input:
# Enter Numbers: 10 20 30 10 40 20 10
# Output:
# Duplicate Elements:
# 10 : 3
# 20 : 2
# Example 2
# Input:
# Enter Numbers: 1 2 3 4 5
# Output:
# No Duplicate Elements ❌
# ⚠️ Conditions
# ✅ Take input from the user
# ✅ Use a list
# ✅ Use a dictionary
# ✅ Use loops
# ✅ Preserve first occurrence order
# ❌ Don't use set()
# ❌ Don't use collections.Counter
# ❌ Don't sort the list
# ❌ Don't import any libraries
# 💡 Hint:
# freq = {}
# First count all elements, then loop through the dictionary and display values where:
# count > 1

numbers = list(map(int, input("Enter Numbers: ").split()))
freq = {}
for i in numbers:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

found = False

for number, count in freq.items():
    if count > 1 :
        if not found:
            print("Duplicate Elements:")
        print(f"{number} : {count}")
        found = True

if not found:
    print("No Duplicate Elements ❌")