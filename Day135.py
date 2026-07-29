# 🔹 Question 1 – Lambda + map(): Square All Numbers
# Write a Python program to create a new list containing the square of every number using lambda and map().
# Program Flow
# Take space-separated integers from the user.
# Convert them into a list.
# Use map() with a lambda function to calculate the square of each number.
# Convert the result into a list.
# Display the squared numbers.
# Example
# Input
# Enter Numbers: 2 4 6 8
# Output
# Squared Numbers:
# 4 16 36 64
# ⚠️ Conditions
# ✅ Take input from the user
# ✅ Use lambda
# ✅ Use map()
# ✅ Convert the result into a list
# ❌ Don't use a for loop to calculate the squares
# ❌ Don't create a separate function using def

numbers = list(map(int, input("Enter Numbers: ").split()))

squared_numbers = list(map(lambda x: x**2, numbers))

print("Squared Numbers:")
print(*squared_numbers)


