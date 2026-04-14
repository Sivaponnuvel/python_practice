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


# 🔥 Question 2
# Write a Python program to:
# 👉 Take a sentence from user
# 👉 Write it into a file sentence.txt
# 👉 Read the file and count number of words
# 👉 Print total word count
# 🧠 Example Output
# Total words: 5

file1 = open("D:/Python/Own try/practice/Day31/sentence.txt","w")
sentence = input("Enter the sentence : ")
file1.write(sentence)
file1.close()

file1 = open("D:/Python/Own try/practice/Day31/sentence.txt")
read = file1.read()
count = 0
words = False
for i in read:
    if i != " " and words == False:
        count += 1
        words = True
    elif i == " ":
        words = False
print(f"Total words: {count}")
file1.close()