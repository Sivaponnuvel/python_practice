# 🔹 Question 1 – Reverse a Word
# Write a Python program to reverse a word entered by the user.
# Program Flow
# Input:
# Enter a word: Python
# Expected Output:
# Reversed word: nohtyP
# ⚠️ Conditions
# ✅ Use input()
# ✅ Store the word in a variable
# ✅ Reverse the word
# ✅ Display the reversed word
# ❌ Don't use libraries
# ❌ Don't use a predefined word
# ❌ Don't use a function such as reverse()

def rev_word(word):
    rev = ""
    for i in word:
        rev = i + rev
    return rev

word = input("Enter a word: ")
print(f"Reversed word: {rev_word(word)}")


# 🔹 Question 2 – Palindrome Number
# Write a Python program to check whether a given number is a palindrome.
# A palindrome number reads the same forward and backward.
# For example:
# 121 → Palindrome
# 123 → Not Palindrome
# Program Flow
# Input:
# Enter a number: 121
# Expected Output:
# 121 is a Palindrome Number ✅
# For a non-palindrome:
# Input:
# Enter a number: 123
# Expected Output:
# 123 is Not a Palindrome Number ❌
# ⚠️ Conditions
# ✅ Use input()
# ✅ Convert the input into an integer
# ✅ Reverse the number using logic
# ✅ Compare the original number with the reversed number
# ✅ Use a loop
# ❌ Don't convert the number into a string for checking
# ❌ Don't use libraries
# ❌ Don't use a predefined number

def is_palindrome(number):
    original = number
    rev_num = 0 
    while number > 0:
        digit = number % 10
        rev_num = rev_num * 10 + digit
        number = number // 10
    if original == rev_num:
        print(f"{original} is a Palindrome Number ✅")
    else:
        print(f"{original} is Not a Palindrome Number ❌")

number = int(input("Enter a number: "))
is_palindrome(number)