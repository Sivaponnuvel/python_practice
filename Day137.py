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


