
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