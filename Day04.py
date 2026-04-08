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


# Question 2
# Write a Python program to take a number from the user and check whether it is divisible by 5 or not.

user = int(input("enter the number : "))
if user % 5 == 0:
    print(f"{user} is a divisible by 5")
else:
    print(f"{user} is a not divisible by 5")