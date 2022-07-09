""" Create a class programmer for storing information of a few programmers working in Microsoft """

class programmer:
    company = "Microsoft"

    # building Constructor
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
    
    # print inf function
    def printInfo (self):
        print(f"Name: {self.name}\tID: {self.ID}.")

harry = programmer("Harry Patel", 21106032)
trans = programmer("Alice Johnson", 21106035)
harry.printInfo()
trans.printInfo()