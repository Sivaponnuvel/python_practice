# Question 1
# Write a Python program to take a list of numbers from the user and find the second largest number in the list.

def second_largest(a):
    largest = a[0]
    for i in a :
        if i > largest:
            largest = i
    second = None
    for i in a :
        if i != largest:
            if second is None or i > second:
                second = i
    print(f"Second largest number is {second}")    
x = input("enter the numbers : ").split()
x = list(map(int,x))
second_largest(x)


