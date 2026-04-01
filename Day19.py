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


