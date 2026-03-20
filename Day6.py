# Question 1
# Write a Python program to print numbers from 1 to 10 using a loop.

def num(n):
    for i in range(n):
        print(i+1)
num(10)


# Question 2
# Write a Python program to take a number from the user and print its multiplication table (1 to 10).

def num(x):
    for i in range(1,11):
        ans = i * x
        print(f"{i} X {x} = {ans}")
a = int(input("enter the number : "))
num(a)