# 🔹 Question 1 – reduce(): Find the Product of All Numbers
# Write a Python program to find the product of all numbers in a list using reduce().
# Program Flow
# Take space-separated integers from the user.
# Convert them into a list.
# Use reduce() to multiply all the numbers.
# Display the final product.
# Example
# Input
# Enter Numbers: 2 3 4 5
# Output
# Product: 120
# ⚠️ Conditions
# ✅ Take input from the user
# ✅ Import reduce from functools
# ✅ Use reduce()
# ✅ Use a lambda function
# ❌ Don't use a loop to calculate the product
# ❌ Don't create a separate function using def

from functools import reduce

numbers = list(map(int,input("Enter Numbers: ").split()))
res = reduce(lambda x, y: x * y, numbers)
print(f"Product: {res}")


# 🔹 Question 2 – enumerate(): Display Index and Name
# Write a Python program to display the index and student name using enumerate().
# Program Flow
# Take student names as space-separated input.
# Use enumerate() to display the index and name.
# Example
# Input
# Enter Student Names: Siva Rahul Priya
# Output
# 0 : Siva
# 1 : Rahul
# 2 : Priya
# ⚠️ Conditions
# ✅ Take input from the user
# ✅ Use enumerate()
# ✅ Use a loop
# ❌ Don't use range(len(...))
# ❌ Don't manually maintain an index variable

names = input("Enter Student Names: ").split()

for index, name in enumerate(names):
    print(f"{index} : {name}")