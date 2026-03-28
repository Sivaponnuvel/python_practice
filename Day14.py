# Question 1
# Write a Python program to take a list of numbers from the user and print the smallest number in the list (without using min()).

def small(a):
    smallest  = a[0]
    for i in a:
        if i < smallest  :
            smallest  = i
    print(f"smallest number is {smallest}")
m = input("enter the numbers : ").split()
m = list(map(int,m))
small(m)


# Question 2
# Write a Python program to take a string from the user and count how many words are present in the string.
# 👉 Example:
# Input: I love python
# Output: 3

def count(c):
    count = 0
    word = False
    for i in c:
        if i != " " and word == False:
            count += 1
            word = True
        elif i == " ":
            word = False
    print(f"Number of words: {count}")
s = input("enter the sentence : ")
count(s)