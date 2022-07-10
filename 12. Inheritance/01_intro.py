
""" Inheritance is the capability of one class to derive or inherit the properties from another class.  """
""" Benefits of Inheritance :-
It provides the reusability of a code. We don’t have to write the same code again and again. Also, it allows us to add more features to a class without modifying it. """

# base class / parent class
class Employee:
    company = "Google"
    def GetDetails (self):
        print("This is an employee.")

# derived class / child class
class Programmer(Employee):
    def anotherGet (self):
        print("hello World")

temp1 = Employee()
print(temp1.company)
temp1.GetDetails()

temp2 = Programmer()
print(temp2.company)
temp2.anotherGet()
temp2.GetDetails()