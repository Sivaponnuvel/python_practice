# 🟢 Question 1 – Recursion
# Topic: Recursive functions
# Create a recursive function called factorial(n) that calculates the factorial of a positive integer.
# The factorial is calculated as:
# \[
# n! = n \times (n-1) \times \cdots \times 1
# \]
# For example, \(5! = 5 \times 4 \times 3 \times 2 \times 1 = 120\).
# Requirements:
# 1. Define a function named factorial(n).
# 2. Use recursion to calculate the factorial.
# 3. Include a base case to stop the recursion.
# 4. Get an integer from the user.
# 5. Print the factorial result.
# 6. Handle negative input by printing Factorial is not defined for negative numbers.
# Example input:
# Enter a number: 5
# Expected output:
# Factorial of 5: 120
# For negative input:
# Enter a number: -3
# Factorial is not defined for negative numbers.
# Rules:
# - Use recursion; do not use loops to calculate the factorial.
# - Do not use external libraries.
# - Remember that 0! = 1.

def factorial(n):
    if n == 0  or n == 1:
        return 1

    return n * factorial(n - 1)

num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"Factorial of {num}: {factorial(num)}")


# 🟢 Question 2 – Class Methods and Class Variables
# Topic: OOP — @classmethod and shared class data
# Imagine you're developing a user management system. Create a class named User that tracks how many user objects have been created.
# Requirements:
# 1. Create a class variable user_count = 0.
# 2. In __init__(), store each user's name and email.
# 3. Increment user_count whenever a new user object is created.
# 4. Create a class method named get_user_count() using @classmethod.
# 5. Create three user objects using input.
# 6. Print each user's name and email.
# 7. Display the total number of users created using get_user_count().
# Expected output (example inputs):
# Enter name: Arun
# Enter email: arun@example.com
# Enter name: Siva
# Enter email: siva@example.com
# Enter name: Priya
# Enter email: priya@example.com
# User Details:
# Arun - arun@example.com
# Siva - siva@example.com
# Priya - priya@example.com
# Total Users: 3
# Rules:
# - Use a class variable to track the count.
# - Use @classmethod for get_user_count().
# - Do not calculate the count manually using len() on a list.
# - Do not use external libraries.

class User:
    user_count = 0
    def __init__(self, name, email):
        self.name = name
        self.email = email

        User.user_count += 1

    @classmethod
    def get_user_count(cls):
        return cls.user_count

users = []

for i in range(3):
    name  = input("Enter name: ")
    email = input("Enter email: ")

    user = User(name, email)
    users.append(user)

print("User Details:")
for i in users:
    print(f"{i.name} - {i.email}")

print(f"Total Users: {User.get_user_count()}")