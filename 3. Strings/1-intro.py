
a = 2
b = "Hello World !"
print(type(a), type(b))

print("\n{")
s = "Hello"

# so one unique thing in python is that we can use negative indexing
print(s[-1])  # -1 means the first letter from right side
print(s[-5])

# remember that python is also a 0 based indexing language
print(s[0], s[4])
print("}\n")

# we can have single or double or even triple quoted strings
c = 'Hello World'
d = "Dhruv's"
print()
e = '''        Twinkle Twinkle Little Star
        How I wonder what you are !'''
print(c, d)
print(e)

# now hope the use of different quoted strings is clear

# concatinating string
print()
greet = "Good Morning, "
name = "Dhruv"
sent = greet + name
print(sent)

# as seen in C++ we can assign any random character to any index of a string, but the same is not allowed in Python
s[3] = 'E'
print(s)
# this would give an error: TypeError: 'str' object does not support item assignment