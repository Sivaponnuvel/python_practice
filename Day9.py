# Question 1
# Write a Python program to take a string from the user and count the number of vowels in it.
def vow(a):
    s = 0
    for i in a:
        if i in "aeiouAEIOU":
            s += 1
    print(f"Number of vowels : {s}")
n = input("Enter the name : ")
vow(n)


