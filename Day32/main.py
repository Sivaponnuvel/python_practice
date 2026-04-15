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


# 🔥 Question 2
# Write a Python program to:
# 👉 Create a file numbers.txt
# 👉 Take numbers from user (space separated)
# 👉 Write numbers into file
# 👉 Read the file and find:
# total numbers count
# sum of numbers
# 🧠 Example Output
# Count: 5
# Sum: 50

with open("D:/Python/Own try/practice/Day32/numbers.txt","w") as file:
    user = list(map(int,input("Enter numbers separated by space : " ).split()))
    file.write(" ".join(map(str,user)))
    file.close()

with open("D:/Python/Own try/practice/Day32/numbers.txt") as file:
    read = file.read().split()
    numbers = list(map(int,read))
    count = len(numbers)
    total = sum(numbers)
    print(f"Count: {count}")
    print(f"Sum: {total}")
    file.close()