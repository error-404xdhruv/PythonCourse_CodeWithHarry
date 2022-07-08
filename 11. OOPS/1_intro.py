class RailwayForm :
    formType = "Railway Form"
    def printData (self):
        print(f"Name : {self.name}")
        print(f"Train : {self.train}")

newPassengersApplication = RailwayForm()
newPassengersApplication.name = "Dhruv"
newPassengersApplication.train = "Amritsar Mail"
newPassengersApplication.printData()