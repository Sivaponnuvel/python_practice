# Question 1
# Write a Python program to:
# 👉 Take a list of numbers from the user
# 👉 Print all prime numbers in the list

def prime_number(a):
    prime_numbers = []
    for i in a:
        if i > 1:
            is_prime  = True
            for j in range(2,i):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_numbers.append(i)
    print(prime_numbers)
s = input("enter the numbers : ").split()
s = list(map(int,s))
prime_number(s)


# Question 2
# Write a Python program to:
# 👉 Take a string from the user
# 👉 Find the most frequent character in the string
# Example:
# Input: aabbccc
# Output: c

def char(a):
    freq = {}
    for i in a:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    max_char = ''
    max_count = 0
    for i in freq:
        if freq[i] > max_count:
            max_count = freq[i]
            max_char = i
    print(max_char)
string = input("enter the string : ")
char(string)