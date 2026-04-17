# 🔥 Question 1
# Write a Python program to:
# 👉 Take two numbers from user
# 👉 Divide the numbers
# 👉 Handle error if:
# user enters non-number
# division by zero
# 👉 Print result if no error
# 🧠 Example Output
# Result: 5
# OR
# Error: division by zero
# OR
# Error: invalid input

try:
    number1 = int(input("Enter the 1st number : "))
    number2 = int(input("Enter the 2nd number : "))
    print(f"Result: {number1/number2}")
except ValueError:
    print("Error: invalid input")
except ZeroDivisionError:
    print("Error: division by zero")


# 🔥 Question 2
# Write a Python program to:
# 👉 Take a filename from user
# 👉 Try to open and read the file
# 👉 Handle error if file does not exist
# 👉 Print file content if exists
# 🧠 Example Output
# File content: Hello world
# OR
# Error: file not found

try :
    user = input("Enter the file name : ")
    with open(user)as file:
        content = file.read()
        if content:
            print(f"File content: {content}")
        else:
            print("File is empty")
except FileNotFoundError:
    print("Error: File not found")