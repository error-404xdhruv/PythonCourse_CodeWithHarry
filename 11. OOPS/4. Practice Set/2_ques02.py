# write a class calculator capable of finding square, cube and square root of a number

class calculator:
    def __init__(self, num):
        self.number = num

    def square (self):
        print(f"Square: {self.number**2}")
    def cube (self):
        print(f"Cube: {pow(self.number, 3)}")
    def squareRoot (self):
        # print(f"Square Root: {pow(self.number, 0.5)}")
        return pow(self.number, 0.5)

number = int(input())
a = calculator(number)
a.square()
a.cube()
b = float(a.squareRoot())
print("Square Root:",round(b, 2))