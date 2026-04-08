# 🔥 Question 1 - Method Overriding
# 🎯 Task
# Write a Python program to:
# 👉 Create class Animal
# method: sound() → print "Animal makes sound"
# 👉 Create class Dog (inherits Animal)
# override method sound() → print "Dog barks"
# 👉 Create object of Dog and call method
# 🧠 Example Output
# Dog barks

class Animal:
    def sound(self):
        return "Animal makes sound"
class Dog(Animal):
    def sound(self):
        return "Dog barks"
obj = Dog()
print(f"{obj.sound()}")


