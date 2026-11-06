# Question 1: Check Whether a String Is a Palindrome 
# Interview Topic: Strings, Loops, Conditional Statements
# Write a Python function named is_palindrome(text) to check whether a given string is a palindrome.
# A palindrome reads the same forward and backward.
# Requirements:
# 1. Create a function named is_palindrome(text).
# 2. Ignore uppercase and lowercase differences.
# 3. Ignore spaces.
# 4. Return True if the string is a palindrome.
# 5. Otherwise, return False.
# Example 1:
# Input:
# text = "Madam"
# Expected Output:
# True
# Example 2:
# Input:
# text = "Python"
# Expected Output:
# False
# Example 3:
# Input:
# text = "nurses run"
# Expected Output:
# True

def is_palindrome(text):
    text = text.lower()
    text = text.replace(" ", "")

    rev = ""
    for i in text:
        rev = i + rev

    if rev == text:
        return True
    else:
        return False


text = input("Enter a text: ")
print(is_palindrome(text))


# Question 2: Find the Second Largest Number in a List 
# Interview Topic: Lists, Loops, Conditional Statements
# Write a Python function named second_largest(numbers) to find the second-largest distinct number in a list.
# Requirements:
# 1. Create a function named second_largest(numbers).
# 2. Find the second-largest distinct number.
# 3. Do not use sort(), sorted(), or max().
# 4. If the list contains fewer than two distinct numbers, return None.
# 5. Do not modify the original list.
# Example 1:
# Input:
# numbers = [10, 20, 5, 8, 30]
# Expected Output:
# 20
# Example 2:
# Input:
# numbers = [10, 10, 20, 20, 30]
# Expected Output:
# 20
# Example 3:
# Input:
# numbers = [5, 5, 5]
# Expected Output:
# None

def second_largest(numbers):
    largest = None
    second = None

    for i in numbers:
        if largest is None or i > largest:
            if i != largest:
                second = largest
                largest = i

        elif (second is None or i > second )and i != largest:
            second = i

    return second

numbers = list(map(int, input("Enter numbers: ").split()))
print(second_largest(numbers))