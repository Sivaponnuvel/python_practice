# 🔹 Question 1 – Lambda Function: Square of a Number
# Create a lambda function that takes a number and returns its square.
# Program Flow
# Input:
# Enter a number: 7
# Expected Output:
# Square of 7: 49
# ⚠️ Conditions
# ✅ Use input()
# ✅ Convert the input into an integer
# ✅ Create a lambda function
# ✅ Lambda must accept one argument
# ✅ Use the lambda function to calculate the square
# ❌ Don't use a normal def function
# ❌ Don't use libraries

result = lambda number: number ** 2

number = int(input("Enter a number: "))
print(f"Square of {number}: {result(number)}")


