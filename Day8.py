# Question 1
# Write a Python program to print this pattern:
# *
# **
# ***
# ****
# *****

def star(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*", end="")
        print()
a = int(input("enter the number : "))
star(a)


