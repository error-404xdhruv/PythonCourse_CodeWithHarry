
class Employee:
    company = "Google"

    # building Contructors
    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit

        print("Build Succeed!")
    
    # print the details
    def getDetails (self):
        print(f"Company: {self.company}")
        print(f"Name: {self.name}", end="  ;  ")
        print(f"Salary: {self.salary}", end= "  ;  ")
        print(f"Sub-unit: {self.subunit}")
    
harry = Employee("Harry Singh", 100000, "Alphabet")
harry.getDetails()