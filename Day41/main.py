# 🔹 Question 1
# Write a Python program to:
# 👉 Create a module named mymath.py
# 👉 Inside the module, create functions:
# add(a, b)
# subtract(a, b)
# multiply(a, b)
# 👉 In another file (main.py):
# Import the module
# Take two numbers from user
# Call all functions
# Print results
# 🧠 Example Output:
# Addition: 10
# Subtraction: 2
# Multiplication: 24

import mymath as m
try:
    number1 = int(input("Enter the 1st number: "))
    number2 = int(input("Enter the 2nd number: "))
except ValueError:
    print("Invalid input ❌")
else:
    print(f"Addition: {m.add(number1,number2)}")
    print(f"Subtraction: {m.subtract(number1,number2)}")
    print(f"Multiplication: {m.multiply(number1,number2)}")
    print(f"Division: {m.divide(number1,number2)}")


# 🔹 Question 2
# Write a Python program to:
# 👉 Use built-in module random
# 👉 Generate a random number between 1 to 10
# 👉 Ask user to guess the number
# 👉 If correct → print "Correct guess"
# 👉 If wrong → print "Wrong guess" + show correct number
# 🧠 Example Output:
# Enter your guess: 5
# Wrong guess ❌
# Correct number was: 7

import random
attempts = 5
correct_number = random.randint(1,10)
while attempts > 0:
    try:
        user = int(input("Enter your guess number (1-10): "))
        if user == correct_number:
            print("Correct guess ✅")
            break
        else:
            attempts -= 1
            print(f"Wrong Guess❌\nAttempts left: {attempts}")
    except ValueError:
        print("Invalid input ❌")
if attempts == 0:
    print(f"Game over ❌ Correct number was: {correct_number}")