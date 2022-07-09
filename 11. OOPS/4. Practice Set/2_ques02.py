# write a class calculator capable of finding square, cube and square root of a number
class calculator:
    def printAfterCalc (self):
        print(f"Square: {self*self}\tCube: {pow(self, 3)}\tSquare Root: {pow(self, 1/2)}")

number = int(input())
number = calculator()
number.printAfterCalc()