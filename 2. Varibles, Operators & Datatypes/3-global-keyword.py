
# global is a keyword which is used to modify a variable that is outside of the current scooe of the function

x = 15


def printX():
    global x
    x = x + 5
    print("Value of x inside the function:", x)


printX()

print("Value of x outside the function:", x)
