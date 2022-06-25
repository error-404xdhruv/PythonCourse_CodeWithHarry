
# Arithmetic Operators
from ast import If


a, b = 2, 10

add = a+b
subt = a-b
multiply = a*b
div1 = a/b
div2 = a//b
modulo = a % b
power = a**b
# a**b means a^b i.e., a to the power b

print(add)
print(subt)
print(multiply)
print(div1)
print(div2)
print(modulo)
print(power)

# Comparison Operator
a, b = 13, 33

print(a > b)
print(a < b)
print(a >= b)
print(a >= b)
print(a == b)
print(a != b)

# Logical Operators

a, b = 2, 2
if (a == 2 and b == 2):
    print("YES")
else:
    print("NO")

a, b = 0, 3
if (a == 0 or b == 0):
    print("YES")
else:
    print("NO")

a = True
print(not a)

# Bitwise Operators
a = 10
b = 4

print(a & b)

print(a | b)

print(~a)

print(a ^ b)

# a >> 1 gives a/2, a >> 2 gives (a/2)/2 and so on
print(a >> 2)

print(a << 2)

# Assignment Operators
a = 2
b = 4
c = b

a += 2
print(a)
# a += x means a = a + x, similar case with other assignments operators

# Identity Operators
print(b is c)
print(a is not b)

# Membership Operators

a, b = 2, 10
list = [2, 4, 6, 8]

if (a in list):
    print("Present")
else:
    print("No")
if (b not in list):
    print("Not in List")