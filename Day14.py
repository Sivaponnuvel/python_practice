# Question 1
# Write a Python program to take a list of numbers from the user and print the smallest number in the list (without using min()).

def small(a):
    smallest  = a[0]
    for i in a:
        if i < smallest  :
            smallest  = i
    print(f"smallest number is {smallest}")
m = input("enter the numbers : ").split()
m = list(map(int,m))
small(m)


