# Question 1: Check Whether a Number Is an Armstrong Number
# Interview Topics: While Loop, Arithmetic Operators, Conditional Statements
# Write a Python function named is_armstrong(n) to check whether a given number is an Armstrong number.
# Requirements:
# 1. Create a function named is_armstrong(n).
# 2. Check whether the given number is an Armstrong number using a loop.
# 3. Do not convert the number into a string.
# 4. Return True if it is an Armstrong number; otherwise, return False.
# 5. Handle zero correctly.
# Examples:
# Input: 153Output: True
# Explanation: \(1^3 + 5^3 + 3^3 = 153\)
# Input: 123Output: FalseInput: 9474Output: TrueInput: 0Output: True

def is_armstrong(n):
    if n < 0:
        return False
    if n == 0:
        return True

    temp = n
    k = 0
    while temp > 0:
        k += 1
        temp //= 10

    temp = n
    total_sum = 0
    while temp > 0:
        digit = temp % 10
        total_sum += digit ** k
        temp //= 10

    return total_sum == n

n = int(input("Enter number: "))
print(is_armstrong(n))


# Question 2: Count the Frequency of Each Element in a List
# Interview Topics: Lists, Dictionaries, Loops, Conditional Statements
# Write a Python function named count_frequency(numbers) to count how many times each element appears in a list.
# Requirements:
# 1. Create a function named count_frequency(numbers).
# 2. Use a loop to count the frequency of each element.
# 3. Store the result in a dictionary.
# 4. Do not use the count() method.
# 5. Return the frequency dictionary.
# 6. If the list is empty, return an empty dictionary {}.
# Examples:
# Input:numbers = [1, 2, 2, 3, 1, 4, 2]Output:{    1: 2,    2: 3,    3: 1,    4: 1}
# Input:numbers = [5, 5, 5]Output:{5: 3}
# Input:numbers = []Output:{}

def count_frequency(numbers):
    freq = {}

    for i in numbers:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1

    return freq

numbers = list(map(int, input("Enter numbers: ").split()))
print(count_frequency(numbers))