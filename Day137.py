# 🔹 Question 1 – filter() + lambda: Display Even Numbers
# Write a Python program to display only the even numbers from a list using filter() and lambda.
# Program Flow
# Take space-separated integers from the user.
# Convert them into a list.
# Use filter() with a lambda function to get only the even numbers.
# Convert the result into a list.
# Display the even numbers.
# Example
# Input
# Enter Numbers: 10 15 21 28 35 40
# Output
# Even Numbers:
# 10 28 40
# ⚠️ Conditions
# ✅ Take input from the user
# ✅ Use filter()
# ✅ Use lambda
# ✅ Convert the result into a list
# ❌ Don't use a for loop to filter the numbers
# ❌ Don't create a separate function using def

numbers = list(map(int, input("Enter Numbers: ").split()))

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(*even_numbers)


# 🔹 Question 2 – zip(): Combine Student Names and Marks
# Write a Python program to combine two lists using zip().
# Program Flow
# Take student names as space-separated input.
# Take student marks as space-separated input.
# Combine both lists using zip().
# Display each student's name and mark.
# Example
# Input
# Enter Student Names: Siva Rahul Priya
# Enter Student Marks: 85 90 78
# Output
# Siva : 85
# Rahul : 90
# Priya : 78
# ⚠️ Conditions
# ✅ Take both lists from the user
# ✅ Use zip()
# ✅ Use a loop to display the output
# ❌ Don't use indexing like names[i]
# ❌ Don't use range()

names = input("Enter Students Names: ").split()
marks = list(map(int, input("Enter Students Marks: ").split()))

result = list(zip(names,marks))

for name, mark in result:
    print(f"{name} : {mark}")