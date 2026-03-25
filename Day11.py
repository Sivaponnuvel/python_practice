# Question 1
# Write a Python program to take a list of numbers from the user and print only the even numbers from the list.

def even(a):
    even_num = []
    for i in a:
        if i % 2 == 0:
            even_num.append(i)
    print(f"Even numbers : {even_num}")
x = input("Enter the numbers : ").split()
x = list(map(int,x))
even(x)


# Question 2
# Write a Python program to take a list of numbers from the user and count how many numbers are greater than 10.

def count_greater(s):
    num = 0
    for i in s:
        if i > 10:
           num += 1
    print(f"Count of numbers greater than 10: {num}") 
a = input("Enter the numbers : ").split()
a = list(map(int,a))
count_greater(a)