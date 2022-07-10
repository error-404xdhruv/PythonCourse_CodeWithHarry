
# a python program to demonstrate Inheritance
# Base or Super or Parent Class. Note objec in brackets
# Generally, object is made ancestor of all Classes
# In Python, "class Person" is equivalent to "class Person(object)"
class Person (object):
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def isEmployee(self):
        return False

# creating SubClass
class ChildSubClass (Person):
    def isEmployee(self):
        return True


emp = Person("Person 1")
print(emp.getName(), emp.isEmployee())

emp = ChildSubClass("Person 2")
print(emp.getName(), emp.isEmployee())
