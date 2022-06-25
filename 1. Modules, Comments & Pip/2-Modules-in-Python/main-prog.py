
# we can import only one function from a module (here I have imported add function from calc.py module)
from calc import add

# or we can also import all the functions from a module
import calc

print(calc.add(2, 3))
print(calc.subtract(9, 7))