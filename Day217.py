# Question 1 – List Coding Problem
# Topic: Lists, Loops and Conditional Statements
# Write a Python program to find the common elements between two lists without duplicates.
# Example:
# list1 = [10, 20, 30, 40, 20, 50]list2 = [20, 40, 60, 20, 70]
# Expected output:
# Common Elements: [20, 40]
# Requirements:
# 1. Create the two lists shown above.
# 2. Find the elements that appear in both lists.
# 3. Include each common element only once.
# 4. Print the common elements as a list.
# Conditions:
# - Use loops and conditional statements.
# - Do not use set().
# - Do not use external libraries.
# - Your solution should work if the list values change.

list1 = [10, 20, 30, 40, 20, 50]
list2 = [20, 40, 60, 20, 70]

common = []

for i in list1:
    if i in list2:
        if i not in common:
            common.append(i)

print(f"Common Elements: {common}")


