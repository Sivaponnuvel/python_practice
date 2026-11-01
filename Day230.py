# 🔹 Question 1 – Custom Iterator Coding Problem
# Topic: Classes, Iterators, __iter__() and __next__()
# Write a Python program to create a custom iterator that generates numbers divisible by 3 from 1 to a given number n.
# Example 1
# Input:
# n = 15
# Expected output:
# Numbers Divisible by 3: 3 6 9 12 15
# Example 2
# Input:
# n = 10
# Expected output:
# Numbers Divisible by 3: 3 6 9
# Example 3
# Input:
# n = 2
# Expected output:
# Numbers Divisible by 3:
# Requirements
# 1. Get an integer n from the user.
# 2. Create a class named DivisibleByThree.
# 3. Implement the __init__(self, n) method.
# 4. Implement the __iter__(self) method.
# 5. Implement the __next__(self) method.
# 6. Generate numbers divisible by 3 between 1 and n, inclusive.
# 7. Raise StopIteration when no more numbers are available.
# 8. Use a for loop to iterate over the custom iterator.
# 9. Display the numbers in increasing order.
# 10. If n < 3, display only Numbers Divisible by 3:.
# Conditions
# - Must use a class-based custom iterator.
# - Must implement both __iter__() and __next__().
# - Must raise StopIteration appropriately.
# - Do not use yield.
# - Do not create a list to store the generated numbers.
# - Do not import libraries.
# - Do not hardcode the output.

class DivisibleByThree:
    def __init__(self, n):
        self.n = n
        self.current  = 3

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            num = self.current
            self.current += 3
            return num
        else:
            raise StopIteration

n = int(input("Enter n: "))

print("Numbers Divisible by 3:", end=" ")
for num in DivisibleByThree(n):
    print(num, end=" ")


