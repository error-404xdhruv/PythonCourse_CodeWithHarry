class Person(object):

    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    
    def display (self):
        print(self.name , self.idnumber)

# creating the child class
# while writing the subclass we have to write / invoke all the instances of the Parent Class like here we have to invoke self , name and idnumber as well, if we would not do that then we would get errors
class Child(Person):
    def __init__ (self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)

a = Child("Abhishake Anand", 21106004, "1000USD", "SWE-2")
a.display()