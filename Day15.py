# Question 1
# Write a Python program to take a list of numbers from the user and print the sum of only even numbers in the list.
# 👉 Example:
# Input: 1 2 3 4 5 6
# Output: 12 (2 + 4 + 6)

def sum_even(a):
    even_sum = 0
    for i in a:
        if i % 2 == 0:
            even_sum += i
    print(f"sum of even numbers is {even_sum}")
numbers = input("enter the numbers : ").split()
numbers = list(map(int,numbers))
sum_even(numbers)


# Question 2
# Write a Python program to take a string from the user and find the first non-repeating character.
# 👉 Example:
# Input: aabbcde
# Output: c

def first_non_repeating(s):
    for i in s:
        count = 0
        for j in s:
            if i == j:
                count += 1
        if count == 1:
            print(f"First Non-repeating character is : {i}")
            break
word = input("enter the word :")
first_non_repeating(word)