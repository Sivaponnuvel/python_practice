# 🔥 Question 1
# Write a Python program to:
# 👉 Open a file sample.txt
# 👉 Read and print content
# 👉 Handle file not found error
# 👉 Use finally to print:
# "File operation completed"
# 🧠 Example Output
# Hello world
# File operation completed
# OR
# Error: file not found
# File operation completed

try:
    user = input("Enter the file name : ")
    with open(user) as file:
        read = file.read()
except FileNotFoundError:
    print("Error: file not found")
else:
    print(read)
finally:
    print("File operation completed")


# 🔥 Question 2
# Write a Python program to:
# 👉 Take a number from user
# 👉 Divide 100 by that number
# 👉 Handle:
# invalid input
# division by zero
# 👉 Use finally to print:
# "Execution completed"
# 🧠 Example Output
# Result: 20
# Execution completed
# OR
# Error: division by zero
# Execution completed

try:
    number = int(input("Enter the number : "))
    division =  100/number
except ValueError:
    print("Error: invalid input")
except ZeroDivisionError:
    print("Error: division by zero")
else:
    print(f"Result: {division}")
finally:
    print("Execution completed")