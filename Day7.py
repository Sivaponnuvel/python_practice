# Question 1
# Write a Python program to take a number from the user and find the sum of numbers from 1 to that number.

def num(n):
    s = 0
    for i in range(1,n+1):
        s += i
    print(f"sum of {n} is {s}")
user = int(input("enter the number : "))
num(user)

