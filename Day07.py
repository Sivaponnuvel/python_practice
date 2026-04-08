# Question 1
# Write a Python program to take a number from the user and find the sum of numbers from 1 to that number.

def num(n):
    s = 0
    for i in range(1,n+1):
        s += i
    print(f"sum of {n} is {s}")
user = int(input("enter the number : "))
num(user)


# Question 2
# Write a Python program to take a number from the user and find its factorial using a loop.

def fact(f):
    a = 1
    for i in range(1,f+1):
        a *= i
    print(f"factorial of {f} is {a}")
user1 = int(input("enter the number : "))
fact(user1)