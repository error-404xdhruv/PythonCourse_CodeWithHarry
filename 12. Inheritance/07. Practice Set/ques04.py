# Write a class complex to represent Complex Numbers, along with overloaded operators + and * which adds and mulitply them.
class Complex:
    def __init__(self, r, i):
        self.real = r
        self.imaginary = i
    
    def __add__(self, c):
        return complex(self.real + c.real, self.imaginary + c.imaginary)

    def __mul__(self, c):
        mulReal = self.real*c.real - self.imaginary*c.imaginary
        mulImg = self.real*c.imaginary - self.imaginary*c.real
        return complex(mulReal, mulImg)
    
c1 = Complex(1, 4)
c2 = Complex(8, 5)
print(c1 + c2)
print(c1 * c2)