""" 
Question:
Create a Class 2-D vector and use it to create another class representing a 3-D vector
"""
from cgi import print_form


class C2DVector:
    def __init__(self, i, j):
        self.icap = i
        self.jcap = j

    def __str__(self):
        return (f"{self.icap}i + {self.jcap}j")


""" __str__ is used to set what would show upon calling str(obj) """

""" The super() function is used to give access to methods and properties of a parent or sibling class.

The super() function returns an object that represents the parent class. """


class C3DVector (C2DVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kcap = k

    def __str__(self):
        return (f"{self.icap}i + {self.jcap}j + {self.kcap}k")


my2DVector = C2DVector(2, 3)
my3DVector = C3DVector(2, 4, 5)
print(my2DVector)
print(my3DVector)
