# Create a class pets from a class animals and further create class Dog from pets. Add a method to class Dog.

class animals:
    pass

class pets(animals):
    pass

class dog(pets):
    def bark(self):
        print("Bow Bow")

d = dog()
d.bark()