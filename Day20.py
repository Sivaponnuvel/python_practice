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


# Question 2
# Write a Python program to:
# 👉 Create a class Calculator
# 👉 Create methods:
# add()
# subtract()
# multiply()
# division()
# 👉 Take two numbers from user
# 👉 Perform all operations using object

class Calculator:
    def __init__(self,number1,number2):
        self.number1 = number1
        self.number2 = number2
    def add(self):
        return self.number1 + self.number2
    def subtract(self):
        return self.number1 - self.number2
    def multipy(self):
        return self.number1 * self.number2
    def division(self):
        return self.number1 / self.number2
number_1 = int(input("Enter the 1st Number : "))
number_2 = int(input("Enter the 2nd Number : "))
s3 = Calculator(number_1,number_2)
print(f"Addition: {s3.add()}")
print(f"Subtraction: {s3.subtract()}")
print(f"Multiplication: {s3.multipy()}")
print(f"Division: {s3.division()}")