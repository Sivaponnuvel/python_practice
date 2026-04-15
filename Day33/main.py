# 🔥 Question 1
# Write a Python program to:
# 👉 Create a file story.txt
# 👉 Write 3–4 lines into the file
# 👉 Read the file line by line
# 👉 Print each line
# 👉 Also print total number of lines
# 🧠 Example Output
# Hello
# How are you
# I am learning Python
# File handling is easy
# Total lines: 4

with open("D:/Python/Own try/practice/Day33/story.txt","w") as file:
    file.write("Hello\nHow are you\nI am leaning pyhon\nFile handling is easy")

with open("D:/Python/Own try/practice/Day33/story.txt") as file:
    read = file.readlines()
    for i in read:
        print(i.strip())
    print(f"Total lines: {len(read)}")


# 🔥 Question 2
# Write a Python program to:
# 👉 Create a file data.txt
# 👉 Write a paragraph (sentence) into the file
# 👉 Take a word from user
# 👉 Read the file
# 👉 Count how many times the word appears
# 👉 Print the count
# 🧠 Example Output
# Word count: 2

with open("D:/Python/Own try/practice/Day33/data.txt","w") as file:
    file.write("Python is a powerful programming language.\nPython is easy to learn.\nMany developers use Python for real-world applications.")

with open("D:/Python/Own try/practice/Day33/data.txt") as file:
    read = file.read().lower()
    word = input("Enter the word : ").lower()
    count = read.split().count(word)
    print(f"Word count : {count}")