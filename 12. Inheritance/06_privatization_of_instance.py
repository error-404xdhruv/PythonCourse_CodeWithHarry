# We dont always want the instance variables of the parent class to be inherited by the child class i.e., we can make some of the instance variables of the parent class private, which wont be available to the child class. We can do so by adding double underscores before its name.

class Parent:
    def __init__ (self):
        self.name = "DHRUV"

        # lets make the instance nickName Private
        self.__nickName = "DK"

class Child(Parent):
    def __init__(self):
        self.myName = "Blah Blah"
        Parent.__init__(self)

object1 = Child()
print(object1.nickName)

# this would produce error as nickName instance is private to Parent Class only.