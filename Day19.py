# Question 1
# Write a Python program to:
# 👉 Take a list of numbers from the user
# 👉 Find the missing number in a sequence
# 👉 Example:
# Input: 1 2 3 5 6
# Output: 4

def find_missing(num):
    n = len(num)+1
    total_sum = n*(n+1)//2
    actul_sum = sum(num)
    return total_sum - actul_sum
nums = list(map(int,input("enter the numbers : ").split()))
print(f"Missing number : {find_missing(nums)}")

# Question 2
# Write a Python program to:
# 👉 Take a string from the user
# 👉 Check whether the string is an anagram of another string
# 👉 Example:
# Input: listen, silent
# Output: Anagram

# method-1
def anagram(a,b):
    x = sorted(a)
    y = sorted(b)
    if x == y:
        print("Anagram")
    else:
        print("Not Anagram")
word_1 = input("enter the 1st word : ")
word_2 = input("enter the 2nd word : ")
anagram(word_1,word_2)

# method-2
def Anagram(a,b):
    if len(a) != len(b):
        print("Not Anagram")
        return
    freq = {}
    for i in a:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] =1
    for i in b:
        if i in freq:
            freq[i] -= 1
        else:
            print("Not Anagram")
            return
    for i in freq:
        if freq[i] != 0:
            print("Not Anagram")
            return
    print("Anagram")
x = (input("Enter the 1st word : "))
y = (input("Enter the 2nd word : "))
Anagram(x,y)