# Write a class Train which has methods to book a ticket, get status (no. of seats) and get fare information of trains running under Indian Railways.

class Train():
    def __init__(self, name, seats, fare):
        self.name = name
        self.seats = seats
        self.fare = fare

    def getStatus(self):
        print(f"Name: {self.name}\t\tSeats: {self.seats}.")

    def printFare(self):
        print(f"Fare: Rs {self.fare}.")

    def BookTicket(self):
        if (self.seats > 0):
            print(f"Ticket Confirmed ; Seat Number: {301 - self.seats}.")
            self.seats -= 1
        else:
            print("Sorry, No more tickets Available.")

train1 = Train("Amritsar Mail, 6104405011", 300, 1599)
train1.getStatus()
train1.printFare()

askUser = int(
    input("Do you want to book a ticket ? Press 1 to Book a ticket and 0 to exit: "))
if (askUser == 1):
    n = int(input("How many ticket do you want to book: "))
    for i in range(0, n):
        train1.BookTicket()
print("Thank you for Visiting.")
