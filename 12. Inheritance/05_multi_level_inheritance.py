# When we have a Child and Grand Child Relationship
# Generally, object is made ancestor of all classes
# In Python , 3.X "class Person" is equivalent to "class Person(object)"
from unicodedata import name


class Person:
    def __init__(self, name):
        self.name = name
    def getName (self):
        return self.name

# Child Class
class Child(Person):
    def __init__(self, name, age):
        Person.__init__(self, name)
        self.age = age

    def getAge (self):
        return self.age

# Grand Child Class
class GrandChild (Child):
    def __init__(self, name, age, address):
        Child.__init__(self, name, age)
        self.address = address
    def getAdd (self):
        return self.address

# Driver Code
g = GrandChild("Dhruv", 35, "Varanasi")
print(g.getName(), g.getAge(), g.getAdd())