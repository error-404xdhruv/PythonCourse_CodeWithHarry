class Employee:
    company = "Google"
    salary = 10000
    def getSalary (self):
        print(f"Salary for this employee working in {self.company} is {self.salary}.")
# @staticmethod is used when we ned not pass some arguments to a function in class
    @staticmethod
    def greetEmployee (signature):
        print(f"Good Morning, Sir !\n{signature}")

harry = Employee()
harry.salary = 120000
harry.getSalary()
harry.greetEmployee("Thanks!")

sampleEmployee = Employee()
sampleEmployee.getSalary()