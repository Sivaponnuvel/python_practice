# 🔥 Question 1 – Multiple Inheritance
# Write a Python program to:
# 👉 Create class Father
# method: show_father() → print "This is father"
# 👉 Create class Mother
# method: show_mother() → print "This is mother"
# 👉 Create class Child (inherits from both Father and Mother)
# method: show_child() → print "This is child"
# 👉 Create object of Child and call all methods
# 🧠 Example Output
# This is father
# This is mother
# This is child

class Father:
    def show_father(self):
        print("This is father")
class Mother:
    def show_mother(self):
        print("This is mother")
class Child(Father , Mother):
    def show_child(self):
        print("This is child")
s = Child()
s.show_father()
s.show_mother()
s.show_child()


