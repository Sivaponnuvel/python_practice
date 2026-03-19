# Question 1
# Write a Python program to take three numbers from the user and print the largest number.

user1 = int(input("enter the first number : "))
user2 = int(input("enter the second number : "))
user3 = int(input("enter the third number : "))
if user1 > user2 and user1 > user3:
    print(f"{user1} is the largest number")
elif user2 > user1  and user2 > user3:
    print(f"{user2} is the largest number")
elif user3 > user1 and user3 > user2:
    print(f"{user3} is the largest number")
elif user1 == user2 == user3:
    print("all are equal")
elif user1 == user2:
    print(f"{user1} is the largest number")
elif user2 == user3:
    print(f"{user2} is the largest number")
elif user1 == user3:
    print(f"{user1} is the largest number")

    