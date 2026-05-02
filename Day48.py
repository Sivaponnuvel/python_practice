# 🔹 Question 1 – List + Functions
# Write a Python program to:
# 👉 Create a list of numbers (take 5 numbers from user)
# 👉 Create functions:
# find_max()
# find_min()
# find_sum()
# 👉 Call all functions
# 👉 Print results
# 🧠 Example Output:
# Max: 50
# Min: 10
# Sum: 150

def find_max(a):
    max_number = a[0]
    for i in a:
        if i > max_number:
            max_number = i
    return max_number
def find_min(b):
    min_number = b[0]
    for i in b:
        if i < min_number:
            min_number = i
    return min_number
def find_sum(c):
    sum_number = 0
    for i in c:
        sum_number += i
    return sum_number
numbers =  list(map(int,input("Enter 5 numbers separated by space: ").split()))
if len(numbers) != 5:
    print("Please enter exactly 5 numbers ❌")
else:
    print(f"Max: {find_max(numbers)}")
    print(f"Min: {find_min(numbers)}")
    print(f"Sum: {find_sum(numbers)}")


# 🔹 Question 2 – String Validation (Real-world)
# Write a Python program to:
# 👉 Take a string from user
# 👉 Count:
# vowels
# consonants
# digits
# 👉 Print result
# 🧠 Example:
# Input: Siva123
# Vowels: 2
# Consonants: 2
# Digits: 3

# method-1
def vowels(a):
    count_vowels = 0
    for i in a:
        if i in "aeiouAEIOU":
            count_vowels += 1
    return count_vowels
def consonants(b):
    count_consonants = 0
    for i in b:
        if i.isalpha() and i not in "aeiouAEIOU":
            count_consonants += 1
    return count_consonants
def digits(c):
    count_digits = 0
    for i in c:
        if i.isdigit():
            count_digits += 1
    return count_digits
user = input("Enter string: ")
print(f"Vowels: {vowels(user)}")
print(f"Consonants: {consonants(user)}")
print(f"Digits: {digits(user)}")
