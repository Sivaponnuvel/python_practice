# Question 1
# Write a Python program to take a string from the user and count how many times each character appears in the string.
# 👉 Example:
# Input: hello
# Output:
# h → 1
# e → 1
# l → 2
# o → 1

def char(a):
    s = {}
    for i in a:
        if i in s:
            s[i] += 1
        else:
            s[i] = 1
    print(s)
x = input("Enter the word : ")
char(x)


