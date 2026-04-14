# 🔥 Question 1
# Write a Python program to:
# 👉 Create a file data.txt
# 👉 Write your name and city into the file
# 👉 Then read the file and print the content
# 🧠 Example Output
# Siva
# Chennai

file = open("D:/Python/Own try/practice/Day31/data.txt","w")
file.write("Siva \n")
file.write("Chennai \n")
file.close()

file = open("D:/Python/Own try/practice/Day31/data.txt")
print(file.read())
file.close()


