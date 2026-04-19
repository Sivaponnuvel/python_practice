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


