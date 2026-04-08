# Question 1
# Write a Python program to take a number from the user and check whether it is even or odd.

a = int(input("enter the number : "))
if a % 2 == 0:
    print(f"{a} is even number")
else:
    print(f"{a} is odd number")


# Question 2
# Write a Python program to take a number from the user and check whether it is positive or negative.

user =  int(input("enter a number : "))
if user > 0 :
    print(f"{user} is a positive number")
elif user < 0 :
    print(f"{user} is a negative number")
else:
    print("zero")