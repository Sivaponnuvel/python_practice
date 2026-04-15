# 🔥 Question 1
# Write a Python program to:
# 👉 Create a file log.txt
# 👉 Take a message from user
# 👉 Append the message into the file (don’t overwrite old data)
# 👉 Read the file and print all content
# 🧠 Example Output
# Hello
# How are you
# Good morning

with open("D:/Python/Own try/practice/Day32/log.txt","a") as file:
    user = input("Enter your Message : ")
    file.write(f"{user}\n")
    file.close()

with open("D:/Python/Own try/practice/Day32/log.txt") as file:
    print(file.read())
    file.close()


