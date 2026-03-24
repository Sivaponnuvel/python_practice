# Question 1
# Write a Python program to take 5 numbers from the user, store them in a list, and print the largest number in the list.

def lis(a):
    largest = a[0]
    for i in a:
        if i > largest:
            largest = i
    print(f"largest number is {largest}")
n = input("Enter 5 numbers separated by space:").split()
n = list(map(int,n))
lis(n)


# Question 2
# Write a Python program to take a list of numbers from the user and calculate the sum of all elements in the list.
def sum(s):
    p = 0
    for i in s:
        p += i
    print(p)
x =  input("Enter numbers separated by space : ").split()
x = list(map(int,x))
sum(x)