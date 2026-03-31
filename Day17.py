# Question 1
# Write a Python program to:
# 👉 Take two lists of numbers from the user
# 👉 Print the common elements between the two lists

def common(x,y):
    common_element = []
    for i in x:
        for j in y:
            if i == j and i not in common_element:
                common_element.append(i)
    print(common_element)
a = input("enter the numbers : ").split()
a = list(map(int,a))
b = input("enter the numbers : ").split()
b = list(map(int,b))
common(a,b)


