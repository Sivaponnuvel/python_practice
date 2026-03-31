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


# Question 2
# Write a Python program to:
# 👉 Take a string
# 👉 Find the first repeated character

def character(s):
    first_repeated_character = []
    for i in s:
        if i in first_repeated_character:
            print(f"first repeated character is : {i}")
            break
        else:
            first_repeated_character.append(i)
p = input("enter the word : ")
character(p)