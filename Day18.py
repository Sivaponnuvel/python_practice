# Question 1
# Write a Python program to:
# 👉 Take a list of numbers from the user
# 👉 Find all pairs of numbers whose sum is equal to a given target
# 👉 Example:
# Input list: 1 2 3 4 5
# Target: 6
# Output:
# (1,5)
# (2,4)

def equal(a,b):
    s = []
    for i in a:
        diff = b-i
        if diff in s:
            return diff , i
        s.append(i)
user = input("enter the numbers : ").split()
user = list(map(int,user))
target = int(input("enter the target number : "))
print(equal(user,target)) 


# Question 2
# Write a Python program to print this pattern:
# 1
# 22
# 333
# 4444
# 55555

def pattern(a):
    for i in range(1,a+1):
        for j in range(1,i+1):
            print(i, end="")
        print()
s = int(input("enter the number : "))
pattern(s)