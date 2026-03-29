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


