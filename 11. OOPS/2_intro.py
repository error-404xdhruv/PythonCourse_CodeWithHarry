
# from datetime import date
from datetime import *

class Employee:
    company = "Google"
    salary = 10000
    def getSalary (self):
        print(f"Salary for this employee working in {self.company} is {self.salary}.")
# @staticmethod is used when we ned not pass some arguments to a function in class
    @staticmethod
    def greetEmployee (signature):
        print(f"Good Morning, Sir !\n{signature}")

    @staticmethod
    def dateTimeWhenEmployeeCameToWork ():
        today = date.today()
        now = datetime.now()
        # time = date.time()
        print(f'{now}')

harry = Employee()
harry.salary = 120000
harry.getSalary()
harry.dateTimeWhenEmployeeCameToWork()
harry.greetEmployee("Thanks!")

sampleEmployee = Employee()
sampleEmployee.getSalary()