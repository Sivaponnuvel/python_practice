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


