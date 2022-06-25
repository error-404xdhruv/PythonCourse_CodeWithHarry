
# implicit-type-conversion
x = 4
y = 4.5

print(type(x), type(y))
x = x+y
print(x, type(x))

#  explicit type converison
a = "69"

# conversion to int
print(int(a)+5)
# print(a+5) # but this thing would give error bcz a is a string and 5 is an integer

# conversion to string
d = 69
e = str(d)
print(type(e))

# conversion to float
e = float(a)
print(e)

# conversion from char to int using ord
c = '4'
x = ord(c)
print(type(x), x)
# it would print int 52 (now u must be wondering why 52 and not 4, bcz we are converting a char to int using ord function and it returns the ascii value of the character)

# conversion from int to hex
d = 56
print(hex(d))

# conversion from int to oct
print(oct(d))

# conversion of a string to tuples, list and set
word = "geeksforgeeks"

print(tuple(word))
print(set(word))
print(list(word))

# conversion to complex number
a, b = 1, 2
d = complex(a, b)
print(type(d))

age = input("Enter your age: ")
# by-default input function takes value as string
print(type(age))
print("Age after 2 years: ", int(age)+2)

year = int(input("Enter your birth year: "))
print(type(year))