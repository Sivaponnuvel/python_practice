# Question 1
# Write a Python program to take two numbers from the user and print which number is larger.

a = input("enter the two numbers : ").split()
a = list(map(int,a))
if a[0] > a[1]:
    print(f"{a[0]} is a larger number")
elif a[0] < a[1]:
    print(f"{a[1]} is a larger number")
else:
    print("both number are equal")


