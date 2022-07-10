""" 
Two types of inheritance:
1. Single Inheritance
2. Multiple Inheritance
"""
# Single Inheritance is something which we have seen in previous examples, that is a Child Class derives its properties from only a single Parent Class, but when the Child Class is made to derive properties from more than 1 Parant Classes it is known as Multiple Inheritance
# Example Code:-


class Base1(object):
    def __init__(self):
        self.name1 = "GeeksforGeeks"
        print("Base 1")


class Base2(object):
    def __init__(self):
        self.name2 = "Hello, World"
        print("Base 2")


class Derived(Base1, Base2):
    def __init__(self):

        # calling constructors of Base1 and Base2 Classes
        Base1.__init__(self)
        Base2.__init__(self)

    def PrintSTR(self):
        print(self.name1, self.name2)


ob = Derived()
ob.PrintSTR()
