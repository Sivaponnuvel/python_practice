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


# Question 2
# Write a Python program to take a string from the user and check whether it is a palindrome or not.

# use built-in function 
def palin(n):
    a = n[::-1]
    if n == a:
        print(f"{n} is palindrome")
    else:
        print(f"{n} is not a palindrome")
s =  input("Enter the name : ")
palin(s)   

