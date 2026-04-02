# Question 1
# Write a Python program to:
# 👉 Create a class Person
# 👉 Take name and age from user
# 👉 Store using constructor
# 👉 Create object
# 👉 Print details
# Example Output:
# Name: Siva
# Age: 21

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
a = input("Enter your Name : ")
b = int(input("Enter your Age : "))
s1 = Person(a,b)
print(f"Name : {s1.name}")
print(f"Age : {s1.age}")


